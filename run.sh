#!/bin/bash
set -e
set -u
set -o pipefail

log() {
    local fname=${BASH_SOURCE[1]##*/}
    echo -e "$(date '+%Y-%m-%dT%H:%M:%S') (${fname}:${BASH_LINENO[0]}:${FUNCNAME[1]}) $*"
}

stage=1
stop_stage=10000
egs=mock
skip_done=false
mock=true

. parse_options.sh

egs_dir=egs/${egs}

if [ ${stage} -le 1 ] && [ ${stop_stage} -ge 1 ]; then
    echo "Stage 1: Crawl data"
    _opts=" "
    if [ ! -f ${egs_dir}/data.json ] || ! "${skip_done}" ; then
        if [ ${stop_stage} -gt 1 ] &&  "${mock}" ; then 
            _opts+="--mock "
        fi
        python -m k_shortest_path.crawler ${egs_dir}/config.yaml ${_opts}
    else
        log data.json exists. Skip crawling...
    fi
fi

if [ ${stage} -le 2 ] && [ ${stop_stage} -ge 2 ]; then
    echo "Stage 2: Create graph"
    _opts=" "
    if [ ! -f ${egs_dir}/graph.gml ] || ! "${skip_done}"; then 
        if [ ${stop_stage} -gt 2 ] && "${mock}"; then 
            _opts+="--mock "
        fi
        python -m k_shortest_path.json2graph ${egs_dir}/data.json ${egs_dir}/graph.gml ${_opts}
    else 
        log graph.gml exists. Skip creating...
    fi
fi

if [ ${stage} -le 3 ] && [ ${stop_stage} -ge 3 ]; then
    echo "Stage 3: Visualize data"
    python -m k_shortest_path.visualization ${egs_dir}/graph.gml ${egs_dir}/viz_config.yaml
fi