import os


sci_hub_user = os.getenv('SCI_HUB_USER', None)
sci_hub_pass = os.getenv('SCI_HUB_PASS', None)

if not sci_hub_user and not sci_hub_pass:
    raise Exception('Please set SCI_HUB_USER and SCI_HUB_PASS env variables')

download_path = os.getenv('DOWNLOAD_PATH', 'assets')
