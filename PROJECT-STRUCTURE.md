# Job Search Automation Project Structure

## Directory Structure

├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── api/
│   │   │   ├── (auth)/
│   │   │   │   ├── login/
│   │   │   │   │   ├── page.tsx
│   │   │   │   │   └── layout.tsx
│   │   │   │   ├── register/
│   │   │   │   │   ├── page.tsx
│   │   │   │   │   └── layout.tsx
│   │   │   │   └── layout.tsx
│   │   │   ├── dashboard/
│   │   │   │   ├── page.tsx
│   │   │   │   └── layout.tsx
│   │   │   ├── jobs/
│   │   │   │   ├── [id]/
│   │   │   │   │   └── page.tsx
│   │   │   │   ├── page.tsx
│   │   │   │   └── layout.tsx
│   │   │   ├── layout.tsx
│   │   │   └── page.tsx
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── lib/
│   │   ├── styles/
│   │   ├── types/
│   │   └── utils/
│   ├── public/
│   ├── tests/
│   ├── .env
│   ├── .eslintrc.js
│   ├── next.config.mjs
│   ├── package.json
│   ├── tailwind.config.ts
│   └── tsconfig.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── jobs.py
│   │   │   │   ├── resumes.py
│   │   │   │   └── matches.py
│   │   │   └── deps.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── job.py
│   │   │   ├── resume.py
│   │   │   └── user.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── job_service.py
│   │   │   ├── resume_service.py
│   │   │   └── matching_service.py
│   │   ├── utils/
│   │   │   ├── __init__.py
│   │   │   └── helpers.py
│   │   ├── scrapers/
│   │   │   ├── __init__.py
│   │   │   ├── linkedin_scraper.py
│   │   │   ├── indeed_scraper.py
│   │   │   ├── glassdoor_scraper.py
│   │   │   ├── ziprecruiter_scraper.py
│   │   │   └── careerbuilder_scraper.py
│   │   ├── crawl4ai_config/
│   │   │   ├── __init__.py
│   │   │   └── extraction_strategies.py
│   │   └── main.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_api/
│   │   ├── test_services/
│   │   └── test_scrapers/
│   ├── .env
│   ├── pyproject.toml
│   └── requirements.txt
│
├── supabase/
│   ├── migrations/
│   ├── functions/
│   ├── seed.sql
│   └── config.toml
│
├── scripts/
│   ├── setup.sh
│   ├── dev.sh
│   └── deploy.sh
│
├── docs/
│   ├── api/
│   ├── development/
│   └── user/
│
├── .github/
│   └── workflows/
│
├── .gitignore
├── docker-compose.yml
├── README.md
└── package.json

## Directory and File Descriptions

### Frontend (Next.js 18)

- `frontend/`: Contains all frontend-related code and configuration.
  - `src/`: Source directory for Next.js 18 application.
    - `app/`: Next.js 18 app directory (using App Router).
      - `api/`: API routes for Next.js.
      - `(auth)/`: Grouped authentication routes.
        - `login/`: Login page and its layout.
        - `register/`: Registration page and its layout.
        - `layout.tsx`: Shared layout for auth pages.
      - `dashboard/`: Dashboard page and its layout.
      - `jobs/`: Job-related pages and layouts.
        - `[id]/`: Dynamic route for individual job pages.
      - `layout.tsx`: Root layout component for the app.
      - `page.tsx`: Root page component.
    - `components/`: Reusable React components.
    - `hooks/`: Custom React hooks.
    - `lib/`: Utility functions and libraries.
    - `styles/`: Global styles and Tailwind CSS configuration.
    - `types/`: TypeScript type definitions.
    - `utils/`: Utility functions specific to the frontend.
  - `public/`: Static assets.
  - `tests/`: Frontend tests (unit and integration).
  - `.env`: Environment variables for the frontend.
  - `.eslintrc.js`: ESLint configuration.
  - `next.config.mjs`: Next.js configuration file (using ES modules).
  - `package.json`: Frontend dependencies and scripts.
  - `tailwind.config.ts`: Tailwind CSS configuration (in TypeScript).
  - `tsconfig.json`: TypeScript configuration.

### Backend (Python 3.11)

