import sys
from typing import TYPE_CHECKING

from . import main

if TYPE_CHECKING:
    from subprocess import CompletedProcess

completed_process: "CompletedProcess" = main()
sys.exit(completed_process.returncode)
