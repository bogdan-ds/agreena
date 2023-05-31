import os

from typing import Tuple
from sentinelsat import SentinelAPI

from src.request_items import BoundingBox
from src.utils import convert_bounding_box_to_wkt


class SentinelClient:
    """Client for Sentinel Hub API.

    Attributes:
        api: SentinelAPI object
        download_path: Path to download images to
    """

    def __init__(self, user: str, password: str,
                 api_url: str = "https://apihub.copernicus.eu/apihub",
                 download_path: str = "./assets"):
        self.api = SentinelAPI(user, password, api_url)
        self.download_path = download_path

    def get_first_sentinel_product(self, bounding_box: BoundingBox) -> \
            Tuple[str, str]:
        """
        Get Sentinel image from SciHub.

        Args:
            bounding_box: BoundingBox object
        Returns:
            Tuple of uuid and title as str
        """
        footprint = convert_bounding_box_to_wkt(bounding_box)
        products = self.api.query(footprint,
                                  platformname='Sentinel-1',
                                  producttype='SLC',
                                  orbitdirection='ASCENDING',
                                  limit=1)

        uuid = list(products.keys())[0]
        title = products[uuid]["title"]
        return uuid, title

    def download_quicklook_for_product(self, uuid: str, title: str) -> None:
        """
        Download preview from Sentinel product.

        Args:
            uuid: str uuid of product
            title: str title of product
        """
        if not self.quicklook_exists(title):
            response = self.api.download_quicklook(
                uuid, directory_path=self.download_path)
            error = response.get("error", "")
            if error != "":
                raise Exception(error)

    def quicklook_exists(self, title: str) -> bool:
        """
        Check if quicklook is already downloaded in the download path.

        Args:
            title: str title of product
        Returns:
            bool True if quicklook exists, False otherwise
        """
        return os.path.exists(os.path.join(self.download_path, title + ".jpeg"))
