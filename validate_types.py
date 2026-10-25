import subprocess
import sys

result = subprocess.run(
    [sys.executable, "-m", "mypy", "."],
    check=False,
)

sys.exit(result.returncode)