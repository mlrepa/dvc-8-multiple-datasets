import argparse
import json
from pathlib import Path
import yaml


if __name__ == '__main__':

    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--config', dest='config', required=True)
    args = args_parser.parse_args()

    print("Stage: COLLECT_METRICS")

    # Load main config (params.yaml)
    with open(args.config) as fd:
        params = yaml.safe_load(fd)

    reports_dir = Path(params['reports_dir'])
    metrics_dir = reports_dir / params['evaluate']['metrics_dir']
    datasets = params['evaluate']['datasets']

    metrics = {}

    for ds in datasets:

        ds_path = metrics_dir / f'metrics_{ds}.json'

        with open(ds_path) as ds_file:
            ds_metrics = json.load(ds_file)

        metrics[ds] = ds_metrics

    metrics_path = reports_dir / params['collect_metrics']['metrics']

    with open(metrics_path, 'w') as metrics_file:
        json.dump(metrics, metrics_file, indent=4)
