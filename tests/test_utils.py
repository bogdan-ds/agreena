from src.request_items import BoundingBox
from src.utils import convert_bounding_box_to_wkt, find_bbox_file, \
    get_predominant_rgb_colour_in_image, rgb_to_colour_name


def test_convert_bounding_box_to_wkt():
    """
    Test convert_bounding_box_to_wkt function.
    """
    bounding_box = BoundingBox(minLong=24.644842122715147,
                               minLat=42.06253714023231,
                               maxLong=24.89038637385545,
                               maxLat=42.19082231860318)
    expected_result = "POLYGON((24.644842122715147 42.19082231860318, " \
                      "24.644842122715147 42.06253714023231, " \
                      "24.89038637385545 42.06253714023231, " \
                      "24.89038637385545 42.19082231860318, " \
                      "24.644842122715147 42.19082231860318))"
    result = convert_bounding_box_to_wkt(bounding_box)
    assert result == expected_result


def test_find_bbox_file():
    """
    Test find_bbox_file function.
    """
    path = "tests/assets"
    bounding_box = BoundingBox(minLong=24.644842122715147,
                               minLat=42.06253714023231,
                               maxLong=24.89038637385545,
                               maxLat=42.19082231860318)
    serialized_bbox = bounding_box.serialize()
    expected_result = ["tests/assets/4124203033336938628.jpg"]
    result = find_bbox_file(path, serialized_bbox)
    assert result == expected_result


def test_get_predominant_rgb_colour_in_image():
    """
    Test get_predominant_colour_in_image function.
    """
    image_path = "tests/assets/test.jpg"
    expected_result = (220, 217, 208)
    result = get_predominant_rgb_colour_in_image(image_path)
    assert result == expected_result


def test_rgb_to_colour_name():
    """
    Test rgb_to_colour_name function.
    """
    rgb = (220, 217, 208)
    expected_result = "white"
    result = rgb_to_colour_name(rgb)
    assert result == expected_result
