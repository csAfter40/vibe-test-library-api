# Library API

A simple Library Backend REST API built with Django REST Framework, PostgreSQL, and Docker.

## Features

- RESTful API for managing Authors and Books
- PostgreSQL database
- Dockerized for easy deployment
- CI/CD with GitHub Actions
- Production-ready configuration

## API Endpoints

- `GET /api/authors/` - List all authors
- `POST /api/authors/` - Create a new author
- `GET /api/books/` - List all books
- `POST /api/books/` - Create a new book

## Local Development

### Prerequisites

- Python 3.12+
- Docker and Docker Compose
- (Optional) uv package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd vibe-deploy
```

2. Create a `.env` file (copy from `.env.example`):
```bash
cp .env.example .env
```

3. Edit `.env` with your configuration (optional for local development)

4. Start the services with Docker Compose:
```bash
docker compose up
```

The API will be available at `http://localhost:8000`

### Running Tests

To run tests locally:

```bash
cd app
uv run python manage.py test
```

Or using Docker:

```bash
docker compose exec api python manage.py test
```

## Production Deployment

### Environment Variables

Set the following environment variables in production:

- `PRODUCTION=true` - Enable production mode (disables DEBUG)
- `DEBUG=0` - Disable debug mode
- `SECRET_KEY` - Django secret key (use a strong, random key)
- `ALLOWED_HOSTS` - Comma-separated list of allowed hostnames
- `DB_NAME` - PostgreSQL database name
- `DB_USER` - PostgreSQL username
- `DB_PASSWORD` - PostgreSQL password
- `DB_HOST` - PostgreSQL host (use `db` in Docker Compose)
- `DB_PORT` - PostgreSQL port (default: 5432)

### Oracle Cloud VM Deployment

1. Create an Oracle Cloud Ubuntu VM (Free Tier)
2. Install Docker and Docker Compose:
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Log out and back in for group changes to take effect
```

3. Clone the repository:
```bash
git clone <repository-url>
cd vibe-deploy
```

4. Create `.env` file with production settings:
```bash
nano .env
```

Set:
```
PRODUCTION=true
DEBUG=0
SECRET_KEY=<generate-a-strong-secret-key>
ALLOWED_HOSTS=<your-vm-ip-or-domain>
DB_NAME=library
DB_USER=postgres
DB_PASSWORD=<strong-password>
DB_HOST=db
DB_PORT=5432
```

5. Start the services:
```bash
docker compose up -d
```

6. Open port 8000 in Oracle Cloud security rules:
   - Go to Oracle Cloud Console
   - Navigate to Networking > Security Lists
   - Add an Ingress Rule for port 8000 (TCP)

7. Access the API at `http://<your-vm-ip>:8000`

### Checking Logs

```bash
docker compose logs -f api
```

### Stopping Services

```bash
docker compose down
```

To also remove volumes (database data):
```bash
docker compose down -v
```

## Project Structure

```
vibe-deploy/
├── app/                 # Django application
│   ├── api/            # API app
│   ├── library/        # Django project settings
│   ├── manage.py
│   └── requirements.txt
├── docker/
│   ├── Dockerfile
│   └── entrypoint.sh
├── docker-compose.yml
├── .env.example
└── README.md
```

## Technology Stack

- **Backend**: Django 5.2 + Django REST Framework
- **Database**: PostgreSQL 15
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions
- **Python**: 3.12
