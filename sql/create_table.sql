-- ============================================
-- Hotel Booking System - Database Schema
-- ============================================
-- This script creates the 'bookings' table.
-- Run this in your PostgreSQL database before
-- starting the application (or let FastAPI
-- auto-create it on startup).
--
-- Usage:
--   psql -U postgres -d hotel_booking_db -f sql/create_table.sql
-- ============================================

CREATE TABLE IF NOT EXISTS bookings (
    id                SERIAL PRIMARY KEY,          -- Auto-incrementing unique ID
    full_name         VARCHAR(100) NOT NULL,        -- Guest's full name
    email             VARCHAR(100) NOT NULL,        -- Guest's email address
    phone             VARCHAR(20)  NOT NULL,        -- Guest's phone number
    check_in          DATE         NOT NULL,        -- Check-in date
    check_out         DATE         NOT NULL,        -- Check-out date
    room_type         VARCHAR(50)  NOT NULL,        -- Room type (Standard, Deluxe, Suite, Presidential)
    guests            INTEGER      NOT NULL DEFAULT 1,  -- Number of guests
    special_requests  TEXT,                         -- Any special requests (optional)
    created_at        TIMESTAMP    DEFAULT CURRENT_TIMESTAMP  -- When the booking was made
);

-- ============================================
-- Verify table creation (optional)
-- ============================================
-- SELECT * FROM bookings;
