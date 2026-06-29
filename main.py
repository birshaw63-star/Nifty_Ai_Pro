from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Nifty AI Pro</title>
    </head>
    <body style="background:#111;color:white;text-align:center;font-family:Arial;padding-top:80px;">
        <h1>🚀 Nifty AI Pro</h1>
        <h2>Project Started Successfully</h2>
    </body>
    </html>
    """
