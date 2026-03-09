# application_controller.py
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel, conint
from typing import Optional
from datetime import date
import datetime

from data_manager import Data_Manager
from planner import Planner

app = FastAPI()

# Make paths stable regardless of working directory
HERE = Path(__file__).resolve().parent
FRONTEND_DIR = HERE / "Front_End"
INDEX_PATH = FRONTEND_DIR / "index.html"
DATA_PATH = HERE / "Data" / "planner.json"

app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

data_manager = Data_Manager(str(DATA_PATH))
planner: Planner = data_manager.open_planner()

def save():
    data_manager.save_planner(planner)

def category_exists(cat_name: str) -> bool:
    for c in planner.get_categories():
        if c.get_category_name() == cat_name:
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

class NewEvent(BaseModel):
    name: str
    category: str
    desc: Optional[str] = ""
    date: str
    start: Optional[str] = ""
    end: Optional[str] = ""

class CategoryPayload(BaseModel):
    category_name: str
    description: Optional[str] = ""

class EditTaskPayload(BaseModel):
    task_name: Optional[str] = None
    category_name: Optional[str] = None
    description: Optional[str] = None
    due_date: Optional[str] = None
    weight: Optional[int] = None
    todays_focus: Optional[bool] = None

class EditEventPayload(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    desc: Optional[str] = None
    date: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None

# -------------------------
# Static/index
# -------------------------
@app.get("/")
def serve_index():
    if not INDEX_PATH.exists():
        raise HTTPException(status_code=404, detail="Front_End/index.html not found")
    return FileResponse(str(INDEX_PATH))

# -------------------------
# Dashboard endpoints (for later iterations)
# -------------------------
@app.get("/dashboard/stats")
def get_dashboard_stats():
    print(type(planner.get_tasks()[0].get_due_date()))
    overdue = len(planner.get_overdue_tasks(None))
    due_soon = len(planner.get_due_soon(None))
    status_counts = planner.get_task_status_counts()
    focus_count = len(planner.get_tasks_in_todays_focus())
    

    return {
        "overdue": overdue,
        "dueSoon": due_soon,
        "incomplete": status_counts.get("incomplete", 0),
        "inProgress": status_counts.get("started", 0),
        "focusCount": focus_count
    }

@app.get("/stats/incomplete-by-category")
def stats_incomplete_by_category():
    return planner.get_incomplete_by_category()

@app.get("/tasks/overdue")
def get_overdue_tasks(today: str | None = None):
    return [x.to_dict() for x in planner.get_overdue_tasks(today)]

@app.get("/tasks/due_soon")
def get_due_soon(today: str | None = None):
    return [x.to_dict() for x in planner.get_due_soon(today)]

@app.get("/tasks/by_status/{status}")
def get_tasks_by_status(status: str):
    s = (status or "").strip().lower()
    return [t.to_dict() for t in planner.get_tasks() if (t.get_status() or "").strip().lower() == s]

@app.get("/tasks/focus")
def get_tasks_focus():
    print("FOCUS VALUES:", [t.get_todays_focus() for t in planner.get_tasks()])
    return [t.to_dict() for t in planner.get_tasks_in_todays_focus()]

# -------------------------
# Categories
# -------------------------
@app.get("/categories")
def get_categories():
    return [c.to_dict() for c in planner.get_categories()]

@app.post("/categories")
def create_category(payload: CategoryPayload):
    name = (payload.category_name or "").strip()
    if name == "":
        raise HTTPException(status_code=400, detail="Category name required")
    if category_exists(name):
        raise HTTPException(status_code=400, detail="Category already exists")

    planner.add_category(name, payload.description or "")
    save()
    return planner.get_categories()[-1].to_dict()

@app.patch("/categories/{cat_index}")
def edit_category(cat_index: int, payload: CategoryPayload):
    try:
        old_name = planner.get_category_by_index(cat_index).get_category_name()
        new_name = (payload.category_name or "").strip()
        if new_name == "":
            raise HTTPException(status_code=400, detail="Category name required")
        if new_name != old_name and category_exists(new_name):
            raise HTTPException(status_code=400, detail="Category already exists")

        planner.edit_category(cat_index, new_name, payload.description or "")

        # cascade rename in tasks/events
        if new_name != old_name:
            for t in planner.get_tasks():
                if t.get_category_name() == old_name:
                    t.set_category_name(new_name)
            for e in planner.get_events():
                if e.get_category_name() == old_name:
                    e.set_category_name(new_name)

        save()
        return planner.get_category_by_index(cat_index).to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Category index out of range")

@app.delete("/categories/{cat_index}")
def delete_category(cat_index: int):
    try:
        name = planner.get_category_by_index(cat_index).get_category_name()

        for t in planner.get_tasks():
            if t.get_category_name() == name:
                t.set_category_name("")
        for e in planner.get_events():
            if e.get_category_name() == name:
                e.set_category_name("")

        planner.remove_category_by_index(cat_index)
        save()
        return {"ok": True}
    except IndexError:
        raise HTTPException(status_code=404, detail="Category index out of range")

# -------------------------
# Tasks
# -------------------------
@app.get("/tasks")
def get_tasks():
    return [t.to_dict() for t in planner.get_tasks()]

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
        category_name=payload.category_name,
    )
    save()
    return planner.get_tasks()[-1].to_dict()

