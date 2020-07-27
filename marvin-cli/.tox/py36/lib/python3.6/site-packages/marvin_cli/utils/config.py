import os
import copy
import json
import configparser

def parse_ini(inipath, defaults=None):
    if defaults is None:
        defaults = {}

    config_raw = configparser.ConfigParser()
    config_raw.read(inipath)

    config = copy.deepcopy(defaults)

    for section in config_raw.sections():
        # Firt pass
        for key, value in config_raw.items(section):
            key = '_'.join((section, key)).lower()
            processed_value = value.format(**config)
            config[key] = processed_value

    # Second pass
    for key, value in config.items():
        processed_value = value.format(**config)
        if ',' in processed_value:
            processed_value = processed_value.split(',')
        config[key] = processed_value

    return config

def read_cli_conf():
    file_path = os.path.join(os.environ['MARVIN_DATA_PATH'], '.conf', 'cli_conf.json')
    with open(file_path, 'r') as conf_file:
        return json.load(conf_file)

def generate_default_conf():
    filepath = os.path.join(os.environ['MARVIN_DATA_PATH'], '.conf', 'cli_conf.json')
    config = {
        'default_host': 'localhost',
        'editor': 'nano',
        'executor_url': 'https://s3.amazonaws.com/marvin-engine-executor/marvin-engine-executor-assembly-0.0.5.jar'
    }
    with open(filepath, 'w') as conf:
        json.dump(config, conf, indent=4)

    return config