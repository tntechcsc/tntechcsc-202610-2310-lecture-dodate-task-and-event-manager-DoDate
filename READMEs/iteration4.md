# DoDate Project — Iteration 3  
## MVP (Minimum Viable Product)

---

## Warning

**Do not modify `application_controller.py` or `index.html` unless you have received explicit permission from Cal.(not the TAs, not Brandon, not your congressman, not the Cal imposter that haunts your dreams)**

Unauthorized changes to either file will result in a grade of **zero for the entire iteration**.

These files provide the structural foundation for the API and front-end interface. Altering them without approval can break system functionality and invalidate grading.

---

## Description

Welcome to Iteration 2 of your DoDate project!

In this iteration, you will be implementing the most of the CRUD (create, read, update, delete) features. We already have most of the read features with the getters and one of the create features, but now we will be expanding that across all classes. We are also expanding the "Read" features by writing functions that will analyze the data and return various metrics (e.g., how many incomplete tasks per category?, how many overdue tasks are there?, etc.)

All required work is marked with `TODO` comments. A `TODO` represents a clearly defined, incomplete unit of work.

Modern IDEs make these easy to track:

- **PyCharm** includes a built-in TODO tool window.
- **VS Code** supports extensions such as *TODO Tree* for similar functionality.

These tools allow you to:
- View all TODOs organized by file  
- Navigate directly to each TODO  
- Ensure nothing is missed  

Once a TODO has been fully completed, replace `TODO` in the comment with `DONE`.

---

## TODOs
### Planner

The Planner class is the central coordinating component of the system. It owns and manages all categories, tasks, and events. Most application behavior ultimately routes through this class.

- add_task_step
- toggle_task_step
- edit_task_step
- remove_task_step
- edit_task
- get_task_by_index
- get_overdue
- get_due_soon
- get_tasks_in_todays_focus
- get_task_status_counts
- get_incomplete_by_category
- get_category_by_index
- add_category
- edit_category
- remove_category_by_index
- get_event_by_index
- add_event
- remove_event_by_index
- set_event_category
- get_upcoming_events
- get_todays_events

### Task

The Task class represents an actionable to-do item. Tasks have descriptive information and a status (incomplete, in progress, completed).


- update_task
- is_overdue
- add_step
- toggle_step
- edit_step
- remove_step

---

## Running your Program
Once you are ready to run your program, you can run the application_controller.py file by clicking the run button on your IDE while the file is open or using the following command:
```
python3 application_controller.py
```
**If you are on a Windows machine you will need to use "python" instead of "python3".**

## Submission Instructions

Open a terminal and ensure you are inside the repository directory before running any Git commands.

Stage your changes:
```
git add .
```

Commit your work with a clear message describing what you added:
```
git commit -m "Completed Iteration 4 to add CRUD"
```

Push your commit to GitHub:
```
git push
```
Open your repository in GitHub and ensure your work appears in the files.