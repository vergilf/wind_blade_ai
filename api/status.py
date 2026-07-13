from fastapi import APIRouter

from services.task_manager import get_task_status

router = APIRouter()


@router.get("/gaip/v1/tasks/{task_id}/status")
def task_status(task_id: str):
    status = get_task_status(task_id)

    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",

        # TODO: Demo阶段固定值，后续从请求头 X-Request-Id 读取
        "request_id": "REQ-20260709-0005",

        # TODO: Demo阶段固定值，后续替换为当前毫秒时间戳
        "timestamp_ms": 1783562440000,

        "code": 0,
        "message": "success",
        "payload": status,
    }