from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Nifty AI Pro")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(file.read())
