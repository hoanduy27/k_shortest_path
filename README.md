# K-shortest path 

## egs structure
### Configuration files 
- config.yaml: Config for crawler
- viz_config.yaml: Config for visualization

We've prepared the [TEMPLATE egs](egs/TEMPLATE) for demonstration how to write a config.


### Output files
- data.json: Output of crawler step (stage 1 in `run.sh`).
- graph.gml: The created graph from the data crawled (stage 2 in `run.sh`).
- [source]--[dest]/[k].pdf: k-shortest-path visualization from [source] to [dest] (stage 3 in `run.sh`).

## Run instructions for `run.sh`

1. Create `.env` file and put every API KEY needed (for crawler)
2. Run `run.sh` (type `./run.sh --help` for instruction)

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

## Create a new recipe
```sh
cd egs/TEMPLATE/
./setup.sh </path/to/new_recipe>
```


## Using mock data for `run.sh` 
You can use mock data for `run.sh` as follow:

This script will run your real code in stage 2 to build the graph, using mock data in stage 1
```sh
./run.sh --stage 1 --stop_stage 2 --mock true
```

This script will run your real code in stage 3 to visualize the result, using mock data in stage 1 and stage 2
```sh
./run.sh --stage 1 --stop_stage 3 --mock true
```