- `backend/`: Contains all backend-related code and configuration.
  - `app/`: Main application directory.
    - `api/`: API-related code.
      - `endpoints/`: Individual API route handlers.
      - `deps.py`: Dependency injection configurations.
    - `core/`: Core application components.
      - `config.py`: Application configuration management.
      - `security.py`: Authentication and authorization logic.
    - `models/`: Pydantic models for data validation and serialization.
    - `services/`: Business logic and services that interact with Supabase.
    - `utils/`: Utility functions for the backend.
    - `main.py`: FastAPI application entry point.
  - `tests/`: Backend tests.
  - `.env`: Environment variables for the backend.
  - `pyproject.toml`: Poetry configuration and dependencies (specifying Python 3.11).
  - `requirements.txt`: Python dependencies for non-Poetry environments.

### Supabase

- `supabase/`: Supabase-specific configuration and migrations.
  - `migrations/`: SQL migration files for Supabase.
  - `functions/`: Supabase Edge Functions (if used).
  - `seed.sql`: Initial data seeding for the database.
  - `config.toml`: Supabase configuration file.

### Scripts

- `scripts/`: Utility scripts for development and deployment.
  - `setup.sh`: Project setup script.
  - `dev.sh`: Local development startup script.
  - `deploy.sh`: Deployment script.

### Documentation

- `docs/`: Project documentation.
  - `api/`: API documentation.
  - `development/`: Development guides and standards.
  - `user/`: User guides and manuals.

### CI/CD and Configuration

- `.github/workflows/`: GitHub Actions CI/CD configurations.
- `.gitignore`: Git ignore file.
- `docker-compose.yml`: Docker Compose configuration for local development.
- `README.md`: Project overview and setup instructions.
- `package.json`: Root-level npm scripts and dependencies.

## Root package.json

The root `package.json` file includes scripts for running concurrent processes:

```json
{
  "name": "job-search-automation",
  "version": "1.0.0",
  "scripts": {
    "dev": "concurrently \"npm run dev:frontend\" \"npm run dev:backend\"",
    "dev:frontend": "cd frontend && npm run dev",
    "dev:backend": "cd backend && poetry run uvicorn app.main:app --reload",
    "install": "concurrently \"npm run install:frontend\" \"npm run install:backend\"",
    "install:frontend": "cd frontend && npm install",
    "install:backend": "cd backend && poetry install",
    "build": "concurrently \"npm run build:frontend\" \"npm run build:backend\"",
    "build:frontend": "cd frontend && npm run build",
    "build:backend": "cd backend && poetry build",
    "test": "concurrently \"npm run test:frontend\" \"npm run test:backend\"",
    "test:frontend": "cd frontend && npm test",
    "test:backend": "cd backend && poetry run pytest"
  },
  "devDependencies": {
    "concurrently": "^8.0.1"
  }
}
```
## scripts/dev.sh

The `scripts/dev.sh` file uses concurrently to start both frontend and backend:

```bash
#!/bin/bash
# This script uses concurrently to start both frontend and backend

npm run dev
```

## Rationale for Structure

- Next.js 18 App Router: Follows Next.js 18 conventions with the App Router and src directory.
- Nested Layouts: Includes layout.tsx files at various levels for flexible page layouts.
- Route Groups: Uses route groups (e.g., (auth)) to organize related pages.
- Dynamic Routes: Includes examples of dynamic routes (e.g., jobs/[id]).
- Python 3.11: Backend structure optimized for Python 3.11 and FastAPI.
- Supabase Integration: Dedicated directory for Supabase configurations and migrations.
- Scalability: Structure allows for easy addition of new features and components.
- Testing: Dedicated test directories for comprehensive coverage.
- Documentation: Centralized documentation for easy access and maintenance.
- CI/CD Integration: Facilitates easy setup of CI/CD pipelines.
- Environment Management: Separate .env files for frontend and backend.
- Dependency Management: Uses Poetry for backend and npm for frontend.
- Concurrent Development: Utilizes concurrently for simultaneous frontend and backend development.
- Unified Scripts: Root-level package.json provides a central point for common tasks.

This structure provides a solid foundation for the Job Search Automation project, accommodating all required technologies, allowing for efficient Supabase integration, and supporting future growth and maintainability.