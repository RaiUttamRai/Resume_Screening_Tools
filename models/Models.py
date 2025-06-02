from sqlalchemy import Column, Integer, String, Enum,ForeignKey,DateTime,Float
from database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
import enum

class RoleEnum(enum.Enum):
    admin = "admin"
    recruiter = "recruiter"
    candidate = "candidate"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False)

class JobDescription(Base):
    __tablename__ = "job_descriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    recruiter = relationship("User", back_populates="jobs")
    match_score = relationship("ResumeMatchScore", back_populates="job")

class Resume(Base):
    __tablename__ = "resumes"
    id=Column(Integer,primary_key=True,index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    original_filename= Column(String)
    parsed_text = Column(String)
    uploaded_at = Column(String)

    candidate = relationship("User", back_populates="resumes")
    match_score= relationship("ResumeMatchScore", back_populates="resume")

class ResumeMatchScore(Base):
    __tablename__ = "resume_match_scores"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("job_descriptions.id"))
    resume_id = Column(Integer, ForeignKey("resumes.id"))
    score = Column(Float)
    ranked_at = Column(DateTime, default=datetime.utcnow)
    job = relationship("JobDescription", back_populates="match_score")
    resume = relationship("Resume", back_populates="match_score")

