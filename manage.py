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
    else:
        uv_executable = "/bin/uv"

        if Path(uv_executable).is_file():
            os.execv(
                uv_executable,
                [
                    uv_executable,
                    "run",
                    "--project",
                    str(project_dir),
                    "python",
                    str(Path(__file__).resolve()),
                    *sys.argv[1:],
                ],
            )

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "task_manager.settings",
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
