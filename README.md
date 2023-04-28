# Pattern: Multiple datasets for validation 

## Install

```bash
python3 -m venv .venv
echo 'export PYTHONPATH=.' >> .venv/bin/activate
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Run
1. Define list of datasets we need to run evaluation on in `params.yaml`
Example: 
```yaml
evaluate:
  datasets: ['micro', 'customer-1', 'customer-2']
  ...
```

2. Setup `evaluate` stage with `foreach` templating syntax in `dvc.yaml` 
```yaml
  evaluate:
    foreach:
      ${evaluate.datasets}
    do:
      cmd: python stages/evaluate.py --config=params.yaml --dataset=${item}
      deps:
      ...
      params:
      ...
      metrics:
      - ${reports_dir}/${evaluate.metrics_dir}/metrics_${item}.json:
          cache: false
```

3. (Optional) Collect metrics into a single `metrics.json` file and run metrics value range checks in separate stages 
```yaml 
  collect_metrics:
    cmd: python stages/collect_metrics.py --config=params.yaml
    deps:
    ...
    - ${reports_dir}/${evaluate.metrics_dir}
    params:
    ...
    metrics:
    - ${reports_dir}/${collect_metrics.metrics}:
        cache: false
  
  check_metrics:
    cmd: python stages/check_metrics.py --config=params.yaml
    deps:
    ...
    - ${reports_dir}/${collect_metrics.metrics}
    params:
    ...
    plots:
    - ${reports_dir}/${check_metrics.report}:
        cache: false
```

Run pipeline
```bash
dvc exp run
```