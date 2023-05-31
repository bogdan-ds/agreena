import pytest

from src.request_items import BoundingBox


def test_latitude_validation():
    with pytest.raises(ValueError):
        BoundingBox(minLong=24.644842122715147,
                    minLat=42.06253714023231,
                    maxLong=24.89038637385545,
                    maxLat=92.19082231860318)


def test_longitude_validation():
    with pytest.raises(ValueError):
        BoundingBox(minLong=24.644842122715147,
                    minLat=42.06253714023231,
                    maxLong=24.89038637385545,
                    maxLat=190.19082231860318)


def test_serialization():
    bbox = BoundingBox(minLong=24.644842122715147,
                       minLat=42.06253714023231,
                       maxLong=24.89038637385545,
                       maxLat=42.19082231860318)

    expected_result = "4124203033336938628"
    result = bbox.serialize()
    assert result == expected_result


def test_to_tuple():
    bbox = BoundingBox(minLong=24.644842122715147,
                       minLat=42.06253714023231,
                       maxLong=24.89038637385545,
                       maxLat=42.19082231860318)

    expected_result = (24.644842122715147, 42.06253714023231,
                       24.89038637385545, 42.19082231860318)
    result = bbox.to_tuple()
    assert result == expected_result
