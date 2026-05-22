# ============================================
# main.py - FastAPI Hotel Booking Application
# ============================================
# This is the main entry point of the hotel
# booking web application. It handles routing,
# form processing, and template rendering.
# ============================================

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from database import insert_booking, create_table
from typing import Optional

# Load environment variables from .env file
load_dotenv()

# ============================================
# Initialize FastAPI Application
# ============================================
app = FastAPI(
    title="Hotel Booking System",
    description="A full-stack hotel booking web application",
    version="1.0.0"
)

# Mount static files directory (CSS, images, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 template engine
templates = Jinja2Templates(directory="templates")

# ============================================
# Create database table on startup
# ============================================
@app.on_event("startup")
async def startup_event():
    """Create the bookings table if it doesn't exist when the app starts."""
    create_table()


# ============================================
# Route: Home Page (GET /)
# ============================================
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Render the hotel booking form page.
    
    Returns:
        HTMLResponse: The index.html template with the booking form.
    """
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "success": False}
    )


# ============================================
# Route: Process Booking (POST /book)
# ============================================
@app.post("/book", response_class=HTMLResponse)
async def book(
    request: Request,
    full_name: str = Form(...),          # Guest's full name (required)
    email: str = Form(...),              # Guest's email address (required)
    phone: str = Form(...),              # Guest's phone number (required)
    check_in: str = Form(...),           # Check-in date (required)
    check_out: str = Form(...),          # Check-out date (required)
    room_type: str = Form(...),          # Type of room selected (required)
    guests: int = Form(...),             # Number of guests (required)
    special_requests: Optional[str] = Form(None)  # Special requests (optional)
):
    """
    Process the hotel booking form submission.
    
    Receives form data, validates it, stores it in the
    PostgreSQL database, and returns a success message.
    
    Args:
        full_name: Guest's full name
        email: Guest's email address
        phone: Guest's phone number
        check_in: Check-in date (YYYY-MM-DD)
        check_out: Check-out date (YYYY-MM-DD)
        room_type: Selected room type
        guests: Number of guests
        special_requests: Any special requests or notes
    
    Returns:
        HTMLResponse: The index.html template with success message.
    """
    # Insert booking data into the database
    insert_booking(
        full_name=full_name,
        email=email,
        phone=phone,
        check_in=check_in,
        check_out=check_out,
        room_type=room_type,
        guests=guests,
        special_requests=special_requests or ""
    )

    # Render the template with a success message
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "success": True}
    )


# ============================================
# Run the application with Uvicorn
# ============================================
if __name__ == "__main__":
    import uvicorn
    # Start the server on localhost:8000 with auto-reload
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
