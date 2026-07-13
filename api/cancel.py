from fastapi import APIRouter

from services.task_manager import cancel_task

router = APIRouter()


@router.post("/gaip/v1/tasks/{task_id}/cancel")
def task_cancel(
    task_id: str,
    request: dict,
):
    task = cancel_task(
        task_id=task_id,
        reason=request["reason"],
    )

    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",

        # TODO: Demo阶段固定值，后续从请求头 X-Request-Id 读取
        "request_id": "REQ-20260709-0007",

        # TODO: Demo阶段固定值，后续替换为当前毫秒时间戳
        "timestamp_ms": 1783562510000,

        "code": 0,
        "message": "task cancelled",

        "payload": {
            "task_id": task["task_id"],
            "task_status": task["task_status"],
        },
    }