@app.patch("/tasks/{task_index}")
def patch_task(task_index: int, payload: EditTaskPayload):
    try:
        task = planner.get_task_by_index(task_index)

        if payload.category_name is not None:
            cat = (payload.category_name or "").strip()
            if cat != "" and not category_exists(cat):
                raise HTTPException(status_code=400, detail="Category does not exist")

        task.update_task(
            name=payload.task_name,
            todays_focus=payload.todays_focus,
            desc=payload.description,
            due_date=payload.due_date,
            weight=payload.weight,
        )

        if payload.category_name is not None:
            task.set_category_name((payload.category_name or "").strip())

        save()
        return task.to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")

@app.patch("/tasks/{task_index}/status")
def patch_task_status(task_index: int):
    try:
        planner.set_task_status(task_index)
        save()
        return planner.get_task_by_index(task_index).to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")

@app.patch("/tasks/{task_index}/focus")
def patch_task_focus(task_index: int):
    try:
        planner.set_task_todays_focus(task_index)
        save()
        return planner.get_task_by_index(task_index).to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")

@app.delete("/tasks/{task_index}")
def delete_task(task_index: int):
    try:
        planner.delete_task(task_index)
        save()
        return {"ok": True}
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")

# Steps: add / toggle already exist in your version; add edit/delete so UI can exercise Planner methods.
@app.post("/tasks/{task_index}/steps")
def post_add_step(task_index: int, payload: dict):
    try:
        text = (payload.get("text") or "").strip()
        if text == "":
            raise HTTPException(status_code=400, detail="Step text required")
        planner.add_task_step(task_index, text)
        save()
        return planner.get_task_by_index(task_index).to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task index out of range")

@app.patch("/tasks/{task_index}/steps/{step_index}/toggle")
def patch_toggle_step(task_index: int, step_index: int):
    try:
        planner.toggle_task_step(task_index, step_index)
        save()
        return planner.get_task_by_index(task_index).to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task/step index out of range")

@app.patch("/tasks/{task_index}/steps/{step_index}")
def patch_edit_step(task_index: int, step_index: int, payload: dict):
    try:
        text = (payload.get("text") or "").strip()
        if text == "":
            raise HTTPException(status_code=400, detail="Step text required")
        planner.edit_task_step(task_index, step_index, text)
        save()
        return planner.get_task_by_index(task_index).to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task/step index out of range")

@app.delete("/tasks/{task_index}/steps/{step_index}")
def delete_step(task_index: int, step_index: int):
    try:
        planner.remove_task_step(task_index, step_index)
        save()
        return planner.get_task_by_index(task_index).to_dict()
    except IndexError:
        raise HTTPException(status_code=404, detail="Task/step index out of range")

# -------------------------
# Events
# -------------------------
@app.get("/events")
def get_events():
    return [
        {
            "name": e.get_event_name(),
            "category": e.get_category_name(),
            "date": e.get_date(),
            "start": e.get_start_time(),
            "end": e.get_end_time(),
            "desc": e.get_description(),
        }
        for e in planner.get_events()
    ]

@app.post("/events")
def create_event(payload: NewEvent):
    if not category_exists(payload.category):
        raise HTTPException(status_code=400, detail="Category does not exist")

    planner.add_event(
        name=payload.name,
        desc=payload.desc or "",
        date=payload.date,
        start=payload.start or "",
        end=payload.end or "",
        cat_name=payload.category,
    )
    save()

    e = planner.get_events()[-1]
    return {
        "name": e.get_event_name(),
        "category": e.get_category_name(),
        "date": e.get_date(),
        "start": e.get_start_time(),
        "end": e.get_end_time(),
        "desc": e.get_description(),
    }

@app.patch("/events/{event_index}")
def patch_event(event_index: int, payload: EditEventPayload):
    try:
        ev = planner.get_event_by_index(event_index)

        if payload.category is not None:
            cat = (payload.category or "").strip()
            if cat != "" and not category_exists(cat):
                raise HTTPException(status_code=400, detail="Category does not exist")
            ev.set_category_name(cat)

        if payload.name is not None:
            ev.set_event_name(payload.name)
        if payload.desc is not None:
            ev.set_description(payload.desc)
        if payload.date is not None:
            ev.set_date(payload.date)
        if payload.start is not None:
            ev.set_start_time(payload.start)
        if payload.end is not None:
            ev.set_end_time(payload.end)

        save()
        return {
            "name": ev.get_event_name(),
            "category": ev.get_category_name(),
            "date": ev.get_date(),
            "start": ev.get_start_time(),
            "end": ev.get_end_time(),
            "desc": ev.get_description(),
        }
    except IndexError:
        raise HTTPException(status_code=404, detail="Event index out of range")

@app.delete("/events/{event_index}")
def delete_event(event_index: int):
    try:
        planner.remove_event_by_index(event_index)
        save()
        return {"ok": True}
    except IndexError:
        raise HTTPException(status_code=404, detail="Event index out of range")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("application_controller:app", host="127.0.0.1", port=8000, reload=True)
