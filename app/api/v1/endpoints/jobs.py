from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.job import Job as JobModel
from app.schemas.job import Job, JobCreate, JobUpdate

router = APIRouter()



@router.get("/", response_model=List[Job])
async def get_jobs(db: Session = Depends(get_db)):
    """Get all jobs"""
    jobs = db.query(JobModel).filter(JobModel.is_active == True).all()
    return jobs

@router.get("/{job_id}", response_model=Job)
async def get_job(job_id: int, db: Session = Depends(get_db)):
    """Get a specific job by ID"""
    job = db.query(JobModel).filter(JobModel.id == job_id, JobModel.is_active == True).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/", response_model=Job)
async def create_job(job: JobCreate, db: Session = Depends(get_db)):
    """Create a new job"""
    db_job = JobModel(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

@router.put("/{job_id}", response_model=Job)
async def update_job(job_id: int, job_update: JobUpdate, db: Session = Depends(get_db)):
    """Update a job"""
    job = db.query(JobModel).filter(JobModel.id == job_id, JobModel.is_active == True).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    for field, value in job_update.dict(exclude_unset=True).items():
        setattr(job, field, value)
    
    db.commit()
    db.refresh(job)
    return job

@router.delete("/{job_id}")
async def delete_job(job_id: int, db: Session = Depends(get_db)):
    """Delete a job"""
    job = db.query(JobModel).filter(JobModel.id == job_id, JobModel.is_active == True).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    
    job.is_active = False
    db.commit()
    return {"message": "Job deleted successfully"}