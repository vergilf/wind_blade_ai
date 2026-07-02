import os
import json
import base64
import requests
from datetime import datetime
import time
from src.prompts.blade_prompt_v3 import BLADE_PROMPT

# ========================
# 1. 路径设置
# ========================
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))

image_dir = os.path.join(project_root, "data/examples")
output_dir = os.path.join(project_root, "outputs")
os.makedirs(output_dir, exist_ok=True)

# ========================
# 2. API
# ========================
url = "http://localhost:1234/v1/chat/completions"

# ========================
# 3. 收集图片
# ========================
image_files = [
    f for f in os.listdir(image_dir)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
]

image_files.sort()

print(f"Found {len(image_files)} images")

# ========================
# 4. 批处理循环
# ========================
summary = []

# 🔥 batch开始时间
start_batch_time = time.time()

for idx, img_name in enumerate(image_files):

    img_path = os.path.join(image_dir, img_name)
    output_file = os.path.join(output_dir, img_name + ".json")

    # 跳过已处理
    if os.path.exists(output_file):
        print(f"[{idx+1}/{len(image_files)}] SKIP {img_name}")
        continue

    print(f"[{idx+1}/{len(image_files)}] Processing {img_name}")

    # 🔥 单张图片开始时间
    t0 = time.time()

    # 读取图片
    with open(img_path, "rb") as f:
        base64_image = base64.b64encode(f.read()).decode("utf-8")

    payload = {
        "model": "local-model",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": BLADE_PROMPT},
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

    try:
        response = requests.post(url, json=payload, timeout=120)
        result = response.json()

        content = result["choices"][0]["message"]["content"]

        parsed = json.loads(content)

        # 🔥 单张图片结束时间
        t1 = time.time()
        inference_time = t1 - t0

        # ========================
        # 结构化输出 + 时间
        # ========================
        structured_result = {
            "image_name": img_name,
            "timestamp": datetime.now().isoformat(),
            "inference_time_sec": round(inference_time, 4),
            "prediction": parsed
        }

        # 保存单张结果
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(structured_result, f, ensure_ascii=False, indent=2)

        summary.append(structured_result)

    except Exception as e:
        print(f"ERROR on {img_name}: {e}")

        summary.append({
            "image_name": img_name,
            "timestamp": datetime.now().isoformat(),
            "error": str(e)
        })

# ========================
# 5. 汇总报告
# ========================
total_time = time.time() - start_batch_time
avg_time = total_time / len(image_files)

report = {
    "total_images": len(image_files),
    "total_time_sec": round(total_time, 4),
    "avg_time_per_image_sec": round(avg_time, 4),
    "timestamp": datetime.now().isoformat(),
    "summary": summary
}

report_file = os.path.join(output_dir, "summary_report.json")

with open(report_file, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

print("\nDONE")
print("Report saved:", report_file)

print("\n===== PERFORMANCE REPORT =====")
print(f"Total batch time: {total_time:.2f} sec")
print(f"Average per image: {avg_time:.2f} sec")
print(f"Images processed: {len(image_files)}")