from pydantic import BaseModel, validator


class BoundingBox(BaseModel):
    """Geo bounding box resource. Follows the specification at:
    https://wiki.openstreetmap.org/wiki/Bounding_Box

    Attributes:
        minLong: Minimum longitude
        minLat: Minimum latitude
        maxLong: Maximum longitude
        maxLat: Maximum latitude
    """
    minLong: float
    minLat: float
    maxLong: float
    maxLat: float

    @validator("minLong", "maxLong")
    def longitude_must_be_valid(cls, v):
        if v < -180 or v > 180:
            raise ValueError("Longitude must be between -180 and 180")
        return v

    @validator("minLat", "maxLat")
    def latitude_must_be_valid(cls, v):
        if v < -90 or v > 90:
            raise ValueError("Latitude must be between -90 and 90")
        return v

    def serialize(self) -> str:
        """
        Serialize bounding box to string.
        """
        hashed = str(hash(self.minLong) + hash(self.minLat) +
                     hash(self.maxLong) + hash(self.maxLat))
        return hashed

    def to_tuple(self) -> tuple:
        return self.minLong, self.minLat, self.maxLong, self.maxLat
