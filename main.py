from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from datetime import datetime, timezone
from api.market import get_market_data
from api.signal import get_signal

app = FastAPI(
    title="Nifty AI Pro",
    version="1.0.0"
)

# Static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())


@app.get("/market")
def market():
    data = get_market_data()
    data["last_update"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    return data


@app.get("/signal")
def signal():
    return get_signal()
