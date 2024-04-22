from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Input projects into the portfolio website
class Project(BaseModel):
    title: str
    description: str

project_items = []

# Endpoint to get all projects
@app.get('/projects')
async def get_projects():
    return project_items

# Endpoint to add a new project
@app.post('/projects')
async def add_projects(project: Project):
    project_items.append(project)
    return project
    
@app.get("/projects/{title}")
async def get_project(title: str):
    for project in project_items:
        if project.title == title:
            return project
    raise HTTPException(status_code=404, detail="Project not found")
