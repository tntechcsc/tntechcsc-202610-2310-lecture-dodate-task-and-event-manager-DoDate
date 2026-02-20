# application_controller.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel, conint
from typing import Optional

from data_manager import Data_Manager
from planner import Planner

app = FastAPI()

FRONTEND_DIR = Path("Front_End")
INDEX_PATH = FRONTEND_DIR / "index.html"
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

DATA_PATH = Path("./Data/planner.json")
data_manager = Data_Manager(str(DATA_PATH))
planner: Planner = data_manager.open_planner()

def save():
    data_manager.save_planner(planner)

def category_exists(cat_name: str) -> bool:
    cat_name = (cat_name or "").strip()
    for c in planner.get_categories():
        if (c.get_category_name() or "") == cat_name:
            return True
    return False

@app.get("/")
def serve_index():
    try:
        if not INDEX_PATH.exists():
            raise HTTPException(status_code=404, detail="Front_End/index.html not found")
        return FileResponse(str(INDEX_PATH))
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/categories")
def get_categories():
    try:
        return [c.to_dict() for c in planner.get_categories()]
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/tasks")
def get_tasks():
    try:
        return [t.to_dict() for t in planner.get_tasks()]
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

class NewTask(BaseModel):
    task_name: str
    category_name: str
    description: Optional[str] = ""
    due_date: Optional[str] = None
    weight: conint(ge=1, le=5) = 3
    todays_focus: bool = False

@app.post("/tasks")
def create_task(payload: NewTask):
    try:
        if not category_exists(payload.category_name):
            raise HTTPException(status_code=400, detail="Category does not exist")

        planner.create_task(
            name=payload.task_name,
            todays_focus=payload.todays_focus,
            desc=payload.description or "",
            due_date=payload.due_date,
            status="incomplete",
            weight=int(payload.weight),
            category_name=payload.category_name
        )
        save()
        return planner.get_tasks()[-1].to_dict()
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.patch("/tasks/{task_index}/status")
def patch_task_status(task_index: int):
    try:
        planner.set_task_status(task_index)
        save()
        return planner.get_tasks()[task_index].to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.patch("/tasks/{task_index}/focus")
def patch_task_focus(task_index: int):
    try:
        planner.set_task_todays_focus(task_index)
        save()
        return planner.get_tasks()[task_index].to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("application_controller:app", host="127.0.0.1", port=8000, reload=True)
