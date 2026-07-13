from fastapi import APIRouter

router = APIRouter()


@router.get("/gaip/v1/model/info")
def model_info():
    return {
        "protocol": "GAIP-HTTP",
        "version": "1.1",

        # TODO: Generate a unique request ID for each request.
        "request_id": "REQ-20260709-0002",

        # TODO: Replace with current timestamp (milliseconds).
        "timestamp_ms": 1783562410000,

        "code": 0,
        "message": "success",

        "payload": {
            # TODO: Replace with real model information if multiple models are supported.
            "model_id": "BLADE-OBB-001",

            # TODO: Replace with actual model name.
            "model_name": "wind_blade_defect_yolo_obb",

            # TODO: Replace with actual deployed model version.
            "model_version": "v1.0.3",

            # TODO: Replace with actual dataset version.
            "data_version": "dataset_2026_07_A",

            # Demo stage: return fixed value.
            "algorithm": "YOLO-OBB",

            # Demo stage: return fixed value.
            "engine": "ONNXRuntime/TensorRT",

            # TODO: Read actual runtime OS if required.
            "runtime_os": "Windows 10",

            # TODO: Keep consistent with protocol section 4.3 defect codes.
            "supported_defects": [
                "crack",
                "lightning_damage",
                "coating_peeling",
                "corrosion"
            ]
        }
    }