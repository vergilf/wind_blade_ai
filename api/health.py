from fastapi import APIRouter

router = APIRouter()


@router.get("/gaip/v1/health")
def health():
    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",
        "request_id": "REQ-20260709-0001",
        "timestamp_ms": 1783562400000,
        "code": 0,
        "message": "success",
        "payload": {
            "service_status": "online",
            "deploy_mode": "local_windows_service",
            "os": "Windows 10",
            "model_status": "loaded",
            "current_task_count": 0,
            "memory_usage": 0.38,
        },
    }