set -xe

docker compose ls

function running_icebergs {
    docker compose ls | (grep ^random-iceberg || test $? = 1)
}

running_icebergs

function their_config {
    running_icebergs | awk '{print $3}' | sed 's/^/-f /' | sed 's/,/ -f /g'
}

their_config

their_config | xargs -i sh -c 'docker compose {} down -v --remove-orphans'

