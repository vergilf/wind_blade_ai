"""
Memory Repository

Demo implementation.

Store all task data in Python memory.

TODO:
Replace with MySQL implementation in the future.
"""

tasks = {}


def create_task(task: dict):
    tasks[task["task_id"]] = task
    return task


def get_task(task_id: str):
    return tasks.get(task_id)


def update_task(task_id: str, task: dict):
    tasks[task_id] = task


def get_all_tasks():
    return tasks