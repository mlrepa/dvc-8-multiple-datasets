import yaml


print("Stage: DATA_LOAD")

with open("params.yaml") as fd:
    params = yaml.safe_load(fd)

# get stage configs
data_load_config = params['data_load']
if data_load_config['sampling']['enable'] is True:
    sampling_size = data_load_config['sampling']['size']

print(f"DEBUG: dataset:  {data_load_config['dataset']}")
print(f"INFO:  Sampling size: {sampling_size}")
