# Backend Practice Project

## Step-by-Step Implementation Plan

---

## 1. Project Goal

Implement a **simple Library Backend REST API** to practice:

* Docker containerization
* CI/CD pipelines
* Cloud deployment
* Working with Cursor (agent-based / vibe coding)

The focus is **learning core concepts**, not building a production-grade system.

---

## 2. Tech Stack

* **Backend:** Django + Django REST Framework
* **Database:** PostgreSQL
* **Containerization:** Docker, Docker Compose
* **CI/CD:** GitHub Actions
* **Cloud:** Oracle Cloud VM (Free Tier, Ubuntu)

---

## 3. High-Level Architecture

```
Client
  ↓
Django REST API (Docker container)
  ↓
PostgreSQL (Docker container)
```

* Two containers: `api` and `db`
* Managed locally with Docker Compose
* Deployed to Oracle Cloud VM using Docker Compose

---

## 4. Functional Requirements

### 4.1 Models

#### Author

* `id`
* `name` (string, required)
* `created_at`

#### Book

* `id`
* `title` (string, required)
* `author` (ForeignKey → Author)
* `published_year` (integer, optional)
* `created_at`

---

### 4.2 API Endpoints

Use Django REST Framework `ModelViewSet`.

| Method | Endpoint        | Description   |
| ------ | --------------- | ------------- |
| GET    | `/api/authors/` | List authors  |
| POST   | `/api/authors/` | Create author |
| GET    | `/api/books/`   | List books    |
| POST   | `/api/books/`   | Create book   |

* No authentication required
* JSON input/output only

---

## 5. Repository Structure

```
library-api/
├── app/
│   ├── library/
│   ├── api/
│   ├── manage.py
│   ├── requirements.txt
│   └── tests/
├── docker/
│   ├── Dockerfile
│   └── entrypoint.sh
├── docker-compose.yml
├── .env.example
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## 6. Step-by-Step Implementation Tasks

### STEP 1 – Initialize Django Project

1. Create a Django project named `library`
2. Create a Django app named `api`
3. Install dependencies:

   * `django`
   * `djangorestframework`
   * `psycopg2-binary`
4. Add `rest_framework` and `api` to `INSTALLED_APPS`

---

### STEP 2 – Implement Models

1. Create `Author` and `Book` models
2. Add `__str__` methods
3. Create and apply migrations

---

### STEP 3 – Create API Layer

1. Create serializers for `Author` and `Book`
2. Create `ModelViewSet` classes
3. Register routes using DRF `DefaultRouter`
4. Expose API under `/api/`

---

### STEP 4 – Add Automated Tests

1. Use Django `TestCase`
2. Write tests for:

   * Creating an Author
   * Creating a Book
   * Listing Authors
   * Listing Books
3. Ensure all tests pass with:

```
python manage.py test
```

---

### STEP 5 – Dockerize the Application

#### Dockerfile

* Use Python slim image
* Install dependencies
* Copy project files
* Run migrations on startup
* Start server on `0.0.0.0:8000`

#### Docker Compose

##### `db` service

* Image: `postgres:15`
* Environment variables:

  * `POSTGRES_DB`
  * `POSTGRES_USER`
  * `POSTGRES_PASSWORD`
* Volume for persistent data

##### `api` service

* Built from Dockerfile
* Depends on `db`
* Loads environment variables from `.env`
* Exposes port `8000`

---

### STEP 6 – Environment Configuration

Create the following files:

* `.env.example`
* `.env` (ignored by Git)

Example variables:

```
DEBUG=1
SECRET_KEY=change-me
DB_NAME=library
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

---

### STEP 7 – CI with GitHub Actions

Create `.github/workflows/ci.yml`.

Pipeline requirements:

1. Trigger on `push` and `pull_request`
2. Set up Python
3. Start PostgreSQL service
4. Install dependencies
5. Run migrations
6. Run tests

The pipeline **must fail** if tests fail.

---

### STEP 8 – Production Readiness

1. Add production settings flag
2. Disable `DEBUG` in production
3. Use environment variables only
4. Update `README.md` with deployment steps

---

### STEP 9 – Oracle Cloud Deployment (Manual)

Document these steps clearly:

1. Create Oracle Cloud Ubuntu VM (Free Tier)
2. Install Docker and Docker Compose
3. Clone repository
4. Create `.env` file
5. Run:

```
docker compose up -d
```

6. Open port `8000` in Oracle Cloud security rules

---

## 7. Quality Guidelines

* Keep code simple and readable
* Prefer clarity over cleverness
* Use meaningful commit messages
* Avoid premature optimization

---

## 8. Definition of Done

* API works locally using Docker
* Tests pass locally and in CI
* App runs successfully on Oracle Cloud VM
* README clearly explains setup and deployment

---

## 9. Optional Improvements (After Completion)

* Pagination
* Filtering
* OpenAPI / Swagger docs
* CI-based deployment
* Nginx reverse proxy

---

## End of Document
