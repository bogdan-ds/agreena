import glob
import math

from PIL import Image

from src.request_items import BoundingBox


def convert_bounding_box_to_wkt(bounding_box: BoundingBox) -> str:
    """
    Convert bounding box to a WKT polygon.

    Args:
        bounding_box: BoundingBox object
    Returns:
        str WKT polygon
    """
    return 'POLYGON(({0} {3}, {0} {1}, ' \
           '{2} {1}, {2} {3}, {0} {3}))'.format(*bounding_box.to_tuple())


def find_bbox_file(path: str, serialized_bbox: str) -> list:
    """
    Find serialized bbox filename in path.

    Args:
        path: str path to search
        serialized_bbox: str serialized bbox
    Returns:
        list of str filenames or emtpy list if not found
    """
    return glob.glob(f"{path}/{serialized_bbox}.*")


def get_predominant_rgb_colour_in_image(image_path: str) -> tuple:
    """
    Get predominant RGB colour in image.

    Args:
        image_path: str path to image
    Returns:
        tuple representing RGB colour
    """
    image = Image.open(image_path)
    width, height = image.size
    pixels = image.getcolors(width * height)
    sorted_pixels = sorted(pixels, key=lambda t: t[0], reverse=True)
    most_common_rgb = sorted_pixels[0][1]
    return most_common_rgb


def rgb_to_colour_name(rgb: tuple) -> str:
    """
    Convert RGB tuple to colour name. Measures distance between RGB tuple and
    known colours and returns the closest match. RGB colours are represented by
    a tuple of three integers between 0 and 255, these can be treated as points
    in a 3D space. The distance between two points in 3D space is calculated by
    the dist method, which gives the Euclidean distance between two points.

    Args:
        rgb: tuple representing RGB colour
    Returns:
        str colour name
    """
    colours = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "yellow": (255, 255, 0),
        "magenta": (255, 0, 255),
        "cyan": (0, 255, 255),
        "black": (0, 0, 0),
        "white": (255, 255, 255)
    }
    distances = dict()
    for colour, rgb_colour in colours.items():
        distances[colour] = math.dist(rgb, rgb_colour)
    return min(distances, key=distances.get)
