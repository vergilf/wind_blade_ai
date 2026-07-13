from fastapi import APIRouter

from services.task_manager import create_task

router = APIRouter()


@router.post("/gaip/v1/tasks")
def create_task_api(request: dict):
    # Create task through TaskManager
    task = create_task(request)

    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",

        # TODO: Generate a unique request ID for each request.
        "request_id": "REQ-20260709-0003",

        # TODO: Replace with current timestamp (milliseconds).
        "timestamp_ms": 1783562420000,

        "code": 0,

        # TODO: Keep consistent with customer protocol if modified.
        "message": "task created",

        "payload": {
            "task_id": task["task_id"],
            "task_status": task["task_status"]
        }
    }