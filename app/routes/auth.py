from fastapi import APIRouter, Form, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
import sqlite3

from app.models import get_db


router = APIRouter()


BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)


# =========================
# LOGIN PAGE
# =========================

@router.get("/login")
async def login_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


# =========================
# REGISTER PAGE
# =========================

@router.get("/register")
async def register_page(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )


# =========================
# REGISTER
# =========================

@router.post("/register")
async def register(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):

    connection = get_db()

    try:

        connection.execute(
            """
            INSERT INTO users (name, email, password)
            VALUES (?, ?, ?)
            """,
            (name, email, password)
        )

        connection.commit()

        return {
            "message": "Registration successful",
            "name": name,
            "email": email
        }

    except sqlite3.IntegrityError:

        return {
            "message": "Email already registered"
        }

    finally:

        connection.close()


# =========================
# LOGIN
# =========================

@router.post("/login")
async def login(
    email: str = Form(...),
    password: str = Form(...)
):

    connection = get_db()

    user = connection.execute(
        """
        SELECT * FROM users
        WHERE email = ? AND password = ?
        """,
        (email, password)
    ).fetchone()

    connection.close()

    if user:

        return {
            "message": "Login successful",
            "name": user["name"],
            "email": user["email"]
        }

    return {
        "message": "Invalid email or password"
    }


# =========================
# LOGOUT
# =========================

@router.get("/logout")
async def logout():

    return {
        "message": "Logout successful"
    }


# =========================
# SESSION INFO
# =========================

@router.get("/session-info")
async def session_info():

    return {
        "logged_in": False,
        "user": None
    }