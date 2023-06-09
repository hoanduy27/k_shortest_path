import os 
import argparse
import yaml
from typing import Dict
import json
from dotenv import load_dotenv
from .mock_data import *
import osmnx as ox

load_dotenv()

class BaseCrawler:
    """
    A Base Crawler class

    Args:
        center_longtitude: The longtitude of the center point
        center_latitude: The latitude of the center point
        radius: The radius from the center point to get other points
        num_points: Number of points to make a map (including center point)
        result_file: path to json file to write the map data
        seed: random seed
    """
    def __init__(
            self, 
            center_longtitude: float,
            center_lattitude: float, 
            radius: float, 
            num_points: int,
            result_file: str, 
            seed=None,
            *args, **kwargs
        ):

        self.center_longtitude = center_longtitude
        self.center_lattitude = center_lattitude
        self.radius = radius
        self.result_file = result_file
        self.num_points = num_points
        self.seed = seed 

    def crawl(self) -> dict:
        raise NotImplementedError
    
    def __call__(self):
        result = self.crawl()
        with open(self.result_file, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
    @classmethod
    def from_config(cls, config_path: str):
        with open(config_path, 'r') as f:
            config_params = yaml.load(f, Loader=yaml.Loader)

        if 'result_file' not in config_params:
            result_dir = os.path.dirname(config_path)
            result_file = os.path.join(result_dir, 'data.json')
            config_params.update(dict(result_file = result_file))
        
        return cls(**config_params)

class MockCrawler(BaseCrawler):
    def __init__(self, *args, **kwargs):
        super(MockCrawler, self).__init__(*args, **kwargs)
        self.crawler = self.load_crawler()

    def load_crawler(self):
        API_KEY=os.environ.get('API_KEY', None)
        
        crawler = f'Using {API_KEY}'
        print(crawler)

        return crawler
    
    def crawl(self) -> dict:
        return mock_map_data

class Crawler(BaseCrawler):
    def __init__(self, *args, **kwargs):
        super(Crawler, self).__init__(*args, **kwargs)
        # TODO: add your custom parameters if needed (you can modify __init__ params)

    def crawl(self) -> dict:
        geometries = ox.geometries_from_point(
            (self.center_lattitude, self.center_longtitude),
            {'building': True},
            dist=self.radius,
        )
        way = geometries[geometries['addr:street'].notnull()][['addr:street', 'geometry', 'nodes']]
        map_data = {}
        for w in way.values:
            for indx, node in enumerate(w[2]):
                if node not in map_data:
                    xx, yy = w[1].exterior.coords.xy
                    reachable_to = set(w[2])
                    reachable_to.remove(node)
                    map_data[node] = {
                        "longtitude": xx[indx],
                        "lattitude": yy[indx],
                        "street": w[0],
                        "reachable_to": list(reachable_to)
                    }
                else:
                    reachable_to_set = set(w[2] + map_data[node]['reachable_to'])
                    reachable_to_set.remove(node)
                    map_data[node]['reachable_to'] = list(reachable_to_set)
        return map_data

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_path', 
        type=str, 
        help='path to config file'
    )
    parser.add_argument(
        '--mock', 
        action='store_true', 
        help='Whether to mock the data'
    )
    args = parser.parse_args()

    if args.mock:
        crawler_class = MockCrawler
    else:
        crawler_class = Crawler
    
    crawler = crawler_class.from_config(args.config_path)
    crawler()

if __name__ == '__main__':
    main()