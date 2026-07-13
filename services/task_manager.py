"""
Task Manager

Responsible for managing all tasks in memory.

Demo version:
- Store tasks in a Python dictionary.
- No database is used.
"""
from services.inference_service import infer_image

# In-memory task storage
# TODO: Replace with database (SQLite/MySQL/Redis) if required.
tasks = {}


def create_task(request: dict):
    """
    Create a new task.

    Args:
        request: Task request from client.

    Returns:
        The created task information.
    """

    task_id = request["task_id"]

    tasks[task_id] = {
        "task_id": task_id,
        "task_status": "created",

        # Business information
        "inspection_id": request["inspection_id"],
        "wind_farm_id": request["wind_farm_id"],
        "turbine_id": request["turbine_id"],
        "blade_id": request["blade_id"],

        # Expected upload information
        "image_count": request["image_count"],

        # Actual uploaded images
        "images": [],

        # TODO: Store inference result.
        "result": None,
    }

    return tasks[task_id]


def get_task(task_id: str):
    """
    Get task information by task ID.

    Args:
        task_id: Unique task ID.

    Returns:
        Task information or None.
    """

    return tasks.get(task_id)


def update_task(task_id: str, status: str):
    """
    Update task status.

    Args:
        task_id: Unique task ID.
        status: New task status.
    """

    if task_id in tasks:
        tasks[task_id]["task_status"] = status


def add_image(task_id: str, request: dict):
    """
    Add image information to a task.

    Args:
        task_id: Target task ID.
        request: Image information from client.

    Returns:
        The added image information.
    """

    image_info = {
        "image_id": request["image_id"],
        "image_name": request["image_name"],
        "image_path": request["image_path"],
        "image_md5": request["image_md5"],
        "capture_time_ms": request["capture_time_ms"],
        "part_hint": request["part_hint"],
        "camera_id": request["camera_id"],

        # TODO: Replace with actual upload status if validation is added.
        "image_status": "ready",
    }

    tasks[task_id]["images"].append(image_info)

    return image_info

def run_task(task_id: str):
    """
    Run a task.

    Args:
        task_id: Target task ID.

    Returns:
        Updated task information.
    """

    task = get_task(task_id)

    if task is None:
        return None

    task["task_status"] = "running"

    results = []

    for image in task["images"]:
        result = infer_image(image["image_path"])

        results.append({
            "image_id": image["image_id"],
            "result": result,
        })

    task["result"] = results
    task["task_status"] = "finished"

    return task

def get_task_status(task_id: str):
    """
    Get current task status.

    Args:
        task_id: Target task ID.

    Returns:
        Task status information.
    """

    task = get_task(task_id)

    if task is None:
        return None

    return {
        "task_id": task["task_id"],
        "task_status": task["task_status"],

        # TODO: Demo阶段返回固定值，后续改为实时计算
        "progress": 100 if task["task_status"] == "finished" else 0,

        # Real：来自创建Task时的image_count
        "total_images": task["image_count"],

        # TODO: Demo阶段返回固定值，后续改为processed_images
        "processed_images": task["image_count"],

        # TODO: Demo阶段返回固定值，后续统计真正成功识别数量
        "success_images": task["image_count"],

        # TODO: Demo阶段返回固定值，后续统计失败数量
        "failed_images": 0,

        # TODO: Demo阶段返回最后一张图片ID，后续改为当前正在处理图片
        "current_image_id": (
            task["images"][-1]["image_id"]
            if task["images"]
            else ""
        ),
    }

def get_task_result(
    task_id: str,
    include_visual: bool,
    include_empty: bool,
):
    """
    Get task inference result.

    Args:
        task_id: Target task ID.
        include_visual: Whether to include visualization path.
        include_empty: Whether to include normal images.

    Returns:
        Task inference results.
    """

    task = get_task(task_id)

    if task is None:
        return None

    results = task["result"]

    # TODO: Demo阶段暂不根据 include_empty 过滤正常图片
    # 后续根据 defect_detected 过滤结果

    # TODO: Demo阶段未生成画框图片
    # 后续返回 visual_result_path

    return results

def cancel_task(task_id: str, reason: str):
    """
    Cancel a task.

    Args:
        task_id: Target task ID.
        reason: Cancel reason.

    Returns:
        Updated task.
    """

    task = get_task(task_id)

    if task is None:
        return None

    task["task_status"] = "cancelled"

    # TODO: Demo阶段暂不记录取消原因
    # 后续保存到数据库或日志系统

    return task