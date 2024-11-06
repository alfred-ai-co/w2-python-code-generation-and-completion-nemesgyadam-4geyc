from sqlalchemy.orm import Session
from app.db_models.base import Project, Ticket


# CRUD operations for Project
def create_project(db: Session, name: str, description: str):
    new_project = Project(name=name, description=description)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project
