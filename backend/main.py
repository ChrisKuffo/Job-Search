from fastapi import FastAPI, HTTPException
from app.core.supabase_client import supabase
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Job(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Welcome to the Job Search Automation API"}

@app.get("/test-supabase")
async def test_supabase():
    try:
        response = supabase.table('jobs').select("*").limit(5).execute()
        return {"message": "Supabase connection successful", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Supabase connection failed: {str(e)}")

@app.post("/jobs")
async def create_job(job: Job):
    try:
        response = supabase.table('jobs').insert(job.dict()).execute()
        return {"message": "Job created successfully", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create job: {str(e)}")

@app.get("/jobs")
async def get_jobs():
    try:
        response = supabase.table('jobs').select("*").execute()
        return {"message": "Jobs retrieved successfully", "data": response.data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve jobs: {str(e)}")

@app.get("/jobs/{job_id}")
async def get_job(job_id: str):
    try:
        response = supabase.table('jobs').select("*").eq("id", job_id).execute()
        if len(response.data) == 0:
            raise HTTPException(status_code=404, detail="Job not found")
        return {"message": "Job retrieved successfully", "data": response.data[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve job: {str(e)}")

@app.put("/jobs/{job_id}")
async def update_job(job_id: str, job: Job):
    try:
        response = supabase.table('jobs').update(job.dict()).eq("id", job_id).execute()
        if len(response.data) == 0:
            raise HTTPException(status_code=404, detail="Job not found")
        return {"message": "Job updated successfully", "data": response.data[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update job: {str(e)}")