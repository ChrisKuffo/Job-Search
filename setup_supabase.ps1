# setup_supabase.ps1

# Navigate to the backend directory
Set-Location -Path .\backend

# Install Supabase dependency using Poetry
poetry add supabase

# Create config.py file
$configContent = @"
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    SUPABASE_SERVICE_ROLE_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
"@

New-Item -Path .\app\core\config.py -Value $configContent -Force

# Create supabase_client.py file
$clientContent = @"
from supabase import create_client, Client
from app.core.config import settings

supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
"@

New-Item -Path .\app\core\supabase_client.py -Value $clientContent -Force

# Update main.py file
$mainContent = @"
from fastapi import FastAPI
from app.core.supabase_client import supabase

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Job Search Automation API"}

@app.get("/test-supabase")
async def test_supabase():
    try:
        response = supabase.table('jobs').select("*").execute()
        return {"message": "Supabase connection successful", "data": response.data}
    except Exception as e:
        return {"message": "Supabase connection failed", "error": str(e)}
"@

Set-Content -Path .\app\main.py -Value $mainContent

Write-Host "Supabase setup completed. Please ensure your .env file contains the necessary Supabase credentials."