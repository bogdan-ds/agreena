import os

from src import config

from src.request_items import BoundingBox
from src.sentinel_client import SentinelClient
from src.utils import find_bbox_file


def get_image(bbox: BoundingBox, path: str) -> str:
    """Get image from Sentinel Hub or local cache.

    Args:
        bbox: BoundingBox object
        path: str path to download images to
    Returns:
        str path of file
    """
    bbox_file = find_bbox_file(path, bbox.serialize())
    if bbox_file:
        return bbox_file[0]

    client = SentinelClient(config.sci_hub_user, config.sci_hub_pass,
                            download_path=path)
    uuid, title = client.get_first_sentinel_product(bbox)
    client.download_quicklook_for_product(uuid, title)
    return os.path.join(config.download_path, title + ".jpeg")
