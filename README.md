# 🏨 Hotel Booking System

A full-stack hotel booking web application built with **FastAPI**, **HTML/CSS**, and **PostgreSQL**. This project features a stunning glassmorphic booking form with animated backgrounds, smooth micro-interactions, and seamless database integration.

---

## ✨ Features

- 🎨 **Premium Glassmorphic UI** — Frosted glass card on animated gradient background
- ⚡ **FastAPI Backend** — High-performance Python web framework
- 🗃️ **PostgreSQL Database** — Reliable relational data storage
- 📝 **Form Validation** — Client-side HTML5 validation + server-side handling
- 🎭 **Jinja2 Templates** — Dynamic HTML rendering with conditional messages
- 🌐 **Vercel Ready** — Pre-configured for cloud deployment
- 📱 **Mobile Friendly** — Fully responsive design (desktop → tablet → phone)
- ♿ **Accessible** — Reduced motion support & semantic HTML
- 🎆 **Micro-Animations** — Floating orbs, shimmer effects, hover transitions

---

## 🛠️ Tech Stack

| Technology        | Purpose                 |
| ----------------- | ----------------------- |
| **FastAPI**       | Backend web framework   |
| **HTML/CSS**      | Frontend interface      |
| **Jinja2**        | Template engine         |
| **PostgreSQL**    | Database                |
| **psycopg2**      | PostgreSQL connector    |
| **python-dotenv** | Environment variables   |
| **Uvicorn**       | ASGI server             |
| **Pydantic**      | Data validation         |
| **Vercel**        | Cloud deployment        |

---

## 📁 Project Structure

```
Hotel-Booking-Form/
│
├── main.py                 # FastAPI application (routes & logic)
├── database.py             # Database connection & queries
├── models.py               # Pydantic data models
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation (this file)
├── .gitignore              # Git ignore rules
├── .env                    # Environment variables (not committed)
├── vercel.json             # Vercel deployment config
│
├── sql/
│   └── create_table.sql    # SQL schema for bookings table
│
├── templates/
│   └── index.html          # Booking form HTML template
│
└── static/
    └── style.css           # Stylesheet with premium design
```

---

## 🚀 Getting Started

### Prerequisites

Before you begin, make sure you have:

- **Python 3.9+** installed → [Download Python](https://www.python.org/downloads/)
- **PostgreSQL** installed and running → [Download PostgreSQL](https://www.postgresql.org/download/)
- **Git** installed → [Download Git](https://git-scm.com/)

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Hotel-Booking-Form.git
cd Hotel-Booking-Form
```

---

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (macOS/Linux)
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. PostgreSQL Database Setup

#### Step 1: Open PostgreSQL and create a database

```sql
CREATE DATABASE hotel_booking_db;
```

#### Step 2: Run the table creation script

```bash
psql -U postgres -d hotel_booking_db -f sql/create_table.sql
```

Or open `sql/create_table.sql` in **pgAdmin** and execute it manually.

#### Step 3: Update the `.env` file

Open the `.env` file and replace the placeholder with your actual connection string:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/hotel_booking_db
```

---

### 5. Run the Application Locally

```bash
uvicorn main:app --reload
```

Or simply run:

```bash
python main.py
```

🎉 Open your browser and visit: **http://localhost:8000**

---

## 📤 Push to GitHub

Follow these steps to push your project to GitHub:

```bash
# Step 1: Initialize git (if not already done)
git init

# Step 2: Add all files
git add .

# Step 3: Create initial commit
git commit -m "Initial commit: Hotel Booking System"

# Step 4: Add your GitHub repository as remote
git remote add origin https://github.com/your-username/Hotel-Booking-Form.git

# Step 5: Push to GitHub
git branch -M main
git push -u origin main
```

---

## 🌐 Deploy to Vercel

### Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

### Step 2: Login to Vercel

```bash
vercel login
```

### Step 3: Deploy

```bash
# From the project root directory
vercel
```

### Step 4: Set Environment Variables

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project
3. Navigate to **Settings** → **Environment Variables**
4. Add the following variable:

| Name           | Value                                                   |
| -------------- | ------------------------------------------------------- |
| `DATABASE_URL` | `postgresql://user:password@host:5432/hotel_booking_db` |

> 💡 **Tip:** Use a cloud PostgreSQL provider for production:
> - [Neon](https://neon.tech) — Serverless Postgres (free tier available)
> - [Supabase](https://supabase.com) — Open source Firebase alternative
> - [Railway](https://railway.app) — One-click Postgres deployment

### Step 5: Deploy to Production

```bash
vercel --prod
```

---

## 🔧 API Endpoints

| Method | Endpoint | Description                   |
| ------ | -------- | ----------------------------- |
| `GET`  | `/`      | Render the hotel booking form |
| `POST` | `/book`  | Process and store a booking   |
| `GET`  | `/docs`  | FastAPI auto-generated docs   |

---

## 📸 Screenshots

> Add screenshots of your running application here.

| Booking Form   | Success Message |
| -------------- | --------------- |
| *(screenshot)* | *(screenshot)*  |

---

## 📝 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

---

<p align="center">
  Made with ❤️ using <strong>FastAPI</strong> &amp; <strong>PostgreSQL</strong>
</p>
