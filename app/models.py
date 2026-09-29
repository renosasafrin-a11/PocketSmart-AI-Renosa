import sqlite3
from pathlib import Path

from pydantic import BaseModel, Field
from typing import Optional, List


# =========================
# DATABASE
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "pocketsmart.db"


def get_db():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_users_table():

    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# =========================
# PYDANTIC MODELS
# =========================

class User(BaseModel):
    name: str
    email: str
    password: str


class LoginRequest(BaseModel):
    email: str
    password: str


class HomePlannerRequest(BaseModel):
    budget: float = Field(gt=0)
    room_type: str
    style: str
    requirements: Optional[str] = None


class PartyPlannerRequest(BaseModel):
    budget: float = Field(gt=0)
    event_type: str
    guests: int = Field(gt=0)
    theme: Optional[str] = None


class JewelryPlannerRequest(BaseModel):
    budget: float = Field(gt=0)
    occasion: str
    jewelry_type: str
    outfit_description: Optional[str] = None


class Recommendation(BaseModel):
    name: str
    category: str
    price: float
    platform: str
    reason: str
    link: Optional[str] = None


class RecommendationResponse(BaseModel):
    title: str
    budget: float
    recommendations: List[Recommendation] = []
    total_estimated_cost: float = 0