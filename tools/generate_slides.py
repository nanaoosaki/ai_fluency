#!/usr/bin/env python3
"""Compatibility entry point for the prompt-first generated-slide workflow.

Use `tools/generate_visuals.py` directly for new work.
"""

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.generate_visuals import main


if __name__ == "__main__":
    print(
        "Note: generate_slides.py now delegates to the prompt-first generated-slide "
        "workflow in tools/generate_visuals.py."
    )
    main()
