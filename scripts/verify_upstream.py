"""Verify official submodule URLs and immutable commits without ML dependencies."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main():
    lock = json.loads((ROOT / "docs/upstream-lock.json").read_text(encoding="utf-8"))
    expected = {f"upstream/{name}" for name in (
        "assignment1-basics", "assignment2-systems", "assignment3-scaling",
        "assignment4-data", "assignment5-alignment", "lectures")}
    entries = lock["submodules"]
    assert len(entries) == len(expected)
    assert {entry["path"] for entry in entries} == expected
    configured = git("config", "-f", ".gitmodules", "--get-regexp", r"^submodule\..*\.path$")
    assert {line.split(maxsplit=1)[1] for line in configured.splitlines()} == expected
    for entry in entries:
        path, sha, url = entry["path"], entry["commit"], entry["url"]
        assert re.fullmatch(r"[0-9a-f]{40}", sha), path
        assert url == f"https://github.com/stanford-cs336/{Path(path).name}.git", path
        assert git("config", "-f", ".gitmodules", "--get", f"submodule.{path}.url") == url, path
        staged = git("ls-files", "--stage", "--", path).split()
        assert staged[:2] == ["160000", sha], f"gitlink mismatch: {path}"
        assert git("-C", path, "rev-parse", "HEAD") == sha, f"checkout mismatch: {path}"
        print(f"OK {path} {sha}")
    print("Verified 6 official submodules; assignment tests/training were not run.")


if __name__ == "__main__":
    main()
