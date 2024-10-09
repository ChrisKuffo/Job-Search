from fastapi import FastAPI, Depends
from app.core.config import Settings, get_settings
from supabase import create_client, Client

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Job Search Automation API"}

@app.get("/test-supabase")
async def test_supabase(settings: Settings = Depends(get_settings)):
    supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_ANON_KEY)
    try:
        response = supabase.table('jobs').select("*").limit(1).execute()
        return {"message": "Supabase connection successful", "data": response.data}
    except Exception as e:
        return {"message": "Supabase connection failed", "error": str(e)}
