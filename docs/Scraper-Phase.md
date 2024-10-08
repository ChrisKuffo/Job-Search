# Phase 2: Core Backend Functionality

## 1. Set up Supabase project
- Create a Supabase account at https://supabase.com (if not already done)
- Create a new project in Supabase dashboard
- Note down the project URL and API keys
- Update backend/.env file with Supabase project URL and API key

## 2. Set up Supabase tables and functions
- In Supabase dashboard, navigate to the SQL editor
- Create the following tables:
  ```sql
        CREATE TABLE public.users (
        id UUID REFERENCES auth.users NOT NULL PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE TABLE public.resumes (
        id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        user_id UUID REFERENCES public.users NOT NULL,
        content JSONB NOT NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE TABLE public.jobs (
        id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        description TEXT NOT NULL,
        location TEXT,
        salary_range TEXT,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );

        CREATE TABLE public.job_matches (
        id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
        user_id UUID REFERENCES public.users NOT NULL,
        job_id UUID REFERENCES public.jobs NOT NULL,
        resume_id UUID REFERENCES public.resumes NOT NULL,
        score FLOAT NOT NULL,
        created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
        );
        ```
- Set up Row Level Security (RLS) policies for each table:
    ```sql
        ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Users can only view and update their own data" ON public.users
        FOR ALL USING (auth.uid() = id);

        ALTER TABLE public.resumes ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Users can only access their own resumes" ON public.resumes
        FOR ALL USING (auth.uid() = user_id);

        ALTER TABLE public.jobs ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Jobs are viewable by everyone" ON public.jobs
        FOR SELECT USING (true);

        ALTER TABLE public.job_matches ENABLE ROW LEVEL SECURITY;
        CREATE POLICY "Users can only view their own job matches" ON public.job_matches
        FOR SELECT USING (auth.uid() = user_id);
        ``` 
3. Implement user authentication

In Supabase dashboard, navigate to Authentication settings
Configure authentication providers as needed (e.g., email/password, Google, GitHub)
In backend/app/core/:

Create auth.py for Supabase authentication integration
Implement functions for sign up, sign in, sign out, and token refresh


In backend/app/api/endpoints/:

Create auth.py for authentication-related API endpoints


In backend/app/core/:

Create middleware.py for authentication middleware
Implement a function to verify JWT tokens from Supabase


In backend/app/models/:

Create user.py for Pydantic models related to user data


In backend/app/services/:

Create user_service.py for user-related operations
Implement functions for user profile management (get, update, delete)


Update backend/app/main.py to include authentication middleware for protected routes

4. Set up Crawl4AI for multi-site job scraping
4.1 Install Crawl4AI and its dependencies

Add Crawl4AI to requirements.txt or pyproject.toml
Install Crawl4AI and its dependencies using pip or poetry
Verify installation by importing Crawl4AI in a Python shell

4.2 Configure Crawl4AI settings

Create a configuration file for Crawl4AI (e.g., crawl4ai_config.py)
Set up global settings like user agents, request delays, and timeout limits
Configure proxy settings if needed for avoiding IP bans

4.3 Create extraction strategies for each job board

Analyze the HTML structure of each job board (LinkedIn, Indeed, Glassdoor, ZipRecruiter, CareerBuilder)
Create a JsonCssExtractionStrategy for each job board in extraction_strategies.py
Define CSS selectors for job title, company, location, description, and other relevant fields
Implement any necessary data cleaning or formatting functions

4.4 Implement asynchronous scraping function

Create a new file async_scraper.py in the scrapers directory
Import AsyncWebCrawler from Crawl4AI
Implement an asynchronous function to scrape multiple job boards concurrently
Use asyncio.gather to run multiple scraping tasks in parallel

4.5 Create individual scraper modules for each job board

Create separate files for each job board (e.g., linkedin_scraper.py, indeed_scraper.py, etc.)
Implement a scraper class for each job board with methods for searching and extracting job details
Use the corresponding extraction strategy in each scraper class
Include methods for pagination or loading more results

4.6 Implement error handling and rate limiting

Create a custom exception class for scraping errors
Implement try-except blocks in scraper functions to catch and log errors
Use asyncio.Semaphore to limit the number of concurrent requests
Implement exponential backoff for retrying failed requests
Add delays between requests to respect robots.txt and avoid overloading servers

4.7 Integrate with Supabase for data storage

Create a Supabase table schema for storing job data
Implement functions to insert, update, and retrieve job data from Supabase
Create a data pipeline to process and store scraped job data in Supabase

4.8 Implement logging and monitoring

Set up logging to track scraping progress and errors
Implement basic metrics (e.g., jobs scraped per minute, success rate) for monitoring performance

