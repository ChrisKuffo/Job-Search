# Job Search Automation

An AI-powered job search application that leverages web scraping to assist users in finding suitable job opportunities.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is a comprehensive job search application that combines AI analysis, web scraping, and a user-friendly interface to streamline the job hunting process. It leverages modern technologies and artificial intelligence to provide users with personalized job recommendations and insights.

## Key Features

- **Resume Analysis**: AI-powered analysis of uploaded resumes with feedback and suggestions.
- **Job Search Query Generation**: AI-generated optimized job search queries based on resume analysis.
- **Multi-Platform Job Scraping**: Automated scraping of job postings from various platforms including LinkedIn.
- **Enhanced Job Matching**: Advanced algorithms for analyzing job descriptions against user resumes with detailed match scores.
- **User-Friendly Interface**: Modern, responsive design for easy interaction across devices.
- **Real-time Data Streaming**: Live streaming of job listing data to the frontend for immediate user access.
- **AI-Powered Information Extraction**: Utilization of GPT-4 for advanced text processing and analysis of job descriptions.
- **HTML to Markdown Conversion**: Improved readability of job descriptions and other textual content.
- **Comprehensive Error Handling**: Robust error management and request rate limiting for stable performance.
- **User Authentication System**: Secure login and personalized user experiences.
- **AI-Powered Interview Preparation**: Module to help users prepare for interviews based on job descriptions and resume analysis.
- **Performance Optimization**: Implementation of caching mechanisms for improved application speed and responsiveness.

## Technologies Used

### Frontend

- Next.js 14
- TypeScript
- React Query
- Tailwind CSS
- React Hook Form
- Axios
- Framer Motion
- shadcn/ui

### Backend

- Python 3.9+
- FastAPI
- Supabase
- BeautifulSoup4
- spaCy
- Uvicorn
- OpenAI API
- LangChain
- Celery
- Redis
- AIOHTTP
- pandas
- langdetect

### Development Tools

- Poetry
- Git
- ESLint & Prettier
- Jest & React Testing Library
- MyPy
- Cypress
- GitHub Actions
- pre-commit hooks
- concurrently

## Project Structure

The project follows a structured layout. For detailed information about the project structure, please refer to the [PROJECT-STRUCTURE.md](PROJECT-STRUCTURE.md) file.

## Getting Started

Detailed setup instructions will be provided in a separate document.

## Development

- Use Poetry for managing Python package dependencies.
- Follow the Python Style Guide (PEP 8) for backend development.
- Use ESLint and Prettier for frontend code formatting.
- Write unit tests for new features.
- Update documentation as necessary.
- Utilize pre-commit hooks for automated code checks before commits.
- Use concurrently to run multiple commands simultaneously during development.

## Testing

- Backend: Use pytest for unit testing
- Frontend: Use Jest and React Testing Library for component and unit testing
- End-to-End: Use Cypress for comprehensive end-to-end testing
- Continuous Integration: Leverage GitHub Actions for automated testing on every push or pull request

## Deployment

(Deployment instructions will be added in future updates)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.