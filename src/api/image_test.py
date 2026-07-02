import requests
import base64
import os
import json
from datetime import datetime
from src.prompts.blade_prompt_v1 import BLADE_PROMPT

# 1. 项目根目录
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

# 2. 输入图片
image_path = os.path.join(project_root, "data/examples/blade.jpg")
image_name = os.path.basename(image_path)

# 3. 输出目录
output_dir = os.path.join(project_root, "outputs")
os.makedirs(output_dir, exist_ok=True)

# 4. 读取图片
with open(image_path, "rb") as f:
    base64_image = base64.b64encode(f.read()).decode("utf-8")

# 5. API
url = "http://localhost:1234/v1/chat/completions"

payload = {
    "model": "local-model",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": BLADE_PROMPT
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "temperature": 0.0,
    "max_tokens": 300
}

# 6. 请求
response = requests.post(url, json=payload, timeout=60)
result = response.json()

# 7. 提取模型输出
content = result["choices"][0]["message"]["content"]

print("\n=== MODEL OUTPUT ===")
print(content)

# 8. 解析 JSON
try:
    parsed = json.loads(content)
except Exception as e:
    print("JSON解析失败:", e)
    parsed = None

# 9. 组织工业结构输出
final_output = {
    "image": image_name,
    "timestamp": datetime.now().isoformat(),
    "result": parsed
}

# 10. 保存 JSON 文件
output_file = os.path.join(
    output_dir,
    image_name.replace(".jpg", "_result.json")
)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

print("\n=== SAVED TO ===")
print(output_file)