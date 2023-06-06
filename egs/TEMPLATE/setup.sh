#!/bin/bash
log() {
    local fname=${BASH_SOURCE[1]##*/}
    echo -e "$(date '+%Y-%m-%dT%H:%M:%S') (${fname}:${BASH_LINENO[0]}:${FUNCNAME[1]}) $*"
}

help_message=$(cat << EOF
Usage: $0 <target-dir>
EOF
)

if [ $# -ne 1 ]; then
    log "${help_message}"
    log "Error: 1 positional argument is required."
    exit 2
fi


dir=$1
mkdir -p "${dir}"

if [ ! -d "${dir}"/../TEMPLATE ]; then
    log "Error: ${dir}/../TEMPLATE should exist. You may specify wrong directory."
    exit 1
fi

targets=""

# Copy
for f in run.sh local; do
    target="${dir}"/../TEMPLATE/"${f}"
    cp -r "${target}" "${dir}"
    targets+="${dir}/${target} "
done

log "Created: ${targets}"