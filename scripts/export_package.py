#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
# --- How to run ---
# python3 scripts/export_package.py --dry-run
# python3 scripts/export_package.py
from __future__ import annotations

import argparse
import hashlib
import os
import tarfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Final


ROOT: Final = Path(__file__).resolve().parents[1]
DIST: Final = ROOT / "dist"
VERSION: Final = "v0.6.5"
ARCHIVE_NAME: Final = f"cfd-ai-paper-skills-{VERSION}.tar.gz"
PRIVATE_STATE_DIR: Final = "." + ("ta" + "rs")
TRANSIENT_DIRS: Final = frozenset(("__pycache__", ".tmp_pycache", "dist", ".git", "." + "omo", PRIVATE_STATE_DIR))
TRANSIENT_SUFFIXES: Final = (".synctex.gz",)
TRANSIENT_NAMES: Final = frozenset((".DS_Store", ".gitignore"))
NOISY_EXTENSIONS: Final = frozenset((".aux", ".log", ".out"))


@dataclass(frozen=True)
class PackageFile:
    __slots__ = ("path", "relative", "size")

    path: Path
    relative: Path
    size: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export the CFD-AI paper skills package.")
    parser.add_argument("--dry-run", action="store_true", help="List package contents without writing dist files.")
    return parser.parse_args()


def should_exclude(path: Path) -> bool:
    if any(part in TRANSIENT_DIRS for part in path.parts):
        return True
    if path.name in TRANSIENT_NAMES:
        return True
    if path.name.endswith(TRANSIENT_SUFFIXES):
        return True
    if path.suffix in NOISY_EXTENSIONS:
        return True
    return False


def collect_files() -> list[PackageFile]:
    files: list[PackageFile] = []
    for directory, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(dirname for dirname in dirnames if dirname not in TRANSIENT_DIRS)
        root = Path(directory)
        for filename in sorted(filenames):
            path = root / filename
            relative = path.relative_to(ROOT)
            if should_exclude(relative):
                continue
            files.append(PackageFile(path=path, relative=relative, size=path.stat().st_size))
    return sorted(files, key=lambda item: item.relative.as_posix())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def render_manifest(files: list[PackageFile]) -> str:
    total_size = sum(item.size for item in files)
    lines = [
        f"# CFD-AI Paper Skills Package {VERSION} Manifest",
        "",
        f"- Created: {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"- File count: {len(files)}",
        f"- Uncompressed bytes: {total_size}",
        f"- Archive: `dist/{ARCHIVE_NAME}`",
        "",
        "## Included Files",
        "",
        "| Path | Bytes |",
        "|---|---:|",
    ]
    for item in files:
        lines.append(f"| `{item.relative.as_posix()}` | {item.size} |")
    lines.append("")
    return "\n".join(lines)


def render_install() -> str:
    return "\n".join(
        [
            "# Install Notes",
            "",
            "This archive is a source package for the CFD-AI paper skills package.",
            "Use the root `SKILL.md` as the umbrella entrypoint, then route to focused subskills under `skills/*/SKILL.md` as needed.",
            "",
            "## Validate the package",
            "",
            "```bash",
            f"tar -xzf {ARCHIVE_NAME}",
            f"cd cfd-ai-paper-skills-{VERSION}",
            "python3 scripts/validate_package.py",
            "python3 scripts/run_static_evals.py",
            "python3 scripts/export_package.py --dry-run",
            "```",
            "",
            "## Codex native subagents",
            "",
            "Start Codex from the package root so `.codex/agents/` is visible:",
            "",
            "```bash",
            "codex",
            "```",
            "",
            "Then paste one of `.codex/prompts/iterative-edit-review-loop.md`, `.codex/prompts/multi-agent-abstract-rescue.md`, or `.codex/prompts/full-paper-reviewer-editor.md`.",
            "",
            "## Local skill install pattern",
            "",
            "For local skill managers, keep the repository intact so references, rubrics, examples, templates, and Codex agent files stay reachable.",
            "",
            "```bash",
            "mkdir -p ~/.hermes/skills/research",
            "ln -s \"$PWD\" ~/.hermes/skills/research/cfd-ai-paper-skills",
            "hermes skills list | grep cfd-ai-paper-skills",
            "```",
            "",
            "No external credentials are required for deterministic validators. Tectonic is optional and only needed for LaTeX/PDF benchmark compilation.",
            "",
        ],
    )


def write_checksums(files: list[Path], destination: Path) -> None:
    lines = [f"{sha256(path)}  {path.relative_to(ROOT).as_posix()}" for path in files]
    destination.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_archive(files: list[PackageFile], archive_path: Path) -> None:
    with tarfile.open(archive_path, "w:gz") as archive:
        for item in files:
            archive.add(item.path, arcname=Path(f"cfd-ai-paper-skills-{VERSION}") / item.relative)


def remove_stale_archives(archive_path: Path) -> None:
    for stale_archive in DIST.glob("cfd-ai-paper-skills-v*.tar.gz"):
        if stale_archive == archive_path:
            continue
        stale_archive.unlink()


def main() -> int:
    args = parse_args()
    files = collect_files()
    if args.dry_run:
        print(f"dry-run: {len(files)} files would be packaged into dist/{ARCHIVE_NAME}")
        for item in files:
            print(item.relative.as_posix())
        return 0

    DIST.mkdir(parents=True, exist_ok=True)
    archive_path = DIST / ARCHIVE_NAME
    manifest_path = DIST / "MANIFEST.md"
    checksums_path = DIST / "CHECKSUMS.txt"
    install_path = DIST / "INSTALL.md"
    remove_stale_archives(archive_path)
    manifest_path.write_text(render_manifest(files), encoding="utf-8")
    install_path.write_text(render_install(), encoding="utf-8")
    files_with_dist = files + [
        PackageFile(path=manifest_path, relative=manifest_path.relative_to(ROOT), size=manifest_path.stat().st_size),
        PackageFile(path=install_path, relative=install_path.relative_to(ROOT), size=install_path.stat().st_size),
    ]
    write_archive(files_with_dist, archive_path)
    write_checksums([archive_path, manifest_path, install_path], checksums_path)
    print(f"created {archive_path.relative_to(ROOT)}")
    print(f"created {manifest_path.relative_to(ROOT)}")
    print(f"created {checksums_path.relative_to(ROOT)}")
    print(f"created {install_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
