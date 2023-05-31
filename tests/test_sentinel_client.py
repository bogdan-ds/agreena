import os

from src import config
from src.request_items import BoundingBox
from src.sentinel_client import SentinelClient


def test_sentinel_product_request():
    client = SentinelClient(config.sci_hub_user, config.sci_hub_pass,
                            download_path="tests/assets")
    bounding_box = BoundingBox(minLong=24.644842122715147,
                               minLat=42.06253714023231,
                               maxLong=24.89038637385545,
                               maxLat=42.19082231860318)
    print(f"User: {config.sci_hub_user} Password: {config.sci_hub_pass}")
    uuid, title = client.get_first_sentinel_product(bounding_box)
    assert uuid is not None and title is not None


def test_download_quicklook_for_product():
    client = SentinelClient(config.sci_hub_user, config.sci_hub_pass,
                            download_path="tests/assets")
    uuid = "6a7c0616-53f4-4e36-9c46-256e6a2dc0a0"
    title = \
        "S1A_IW_SLC__1SDV_20230524T160833_20230524T160900_048678_05DACA_C7FF"
    client.download_quicklook_for_product(uuid, title)
    assert os.path.exists(os.path.join(client.download_path, title + ".jpeg"))
    os.remove(os.path.join(client.download_path, title + ".jpeg"))


def test_quicklook_exists():
    client = SentinelClient(config.sci_hub_user, config.sci_hub_pass,
                            download_path="tests/assets")
    title = \
        "S1A_IW_SLC__1SDV_20230517T161643_20230517T161710_048576_05D7B7_2D7F"
    assert client.quicklook_exists(title) is True
