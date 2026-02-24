# application_controller.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel, conint
from typing import Optional
from datetime import date

from data_manager import Data_Manager
from planner import Planner

app = FastAPI()

# Stable paths
HERE = Path(__file__).resolve().parent
FRONTEND_DIR = HERE / "Front_End"
INDEX_PATH = FRONTEND_DIR / "index.html"
DATA_PATH = HERE / "Data" / "planner.json"

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

data_manager = Data_Manager(str(DATA_PATH))
planner: Planner = data_manager.open_planner()

def save() -> None:
    data_manager.save_planner(planner)

def category_exists(cat_name: str) -> bool:
    target = (cat_name or "").strip()
    for c in planner.get_categories():
        if (c.get_category_name() or "").strip() == target:
            return True
    return False

def _today_str() -> str:
    return date.today().isoformat()

# -------------------------
# Payload models
# -------------------------
class NewTask(BaseModel):
    task_name: str
    category_name: str
    description: Optional[str] = ""
    due_date: Optional[str] = None
    weight: conint(ge=1, le=5) = 3
    todays_focus: bool = False

# -------------------------
# Static/index
# -------------------------
@app.get("/")
def serve_index():
    if not INDEX_PATH.exists():
        raise HTTPException(status_code=404, detail="Front_End/index.html not found")
    return FileResponse(str(INDEX_PATH))

# -------------------------
# Planner (handy for frontend)
# -------------------------
@app.get("/planner")
def get_planner():
    return planner.to_dict()

# -------------------------
# Dashboard endpoints (NOT in this iteration)
# -------------------------
@app.get("/dashboard/stats")
def dashboard_stats(today: Optional[str] = None):
    raise HTTPException(status_code=501, detail="Dashboard stats not implemented in this iteration")

@app.get("/tasks/overdue")
def get_overdue_tasks(today: Optional[str] = None):
    raise HTTPException(status_code=501, detail="Overdue tasks not implemented in this iteration")

@app.get("/tasks/due_soon")
def get_due_soon_tasks(today: Optional[str] = None):
    raise HTTPException(status_code=501, detail="Due-soon tasks not implemented in this iteration")

# -------------------------
# Categories (read-only in this iteration)
# -------------------------
@app.get("/categories")
def get_categories():
    return [c.to_dict() for c in planner.get_categories()]

@app.post("/categories")
def create_category():
    raise HTTPException(status_code=501, detail="Category create not implemented in this iteration")

@app.patch("/categories/{cat_index}")
def edit_category(cat_index: int):
    raise HTTPException(status_code=501, detail="Category edit not implemented in this iteration")

@app.delete("/categories/{cat_index}")
def delete_category(cat_index: int):
    raise HTTPException(status_code=501, detail="Category delete not implemented in this iteration")

# -------------------------
# Tasks
# -------------------------
@app.get("/tasks")
def get_tasks():
    return [t.to_dict() for t in planner.get_tasks()]

@app.get("/tasks/by_status/{status}")
def get_tasks_by_status(status: str):
    s = (status or "").strip().lower()
    return [t.to_dict() for t in planner.get_tasks() if (t.get_status() or "").strip().lower() == s]

@app.post("/tasks")
def create_task(payload: NewTask):
    if not category_exists(payload.category_name):
        raise HTTPException(status_code=400, detail="Category does not exist")

    planner.create_task(
        name=payload.task_name,
        todays_focus=payload.todays_focus,
        desc=payload.description or "",
        due_date=payload.due_date,
        status="incomplete",
        weight=int(payload.weight),
        category_name=(payload.category_name or "").strip(),
    )
    save()
    return planner.get_tasks()[-1].to_dict()

@app.patch("/tasks/{task_index}/status")
def patch_task_status(task_index: int):
    try:
        planner.set_task_status(task_index)
        save()
        return planner.get_tasks()[task_index].to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")

@app.patch("/tasks/{task_index}/focus")
def patch_task_focus(task_index: int):
    try:
        planner.set_task_todays_focus(task_index)
        save()
        return planner.get_tasks()[task_index].to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")

# Not supported by your pared-down Planner
@app.patch("/tasks/{task_index}")
def patch_task(task_index: int):
    raise HTTPException(status_code=501, detail="Task edit not implemented in this iteration")

@app.delete("/tasks/{task_index}")
def delete_task(task_index: int):
    raise HTTPException(status_code=501, detail="Task delete not implemented in this iteration")

# Steps not supported by your pared-down Planner (keep steps display-only on frontend)
@app.post("/tasks/{task_index}/steps")
def post_add_step(task_index: int):
    raise HTTPException(status_code=501, detail="Step operations not implemented in this iteration")

@app.patch("/tasks/{task_index}/steps/{step_index}/toggle")
def patch_toggle_step(task_index: int, step_index: int):
    raise HTTPException(status_code=501, detail="Step operations not implemented in this iteration")

@app.patch("/tasks/{task_index}/steps/{step_index}")
def patch_edit_step(task_index: int, step_index: int):
    raise HTTPException(status_code=501, detail="Step operations not implemented in this iteration")

@app.delete("/tasks/{task_index}/steps/{step_index}")
def delete_step(task_index: int, step_index: int):
    raise HTTPException(status_code=501, detail="Step operations not implemented in this iteration")

# -------------------------
# Events (read-only in this iteration)
# -------------------------
@app.get("/events")
def get_events():
    return [e.to_dict() for e in planner.get_events()]

@app.post("/events")
def create_event():
    raise HTTPException(status_code=501, detail="Event create not implemented in this iteration")

@app.patch("/events/{event_index}")
def patch_event(event_index: int):
    raise HTTPException(status_code=501, detail="Event edit not implemented in this iteration")

@app.delete("/events/{event_index}")
def delete_event(event_index: int):
    raise HTTPException(status_code=501, detail="Event delete not implemented in this iteration")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("application_controller:app", host="127.0.0.1", port=8000, reload=True)