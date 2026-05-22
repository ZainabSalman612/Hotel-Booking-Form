# ============================================
# database.py - Database Connection & Queries
# ============================================
# This module handles all database operations
# including connection management, table creation,
# and booking data insertion.
# ============================================

import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the database connection string from environment
DATABASE_URL = os.getenv("DATABASE_URL")


# ============================================
# Function: Get Database Connection
# ============================================
def get_connection():
    """
    Establish and return a connection to the PostgreSQL database.

    Uses the DATABASE_URL environment variable for the connection string.
    Format: postgresql://username:password@host:port/database_name

    Returns:
        psycopg2.connection: A PostgreSQL database connection object.

    Raises:
        Exception: If DATABASE_URL is missing or the connection fails.
    """
    if not DATABASE_URL:
        raise ValueError(
            "[ERROR] DATABASE_URL is not set. "
            "Please check your .env file."
        )
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"[ERROR] Failed to connect to database: {e}")
        raise


# ============================================
# Function: Create Bookings Table
# ============================================
def create_table():
    """
    Create the 'bookings' table if it doesn't already exist.

    This function is called on application startup to ensure
    the required database schema is in place.

    Table columns:
        - id: Auto-incrementing primary key
        - full_name: Guest's full name (max 100 chars)
        - email: Guest's email address (max 100 chars)
        - phone: Guest's phone number (max 20 chars)
        - check_in: Check-in date
        - check_out: Check-out date
        - room_type: Type of room booked (max 50 chars)
        - guests: Number of guests (default 1)
        - special_requests: Any special requests (unlimited text)
        - created_at: Timestamp of when the booking was created
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # SQL query to create the bookings table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bookings (
                id SERIAL PRIMARY KEY,
                full_name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL,
                check_in DATE NOT NULL,
                check_out DATE NOT NULL,
                room_type VARCHAR(50) NOT NULL,
                guests INTEGER NOT NULL DEFAULT 1,
                special_requests TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Commit the changes to the database
        conn.commit()
        print("[INFO] Bookings table is ready.")

    except Exception as e:
        print(f"[ERROR] Failed to create table: {e}")

    finally:
        # Always close the connection to avoid resource leaks
        if conn:
            conn.close()


# ============================================
# Function: Insert a New Booking
# ============================================
def insert_booking(full_name, email, phone, check_in,
                   check_out, room_type, guests, special_requests):
    """
    Insert a new booking record into the 'bookings' table.

    Uses parameterized queries (%s placeholders) to prevent
    SQL injection attacks.

    Args:
        full_name (str): Guest's full name
        email (str): Guest's email address
        phone (str): Guest's phone number
        check_in (str): Check-in date (YYYY-MM-DD format)
        check_out (str): Check-out date (YYYY-MM-DD format)
        room_type (str): Type of room (Standard, Deluxe, Suite, Presidential)
        guests (int): Number of guests
        special_requests (str): Any special requests or notes

    Raises:
        Exception: If the insertion fails.
    """
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Parameterized INSERT query to prevent SQL injection
        query = """
            INSERT INTO bookings
                (full_name, email, phone, check_in,
                 check_out, room_type, guests, special_requests)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s);
        """

        # Execute the query with the provided values
        cursor.execute(query, (
            full_name,
            email,
            phone,
            check_in,
            check_out,
            room_type,
            guests,
            special_requests
        ))

        # Commit the transaction to save the booking
        conn.commit()
        print(f"[INFO] Booking for '{full_name}' saved successfully.")

    except Exception as e:
        print(f"[ERROR] Failed to insert booking: {e}")
        raise

    finally:
        # Always close the connection to avoid resource leaks
        if conn:
            conn.close()
