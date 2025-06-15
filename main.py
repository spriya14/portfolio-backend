from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a Prometheus counter
THEME_TOGGLE_COUNTER = Counter("theme_toggle_clicks_total", "Total number of theme toggle clicks")

@app.post("/log-theme-toggle")
async def log_theme_toggle():
    THEME_TOGGLE_COUNTER.inc()
    print("Theme toggle clicked")
    return JSONResponse(content={"status": "ok",THEME_TOGGLE_COUNTER:THEME_TOGGLE_COUNTER._value.get()}, status_code=200)

@app.get("/")
def read_root():
    return {"message": "Hey there! I am running FastAPI with Prometheus metrics."}

@app.get("/metrics")
def metrics():
    return  200, {"Content-Type":THEME_TOGGLE_COUNTER._value.get()}