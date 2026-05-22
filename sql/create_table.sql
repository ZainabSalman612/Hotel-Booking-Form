-- ============================================
-- Hotel Booking System - Database Schema
-- ============================================
-- This script creates the 'bookings' table
-- Run this in your PostgreSQL database before
-- starting the application.
-- ============================================

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
