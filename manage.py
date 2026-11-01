#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    project_dir = Path(__file__).resolve().parent

    venv_python_candidates = [
        project_dir / ".venv" / "bin" / "python",
        project_dir.parent / ".venv" / "bin" / "python",
    ]

    for venv_python in venv_python_candidates:
        if venv_python.is_file():
            venv_dir = venv_python.parent.parent

            if Path(sys.prefix).resolve() != venv_dir.resolve():
                os.execv(
                    str(venv_python),
                    [str(venv_python), *sys.argv],
                )

            break

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "task_manager.settings",
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? "
            "Did you forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
