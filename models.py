# ============================================
# models.py - Pydantic Data Models
# ============================================
# This module defines data models used for
# validating and structuring booking data.
# Pydantic ensures type safety and provides
# automatic validation of incoming data.
# ============================================

from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date


# ============================================
# Model: Booking
# ============================================
class Booking(BaseModel):
    """
    Pydantic model representing a hotel booking.

    This model validates the booking data structure and types.
    It can be used for API request/response validation.

    Attributes:
        full_name (str): The guest's full name.
        email (str): The guest's email address.
        phone (str): The guest's phone number.
        check_in (date): The check-in date.
        check_out (date): The check-out date.
        room_type (str): The type of room booked.
        guests (int): The number of guests staying.
        special_requests (Optional[str]): Any special requests or notes.

    Example:
        >>> booking = Booking(
        ...     full_name="John Doe",
        ...     email="john@example.com",
        ...     phone="+1234567890",
        ...     check_in="2026-06-01",
        ...     check_out="2026-06-05",
        ...     room_type="Deluxe",
        ...     guests=2,
        ...     special_requests="Late check-in"
        ... )
    """

    full_name: str               # Guest's full name
    email: str                   # Guest's email address
    phone: str                   # Guest's phone number
    check_in: date               # Check-in date (YYYY-MM-DD)
    check_out: date              # Check-out date (YYYY-MM-DD)
    room_type: str               # Room type (Standard, Deluxe, Suite, Presidential)
    guests: int                  # Number of guests (1-10)
    special_requests: Optional[str] = None  # Optional special requests

    # --- Field Validators ---

    @field_validator("guests")
    @classmethod
    def guests_must_be_positive(cls, v):
        """Ensure the guest count is between 1 and 10."""
        if v < 1 or v > 10:
            raise ValueError("Number of guests must be between 1 and 10.")
        return v

    @field_validator("room_type")
    @classmethod
    def room_type_must_be_valid(cls, v):
        """Ensure the room type is one of the allowed options."""
        allowed = ["Standard", "Deluxe", "Suite", "Presidential Suite"]
        if v not in allowed:
            raise ValueError(
                f"Room type must be one of: {', '.join(allowed)}"
            )
        return v

    class Config:
        """Pydantic model configuration."""
        # Example schema for auto-generated API docs
        json_schema_extra = {
            "example": {
                "full_name": "Jane Smith",
                "email": "jane@example.com",
                "phone": "+1987654321",
                "check_in": "2026-07-15",
                "check_out": "2026-07-20",
                "room_type": "Suite",
                "guests": 3,
                "special_requests": "Ocean view preferred"
            }
        }
