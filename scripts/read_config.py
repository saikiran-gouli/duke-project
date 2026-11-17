import sys
import yaml
 
# Get the YAML filename passed from GitHub Actions
config_file = sys.argv[1]
 
# Build the complete path
config_path = f"configs/{config_file}"
 
print(f"Reading configuration from: {config_path}")
 
# Open and read the YAML file
with open(config_path, "r") as file:
    config = yaml.safe_load(file)
 
# Read individual values
environment = config["environment"]
aws_region = config["aws_region"]
application = config["application"]
action = config["action"]
 
print("Configuration loaded successfully")
print(f"Environment : {environment}")
print(f"AWS Region  : {aws_region}")
print(f"Application : {application}")
print(f"Action      : {action}")
