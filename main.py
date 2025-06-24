import random
import asyncio
from datetime import datetime
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

CONFIG_FILE = "config.json"
LOG_FILE = "logs.txt"

# Load config
import json
with open(CONFIG_FILE, encoding="utf-8") as f:
    config = json.load(f)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_overlay(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "countdown_target": config["target_time"],
        "log_color": config["log_color"],
        "countdown_color": config["countdown_color"],
        "log_font": config["log_font"],
        "log_size": config["log_size"],
        "countdown_font": config["countdown_font"],
        "countdown_size": config["countdown_size"]
    })

@app.get("/logs")
async def get_log():
    with open(LOG_FILE, encoding="utf-8") as f:
        lines = f.readlines()
    return {"line": random.choice(lines).strip()}
