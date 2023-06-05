# K-shortest path 

## egs structure
### Configuration files 
- config.yaml: Config for crawler
- viz_config.yaml: Config for visualization

### Output files
- data.json: Output of crawler step (stage 1 in `run.sh`).
- graph.gml: The created graph from the data crawled (stage 2 in `run.sh`).
- [source]--[dest]/[k].pdf: k-shortest-path visualization from [source] to [dest] (stage 3 in `run.sh`).

## Run instructions for `run.sh`
[NOTE FOR TEAM]: Currently, please `run_mock.sh` for processing on fake data when other teammates are implementing previous stages. The process of running `run_mock.sh` is absolutely similar to `run.sh`, except the data is fake.

1. Create `.env` file and put every API KEY needed (for crawler)
2. Run `run.sh`. Parameters for `run.sh` scripts are:
- `stage`: Start stage 
- `stop_stage`: Stop stage 
- `egs`: Path to recipe directory
- `skip_done`: Whether to skip stage if it has been completed before (bug now, the script currently always skip completed stage)

You can modify the parameters in `run.sh` or override in the command line using `--`

- Example usage: 

This script will crawl the map, then stop.
```sh
./run.sh --stage 1 --stop_stage 1 --egs hcmut_map
```

This script will crawl the map, build the graph, then stop.
```sh
./run.sh --stage 1 --stop_stage 2 --egs hcmut_map
```

This script will build the graph, then run visualization
```sh
./run.sh --stage 2 --stop_stage 3 --egs hcmut_map
```

