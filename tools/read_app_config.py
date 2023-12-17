import os
import json

from . import directories

SETTING_FILEPATH = directories.BASE_DIR / os.environ['TSM_APP_SETTINGS']
with open(SETTING_FILEPATH, 'r') as f:
    SETTING_CONFIG = json.load(f)

def read_secret_key():
    return SETTING_CONFIG['secret_key']


def read_database_config():
    return SETTING_CONFIG['database']