#!/usr/bin/env bash

# Instalamos uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source "$HOME/.local/bin/env"

# Instalamos dependencias y preparamos Django
make install
make collectstatic
make migrate
