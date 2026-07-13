from fastapi import APIRouter

from services.task_manager import get_task_result

router = APIRouter()


@router.get("/gaip/v1/tasks/{task_id}/result")
def task_result(
    task_id: str,
    include_visual: bool = True,
    include_empty: bool = True,
):
    result = get_task_result(
        task_id=task_id,
        include_visual=include_visual,
        include_empty=include_empty,
    )

    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",

        # TODO: Demo阶段固定值，后续从请求头 X-Request-Id 读取
        "request_id": "REQ-20260709-0006",

        # TODO: Demo阶段固定值，后续替换为当前毫秒时间戳
        "timestamp_ms": 1783562500000,

        "code": 0,
        "message": "success",
        "payload": result,
    }