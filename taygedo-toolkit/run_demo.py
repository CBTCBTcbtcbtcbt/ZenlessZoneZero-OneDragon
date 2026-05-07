import os
import subprocess
import sys
from pathlib import Path


# Helper launcher for IDE run configuration.
def main() -> int:
    root = Path(__file__).resolve().parents[1]
    env = os.environ.copy()

    extra_paths = [str(root / "src"), str(root / "taygedo-toolkit" / "src")]
    current = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = os.pathsep.join(extra_paths + ([current] if current else []))

    cmd = [sys.executable, "-m", "taygedo_toolkit.launcher.cli", *sys.argv[1:]]
    return subprocess.call(cmd, cwd=str(root), env=env)


if __name__ == "__main__":
    raise SystemExit(main())
