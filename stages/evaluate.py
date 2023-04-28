import argparse
import json
from pathlib import Path
import random
import yaml


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args_parser.add_argument('--dataset', dest='dataset', required=True)
    args = args_parser.parse_args()
    
    print("Stage: EVALUATE")
    print(f'Dataset: {args.dataset}')

    # Load main config (params.yaml)
    with open(args.config) as fd:
        params = yaml.safe_load(fd)

    print(f"INFO:  Running mode:     {params['run_mode']}")
    print(f"INFO:  Use stage config: {args.config}")
    print(f"INFO:  Evaluate params:  {params['evaluate']}")

    metric_names = params['evaluate']['metrics']
    metrics = {}

    for metric in metric_names:
        metrics[metric] = random.random()

    reports_dir = Path(params['reports_dir'])
    metrics_dir = reports_dir / params['evaluate']['metrics_dir']
    metrics_dir.mkdir(exist_ok=True)
    
    with open(metrics_dir / f'metrics_{args.dataset}.json', 'w') as metrics_file:
        json.dump(metrics, metrics_file)
