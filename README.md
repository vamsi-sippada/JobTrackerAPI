# JobTracker API

A REST API built with Django and Django REST Framework for tracking job applications. Features JWT authentication, per-user data isolation, and application statistics.

## Tech Stack

- **Backend:** Python, Django, Django REST Framework
- **Authentication:** JWT (SimpleJWT)
- **Database:** SQLite
- **Deployment:** Railway *(coming soon)*

## Features

- User registration and login with JWT authentication
- Create, read, update, delete job applications
- Filter jobs by status (applied, interview, rejected, offer)
- Search jobs by company name or role
- Dashboard stats — count of applications per status
- Token refresh and secure logout with blacklisting
- Per-user data isolation — users only see their own data

## Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. Clone the repository
```bash
   git clone https://github.com/vamsi-sippada/JobTrackerAPI.git
   cd JobTrackerAPI
```

2. Create and activate virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # Mac/Linux
```

3. Install dependencies
```bash
   pip install -r requirements.txt
```

4. Create a `.env` file in the project root
SECRET_KEY=your-secret-key-here
DEBUG=True

5. Run migrations
```bash
   python manage.py migrate
```

6. Start the server
```bash
   python manage.py runserver
```

## API Endpoints

### Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Create a new account |
| POST | `/api/auth/login/` | Login and get JWT tokens |
| POST | `/api/auth/token/refresh/` | Refresh access token |
| POST | `/api/auth/logout/` | Logout and blacklist token |

### Jobs

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/jobs/` | List all your jobs |
| POST | `/api/jobs/` | Add a new job application |
| GET | `/api/jobs/<id>/` | Get a single job |
| PUT | `/api/jobs/<id>/` | Update a job |
| DELETE | `/api/jobs/<id>/` | Delete a job |
| GET | `/api/jobs/stats/` | Get application counts by status |

### Query Parameters

Filter and search jobs:
GET /api/jobs/?status=applied
GET /api/jobs/?search=google
GET /api/jobs/?status=interview&search=developer

## Sample Requests

### Register
```json
POST /api/auth/register/
{
    "email": "user@example.com",
    "password": "yourpassword",
    "username": "yourname"
}
```

### Add a Job
```json
POST /api/jobs/
Authorization: Bearer <access_token>

{
    "company_name": "Google",
    "role": "Python Developer",
    "status": "applied",
    "applied_date": "2026-05-01",
    "deadline": "2026-05-30",
    "notes": "Applied via LinkedIn"
}
```

### Stats Response
```json
GET /api/jobs/stats/
Authorization: Bearer <access_token>

{
    "total": 10,
    "applied": 5,
    "interview": 3,
    "rejected": 1,
    "offer": 1
}
```

## Project Structure
JobTrackerAPI/
├── accounts/          # User auth app
│   ├── models.py      # Custom User model
│   ├── views.py       # Register, Logout views
│   └── urls.py        # Auth endpoints
├── jobs/              # Jobs app
│   ├── models.py      # Job model
│   ├── serializers.py # JobSerializer
│   ├── views.py       # CRUD + Stats views
│   └── urls.py        # Job endpoints
├── jobtracker/        # Project config
│   ├── settings.py
│   └── urls.py
├── requirements.txt
└── .env               # Not committed - see setup