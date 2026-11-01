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
        diagnostics = [
            f"Python executable: {sys.executable}",
            f"Python prefix: {sys.prefix}",
            f"Python base prefix: {sys.base_prefix}",
            f"Project directory: {project_dir}",
            "Virtual environment candidates:",
        ]

        for candidate in venv_python_candidates:
            diagnostics.append(
                f"  {candidate}: exists={candidate.is_file()}"
            )

        raise ImportError(
            "Couldn't import Django.\n" + "\n".join(diagnostics)
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
