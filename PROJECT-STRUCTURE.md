# Job Search Automation Project Structure

## Directory Structure

```
├── frontend/
│   ├── .next/
│   ├── app/
│   │   ├── api/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── lib/
│   │   ├── pages/
│   │   ├── styles/
│   │   ├── types/
│   │   └── utils/
│   ├── public/
│   ├── tests/
│   ├── .env
│   ├── .eslintrc.js
│   ├── next.config.js
│   ├── package.json
│   ├── tailwind.config.js
│   └── tsconfig.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── endpoints/
│   │   │   └── deps.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   └── security.py
│   │   ├── models/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── tests/
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
```

## Directory and File Descriptions

### Frontend

- `frontend/`: Contains all frontend-related code and configuration.
  - `app/`: Next.js 14 app directory.
    - `api/`: API routes for Next.js.
    - `components/`: Reusable React components.
    - `hooks/`: Custom React hooks.
    - `lib/`: Utility functions and libraries.
    - `pages/`: Page components and routing.
    - `styles/`: Global styles and Tailwind CSS configuration.
    - `types/`: TypeScript type definitions.
    - `utils/`: Utility functions specific to the frontend.
  - `public/`: Static assets.
  - `tests/`: Frontend tests (unit and integration).
  - `.env`: Environment variables for the frontend.
  - `.eslintrc.js`: ESLint configuration.
  - `next.config.js`: Next.js configuration file.
  - `package.json`: Frontend dependencies and scripts.
  - `tailwind.config.js`: Tailwind CSS configuration.
  - `tsconfig.json`: TypeScript configuration.

### Backend

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
  - `pyproject.toml`: Poetry configuration and dependencies.
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
    "concurrently": "^6.2.1"
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

1. **Separation of Concerns**: Clear division between frontend, backend, and Supabase configurations.
2. **Next.js App Router**: Follows Next.js 14 conventions with the App Router.
3. **FastAPI Best Practices**: Adheres to FastAPI best practices while accommodating Supabase integration.
4. **Supabase Integration**: Dedicated directory for Supabase configurations and migrations, separate from application code.
5. **Scalability**: Structure allows for easy addition of new features and components.
6. **Testing**: Dedicated test directories for comprehensive coverage.
7. **Documentation**: Centralized documentation for easy access and maintenance.
8. **CI/CD Integration**: Facilitates easy setup of CI/CD pipelines.
9. **Environment Management**: Separate `.env` files for frontend and backend.
10. **Dependency Management**: Uses Poetry for backend and npm for frontend.
11. **Concurrent Development**: Utilizes concurrently for simultaneous frontend and backend development.
12. **Unified Scripts**: Root-level package.json provides a central point for common tasks.
13. **Backend Optimization**: Revised backend structure removes redundant elements typically handled by Supabase.
14. **Service-Oriented Backend**: Includes a services directory for business logic, promoting clean separation from API handlers.

This structure provides a solid foundation for the Job Search Automation project, accommodating all required technologies, allowing for efficient Supabase integration, and supporting future growth and maintainability.