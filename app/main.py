from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.routes import auth, planner
from app.models import create_users_table


app = FastAPI(
    title="PocketSmart AI",
    description="Your Smart Budget & Recommendation Assistant",
    version="1.0.0"
)


# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# =========================
# DIRECTORIES
# =========================

BASE_DIR = Path(__file__).resolve().parent

STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"


# =========================
# STATIC FILES
# =========================

if STATIC_DIR.exists():

    app.mount(
        "/static",
        StaticFiles(directory=STATIC_DIR),
        name="static"
    )


# =========================
# TEMPLATES
# =========================

templates = Jinja2Templates(
    directory=TEMPLATES_DIR
)


# =========================
# DATABASE
# =========================

create_users_table()


# =========================
# ROUTES
# =========================

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)


app.include_router(
    planner.router,
    prefix="/planner",
    tags=["Planner"]
)


# =========================
# HOME
# =========================

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
async def health_check():

    return {
        "status": "healthy"
    }