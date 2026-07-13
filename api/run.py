from fastapi import APIRouter

from services.task_manager import run_task

router = APIRouter()


@router.post("/gaip/v1/tasks/{task_id}/run")
def run_task_api(task_id: str):

    task = run_task(task_id)

    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",

        # TODO: Generate unique request ID.
        "request_id": "REQ-20260709-0005",

        # TODO: Replace with current timestamp.
        "timestamp_ms": 1783562440000,

        "code": 0,
        "message": "success",

        "payload": {
            "task_id": task["task_id"],
            "task_status": task["task_status"]
        }
    }