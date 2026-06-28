import sys
from pathlib import Path

# Ensure the project root is on sys.path so `app` is importable
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.main import app  # noqa: E402, F401 — re-exported for Vercel

__all__ = ["app"]
