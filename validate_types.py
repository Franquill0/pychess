import subprocess
import sys

resultado = subprocess.run(
    [sys.executable, "-m", "mypy", "."],
    check=False,
)

sys.exit(resultado.returncode)