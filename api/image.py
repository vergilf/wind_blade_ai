from fastapi import APIRouter

from services.task_manager import add_image

router = APIRouter()


@router.post("/gaip/v1/tasks/{task_id}/images/by-path")
def upload_image(task_id: str, request: dict):
    """
    Submit a local image path to a task.
    """

    image = add_image(task_id, request)

    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",

        # TODO: Generate unique request ID.
        "request_id": "REQ-20260709-0004",

        # TODO: Replace with current timestamp.
        "timestamp_ms": 1783562430000,

        "code": 0,
        "message": "image path accepted",

        "payload": {
            "task_id": task_id,
            "image_id": image["image_id"],
            "image_status": image["image_status"]
        }
    }