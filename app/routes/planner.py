from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path

from app.services.recommendation import (
    create_home_prompt,
    fallback_home_recommendations,
    create_party_prompt,
    fallback_party_recommendations,
    create_jewelry_prompt,
    fallback_jewelry_recommendations
)

from app.services.gemini import generate_recommendation


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# =========================
# HOME PLANNER
# =========================

@router.get("/home")
async def home_planner(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="home.html"
    )


@router.post("/generate-home")
async def generate_home(
    budget: float = Form(...),
    room_type: str = Form(...),
    style: str = Form(...),
    requirements: str = Form("")
):

    prompt = create_home_prompt(
        budget=budget,
        room_type=room_type,
        style=style,
        requirements=requirements
    )

    result = await generate_recommendation(prompt)

    if result.startswith("Gemini API error"):

        result = {
            "source": "Fallback Recommendation",
            "recommendations":
                fallback_home_recommendations(
                    budget=budget,
                    room_type=room_type,
                    style=style
                )
        }

    return {
        "message": "Home recommendations generated",
        "result": result
    }


# =========================
# PARTY PLANNER
# =========================

@router.get("/party")
async def party_planner(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="party.html"
    )


@router.post("/generate-party")
async def generate_party(
    budget: float = Form(...),
    event_type: str = Form(...),
    guests: int = Form(...),
    theme: str = Form("")
):

    prompt = create_party_prompt(
        budget=budget,
        event_type=event_type,
        guests=guests,
        theme=theme
    )

    result = await generate_recommendation(prompt)

    if result.startswith("Gemini API error"):

        result = {
            "source": "Fallback Recommendation",
            "recommendations":
                fallback_party_recommendations(
                    budget=budget,
                    event_type=event_type,
                    guests=guests,
                    theme=theme
                )
        }

    return {
        "message": "Party recommendations generated",
        "result": result
    }


# =========================
# JEWELRY PLANNER
# =========================

@router.get("/jewelry")
async def jewelry_planner(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="jewelry.html"
    )


@router.post("/generate-jewelry")
async def generate_jewelry(
    budget: float = Form(...),
    occasion: str = Form(...),
    jewelry_type: str = Form(...),
    outfit_description: str = Form("")
):

    prompt = create_jewelry_prompt(
        budget=budget,
        occasion=occasion,
        jewelry_type=jewelry_type,
        outfit_description=outfit_description
    )

    result = await generate_recommendation(prompt)

    if isinstance(result, str) and result.startswith("Gemini API error"):

        result = {
            "source": "Fallback Recommendation",
            "recommendations":
                fallback_jewelry_recommendations(
                    budget=budget,
                    occasion=occasion,
                    jewelry_type=jewelry_type
                )
        }

    return {
        "message": "Jewelry recommendations generated",
        "result": result
    }