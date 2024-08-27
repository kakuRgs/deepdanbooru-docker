import io
import os
from fastapi import FastAPI, File, Query
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from deepdanbooru_onnx import DeepDanbooru
from PIL import Image

app = FastAPI(title="deepdanbooru-docker")
app.add_middleware(CORSMiddleware, allow_origins=["*"])
default_threshold = float("0.1")
deepdanbooru = DeepDanbooru(threshold=default_threshold)

class Result(BaseModel):
    tag: str
    score: float

@app.get("/", include_in_schema=False)
async def route_index():
    return RedirectResponse("/docs")

@app.post("/deepdanbooru", summary="Extract Danbooru tags from an image.")
async def route_deepdanbooru(
    image: bytes = File(),
    threshold: float = Query(default=default_threshold, description="Threshold for filtering tags.")
) -> list[Result]:
    results = deepdanbooru(Image.open(io.BytesIO(image)))
    # Apply the threshold dynamically
    filtered_results = [
        Result(tag=tag, score=score.item()) 
        for tag, score in results.items() if score.item() >= threshold
    ]
    filtered_results.sort(key=lambda result: result.score, reverse=True)
    return filtered_results
