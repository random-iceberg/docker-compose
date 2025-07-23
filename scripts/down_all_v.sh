#!/usr/bin/env sh
set -eu

docker compose ls 2>/dev/null || true

running_icebergs() {
    docker compose ls | awk '$1 ~ /^random-iceberg/ { print }'
}

their_config() {
    running_icebergs | awk '{print $3}' | sed -e 's/^/-f /' -e 's/,/ -f /g'
}

if [ -n "$(running_icebergs)" ]; then
    their_config | xargs -r -I{} sh -c "docker compose {} down -v --remove-orphans"
fi