4.9 Create unit tests for scrapers

Write unit tests for each scraper module
Create mock responses for testing to avoid hitting real websites during tests
Test error handling and edge cases

4.10 Integrate scrapers with the main application

Create API endpoints for triggering scraping jobs
Implement background tasks for running scrapers periodically
Update the job service to use the new scraping functionality

4.11 Perform integration testing

Test the entire scraping pipeline from API request to data storage
Verify that scraped data is correctly stored and retrievable from Supabase

4.12 Implement scraping job management

Create a system for managing and scheduling scraping jobs
Implement status tracking for ongoing and completed scraping tasks

4.13 Optimize and fine-tune

Monitor performance and optimize scraping strategies as needed
Adjust rate limiting and concurrency settings based on real-world performance

5. Develop resume parsing service

Install necessary libraries: python-docx, PyPDF2
In backend/app/services/:

Create resume_parser.py
Implement functions to parse PDF and DOCX files
Create functions to extract key information (contact details, education, experience, skills)


In backend/app/models/:

Create resume.py for Pydantic models related to resume data


In backend/app/api/endpoints/:

Create resumes.py for resume-related API endpoints (upload, get, update, delete)


In backend/app/services/:

Create resume_service.py for interactions with Supabase resumes table


Implement error handling and validation for resume parsing and storage

6. Create job scraping service

Install necessary libraries: beautifulsoup4, requests, aiohttp, langdetect, pandas
In backend/app/services/:

Create job_scraper.py
Implement separate classes/functions for each job board (LinkedIn, Indeed, Glassdoor)
Create a main scraping function that aggregates results from all sources


In backend/app/models/:

Create job.py for Pydantic models related to job data


In backend/app/services/:

Create job_service.py for interactions with Supabase jobs table


In backend/app/api/endpoints/:

Create jobs.py for job-related API endpoints (search, get, update)


Implement langdetect integration for automatic language detection of job postings
Create a data processing pipeline using pandas:

Clean and normalize scraped job data
Extract relevant features (e.g., required skills, experience level)


Implement error handling and rate limiting for web scraping

7. Develop basic job matching algorithm

In backend/app/services/:

Create job_matcher.py
Implement a keyword extraction function for resumes and job descriptions
Create a scoring function to match resumes against job descriptions
Implement a function to rank job matches for a given resume


In backend/app/models/:

Create job_match.py for Pydantic models related to job match data


In backend/app/services/:

Create job_match_service.py for interactions with Supabase job_matches table


In backend/app/api/endpoints/:

Create job_matches.py for job matching API endpoints


Use pandas for data analysis and feature extraction in the matching process
Implement caching for match results to improve performance

8. Set up asynchronous task processing

Evaluate asynchronous processing options:

Option 1: Supabase Edge Functions

In Supabase dashboard, navigate to Edge Functions
Create new edge functions for heavy computing tasks (e.g., job scraping, matching)
Deploy edge functions


Option 2: Celery

Set up Celery with Redis as message broker
Create Celery tasks for time-consuming operations


Option 3: Native Python async

Implement asyncio for concurrent operations




Choose and implement the most suitable option based on project requirements
In backend/app/core/:

Create tasks.py to define asynchronous tasks


Update relevant services to use asynchronous processing

9. Implement caching strategy

Evaluate caching options:

Option 1: Redis

Set up Redis server
Implement Redis caching in relevant services


Option 2: Supabase caching

In Supabase dashboard, review and configure caching settings
Utilize Supabase's built-in caching mechanisms in API calls


Option 3: Application-level caching

Implement in-memory caching using a library like cachetools




Choose and implement the most suitable option based on project requirements
In backend/app/core/:

Create cache.py to manage caching operations


Update relevant services to use caching for frequently accessed data

10. Integrate all components

Ensure all services are properly connected and working together
Implement comprehensive error handling and logging throughout the backend
Create integration tests to verify the functionality of all components together

11. Optimize and refine

Conduct performance testing on all major backend operations
Identify and optimize any bottlenecks in data processing or API responses
Refine job matching algorithm based on initial results
Ensure all Supabase interactions are efficient and follow best practices
In Supabase dashboard, monitor database performance and optimize if necessary

12. Documentation and code review

Update API documentation with all new endpoints
Review and update inline code documentation
Conduct a thorough code review of all new components
Update README.md with any new setup or running instructions for backend services
Document Supabase schema and any custom functions in project documentation

This reformatted version uses consistent markdown formatting, proper indentation, and clear section headers to improve readability and structure. The main sections are now clearly distinguished, and subsections are properly nested.

Is this formatting more to your liking? Would you like me to make any further adjustments?