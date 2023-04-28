import yaml


print("Stage: TRAIN")

with open("params.yaml") as fd:
    params = yaml.safe_load(fd)

# get stage configs 
train_config = params['train']

print(f"DEBUG: params:   {train_config}")
