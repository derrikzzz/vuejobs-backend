from typing import List
from fastapi import APIRouter, HTTPException
from app.schemas.job import Job, JobCreate, JobUpdate

router = APIRouter()

# Sample data for testing
sample_jobs = [
    {
        "id": 1,
        "title": "Frontend Developer",
        "company": "Tech Corp",
        "description": "Build amazing user interfaces with Vue.js",
        "location": "San Francisco, CA",
        "salary": "$80,000 - $120,000",
        "job_type": "Full-time",
        "remote": True,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    },
    {
        "id": 2,
        "title": "Backend Engineer",
        "company": "StartupXYZ",
        "description": "Build scalable APIs with Python and FastAPI",
        "location": "New York, NY",
        "salary": "$90,000 - $140,000",
        "job_type": "Full-time", 
        "remote": False,
        "created_at": "2024-01-02T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    },
    {
        "id": 3,
        "title": "Data Analyst",
        "company": "DataCorp",
        "description": "Analyze data to help businesses make decisions",
        "location": "Chicago, IL",
        "salary": "$70,000 - $110,000",
        "job_type": "Full-time",
        "remote": True,
        "created_at": "2024-01-03T00:00:00Z",
        "updated_at": "2024-01-03T00:00:00Z"
    },
    {
        "id": 4,
        "title": "Software Engineer",
        "company": "TechCorp",
        "description": "Build scalable software solutions with Python and Django",
        "location": "San Francisco, CA",
        "salary": "$100,000 - $150,000",
        "job_type": "Full-time",
        "remote": True,
        "created_at": "2024-01-04T00:00:00Z",
        "updated_at": "2024-01-04T00:00:00Z"
    },
    {
        "id": 5,
        "title": "Product Manager",
        "company": "ProductCorp",
        "description": "Manage product development and ensure successful delivery",
        "location": "New York, NY",
        "salary": "$120,000 - $180,000",
        "job_type": "Full-time",
        "remote": False,
        "created_at": "2024-01-05T00:00:00Z",
        "updated_at": "2024-01-05T00:00:00Z"
    },
    {
        "id": 6,
        "title": "UX Designer",
        "company": "DesignCorp",
        "description": "Create intuitive user experiences with Figma and Adobe XD",
        "location": "San Francisco, CA",
        "salary": "$80,000 - $120,000",
        "job_type": "Full-time",
        "remote": True,
        "created_at": "2024-01-06T00:00:00Z",
        "updated_at": "2024-01-06T00:00:00Z"
    }

]


@router.get("/", response_model=List[Job])
async def get_jobs():
    """Get all jobs"""
    return sample_jobs

@router.get("/{job_id}", response_model=Job)
async def get_job(job_id: int):
    """Get a specific job by ID"""
    job = next((job for job in sample_jobs if job["id"] == job_id), None)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/", response_model=Job)
async def create_job(job: JobCreate):
    """Create a new job"""
    new_job = {
        "id": len(sample_jobs) + 1,
        **job.dict(),
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-01T00:00:00Z"
    }
    sample_jobs.append(new_job)
    return new_job

@router.put("/{job_id}", response_model=Job)
async def update_job(job_id: int, job_update: JobUpdate):
    """Update a job"""
    job = next((job for job in sample_jobs if job["id"] == job_id), None)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    for field, value in job_update.dict(exclude_unset=True).items():
        job[field] = value
    job["updated_at"] = "2024-01-01T00:00:00Z"
    
    return job

@router.delete("/{job_id}")
async def delete_job(job_id: int):
    """Delete a job"""
    job_index = next((i for i, job in enumerate(sample_jobs) if job["id"] == job_id), None)
    if job_index is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    sample_jobs.pop(job_index)
    return {"message": "Job deleted successfully"}