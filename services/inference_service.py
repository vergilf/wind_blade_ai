import base64
import json

import requests
from src.prompts.blade_prompt_v3 import BLADE_PROMPT

LM_STUDIO_URL = "http://127.0.0.1:1234/v1/chat/completions"


def infer_image(image_path: str) -> dict:
    """
    Infer a single image using LM Studio.

    Args:
        image_path: Local image path.

    Returns:
        Parsed JSON result.
    """

    # Read image
    with open(image_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "model": "Qwen/Qwen2.5-VL-3B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": BLADE_PROMPT,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        "temperature": 0.2,
    }

    response = requests.post(
        LM_STUDIO_URL,
        json=payload,
        timeout=120,
    )

    response.raise_for_status()

    result = response.json()

    content = result["choices"][0]["message"]["content"]

    return json.loads(content)