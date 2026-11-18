# import sys
# import yaml
 
# # Get the YAML filename passed from GitHub Actions
# config_file = sys.argv[1]
 
# # Build the complete path
# config_path = f"configs/{config_file}"
 
# print(f"Reading configuration from: {config_path}")
 
# # Open and read the YAML file
# with open(config_path, "r") as file:
#     config = yaml.safe_load(file)
 
# # Read individual values
# environment = config["environment"]
# aws_region = config["aws_region"]
# application = config["application"]
# action = config["action"]
 
# print("Configuration loaded successfully")
# print(f"Environment : {environment}")
# print(f"AWS Region  : {aws_region}")
# print(f"Application : {application}")
# print(f"Action      : {action}")


# import sys
# import yaml
 
# config_file = sys.argv[1]
# config_path = f"configs/{config_file}"
 
# print(f"Reading configuration from: {config_path}")
 
# with open(config_path, "r") as file:
#     config = yaml.safe_load(file)
 
# print("CONFIG VALUE:")
# print(config)
 
# print("CONFIG TYPE:")
# print(type(config))
 
# environment = config["environment"]
# aws_region = config["aws_region"]
# application = config["application"]
# action = config["action"]
 
# print(f"Environment : {environment}")
# print(f"AWS Region  : {aws_region}")
# print(f"Application : {application}")
# print(f"Action      : {action}")



import sys
import yaml
 
config_file = sys.argv[1]
config_path = f"configs/{config_file}"
 
print(f"Reading configuration from: {config_path}")
 
with open(config_path, "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)
 
print(f"Parsed YAML type: {type(config).__name__}")
print(f"Parsed YAML value: {config}")
 
if not isinstance(config, dict):
    raise ValueError(
        f"Expected '{config_path}' to contain a YAML mapping, "
        f"but received {type(config).__name__}: {config!r}"
    )
 
environment = config["environment"]
aws_region = config["aws_region"]
application = config["application"]
action = config["action"]
 
print("Configuration loaded successfully")
print(f"Environment : {environment}")
print(f"AWS Region  : {aws_region}")
print(f"Application : {application}")
print(f"Action      : {action}")
