from src.request_items import BoundingBox
from src.tasks import get_image


def test_serialized_bbox_file_exists():
    bounding_box = BoundingBox(minLong=24.644842122715147,
                               minLat=42.06253714023231,
                               maxLong=24.89038637385545,
                               maxLat=42.19082231860318)
    file = get_image(bounding_box, "tests/assets")
    assert file == "tests/assets/4124203033336938628.jpg"
