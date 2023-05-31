import os

from fastapi import FastAPI, HTTPException, File, UploadFile, Depends
from fastapi.responses import FileResponse

from src import config
from src.request_items import BoundingBox
from src.tasks import get_image
from src.utils import get_predominant_rgb_colour_in_image, rgb_to_colour_name


app = FastAPI()


@app.post("/fetch_image")
async def fetch_image(bbox: BoundingBox):
    try:
        file = await get_image(bbox, config.download_path)
        return FileResponse(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/custom_image_upload", status_code=201)
def custom_image_upload(bbox: BoundingBox = Depends(),
                        file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1]
    if extension == "png":
        raise HTTPException(status_code=400,
                            detail="PNG files not supported.")
    try:
        contents = file.file.read()
        filename = bbox.serialize() + f".{extension}"
        with open(os.path.join(config.download_path, filename), "wb") as f:
            f.write(contents)
    except Exception as e:
        return {"error": f"Error uploading file: {str(e)}"}
    finally:
        file.file.close()
    return {"success": "Successfully uploaded file."}


@app.post("/get_image_colour")
async def get_image_colour(bbox: BoundingBox):
    try:
        file = await get_image(bbox, config.download_path)
        rgb = get_predominant_rgb_colour_in_image(file)
        colour_name = rgb_to_colour_name(rgb)
        return {"colour": colour_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
