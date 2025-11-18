# Backend - Centaura CMS

This is the Django backend for the Centaura CMS.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv myenv
# Windows:
myenv\Scripts\activate
# Linux/Mac:
source myenv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Seed initial content (optional):
```bash
python manage.py seed_homepage
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Start the development server:
```bash
python manage.py runserver localhost:8000
```

The backend will run on `http://localhost:8000`

## Access

- Django Admin: `http://localhost:8000/admin/`
- Dashboard: `http://localhost:8000/dashboard/`
- API: `http://localhost:8000/api/`

## Important Notes

- The backend must run on `localhost:8000` (not `127.0.0.1:8000`) for CORS and CSRF to work properly with the React frontend
- The login page is handled by React at `http://localhost:3000/dashboard/login`
- After login, users are redirected to the Django dashboard at `http://localhost:8000/dashboard/`

"# Jane_and_Aimun_Jawad_Backend" 

