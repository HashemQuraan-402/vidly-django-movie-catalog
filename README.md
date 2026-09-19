# Vidly — Django Movie Catalog

Vidly is a lightweight movie-catalog web application built with Django. It demonstrates server-side rendering, relational data modeling, Django administration, and a REST-style movie resource.

## Features

- Browse all movies in a responsive table.
- View the details of an individual movie.
- Store movie title, release year, stock quantity, daily rate, genre, and creation date.
- Organize movies by genre using a relational database model.
- Manage movies and genres through the Django admin site.
- Access movie data through a Tastypie API resource.
- Configure sensitive settings through environment variables.
- Serve static files with WhiteNoise.

## Tech Stack

- Python
- Django 5.2.7
- SQLite
- Django Tastypie
- HTML and Django Templates
- Bootstrap 5
- Gunicorn
- WhiteNoise

## Project Structure

```text
vidly-django-movie-catalog/
├── api/                    # Tastypie movie API resource
├── movies/                 # Movie models, views, routes, and templates
│   ├── migrations/         # Database schema migrations
│   └── templates/movies/   # Movie list and detail pages
├── templates/              # Shared base template
├── vidly/                  # Project settings, root routes, and home page
├── .env.example            # Required environment-variable names
├── manage.py               # Django command-line utility
├── requirements.txt        # Python dependencies
└── Procfile                # Gunicorn process declaration
```

## Data Model

The application contains two related entities:

- `Genre`: stores the genre name.
- `Movie`: stores the title, release year, number in stock, daily rate, creation date, and a foreign-key relationship to `Genre`.

Deleting a genre also deletes its related movies because the relationship uses Django's `CASCADE` behavior.

## Getting Started

### Prerequisites

- Python 3.13 recommended by the included `Pipfile`
- Git

### 1. Clone the repository

```bash
git clone https://github.com/HashemQuraan-402/vidly-django-movie-catalog.git
cd vidly-django-movie-catalog
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the environment variables

The required variable names are documented in `.env.example`. The application reads them from the operating-system environment; it does not load the `.env` file automatically.

For Windows PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = (python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
$env:DJANGO_DEBUG = "True"
$env:DJANGO_ALLOWED_HOSTS = "localhost,127.0.0.1"
```

For macOS or Linux:

```bash
export DJANGO_SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
export DJANGO_DEBUG="True"
export DJANGO_ALLOWED_HOSTS="localhost,127.0.0.1"
```

Never commit a real secret key or a local `.env` file.

### 5. Create the local database

```bash
python manage.py migrate
```

### 6. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to choose a username, email address, and password.

### 7. Run the application

```bash
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser.

### 8. Collect static files for deployment

For a production build, generate the static output locally or in the hosting platform's build step:

```bash
python manage.py collectstatic --noinput
```

The generated root `static/` directory is ignored by Git and should not be committed. Django and WhiteNoise regenerate it from the installed applications during deployment.

## Application Routes

| Route | Purpose |
| --- | --- |
| `/` | Application home page |
| `/movies/` | Movie catalog |
| `/movies/<id>` | Details for a specific movie |
| `/admin/` | Django administration site |
| `/api/movies/` | Movie API collection |
| `/api/movies/<id>/` | Movie API detail resource |

## Adding Sample Data

1. Start the development server.
2. Open <http://127.0.0.1:8000/admin/>.
3. Sign in with the superuser account.
4. Add one or more genres.
5. Add movies and assign each movie to a genre.
6. Open <http://127.0.0.1:8000/movies/> to view the catalog.

The SQLite database is created locally and is intentionally excluded from Git, so every developer begins with a clean database.

## Validation

Run Django's configuration checks:

```bash
python manage.py check
```

Run the test command:

```bash
python manage.py test
```

## Configuration and Security

- `DJANGO_SECRET_KEY` is required and must be kept private.
- `DJANGO_DEBUG` defaults to `False` when it is not supplied.
- `DJANGO_ALLOWED_HOSTS` accepts a comma-separated list of hosts.
- `db.sqlite3` and local environment files are ignored by Git.
- Production secrets should be configured through the hosting provider, never committed to the repository.

## Future Improvements

- Add search, filtering, and pagination.
- Add user authentication and authorization for the API.
- Add create, update, and delete screens outside the admin site.
- Add model, view, and API test coverage.
- Add API documentation and validation.
- Use PostgreSQL for production deployment.
- Add screenshots and a hosted demonstration.

## Author

**Hashem Quraan**

- GitHub: [HashemQuraan-402](https://github.com/HashemQuraan-402)
- LinkedIn: [hashem-quraan-b561453ab](https://www.linkedin.com/in/hashem-quraan-b561453ab)
