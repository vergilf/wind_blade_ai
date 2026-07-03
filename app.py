import streamlit as st
from PIL import Image
import time
import base64
import requests
import json
import io

# =========================
# LM Studio API配置
# =========================
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"

# =========================
# 图片转base64
# =========================
def encode_image(image: Image.Image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()
    return base64.b64encode(img_bytes).decode("utf-8")

# =========================
# 真正VLM推理函数
# =========================
def run_inference(image):
    base64_image = encode_image(image)

    prompt = """
You are an industrial wind turbine blade inspection expert.

Analyze the image carefully and detect any possible blade damage.

Return ONLY valid JSON in the following format:

{
  "damage_type": "...",
  "severity": "low | medium | high",
  "confidence": 0.0-1.0,
  "reason": "short explanation"
}
"""

    payload = {
        "model": "qwen3-vl-8b-instruct-mlx",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
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
        "temperature": 0.2
    }

    start_time = time.time()

    response = requests.post(
        LM_STUDIO_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    end_time = time.time()

    result_text = response.json()["choices"][0]["message"]["content"]

    try:
        result_json = json.loads(result_text)
    except:
        result_json = {
            "raw_output": result_text,
            "parse_error": True
        }

    result_json["inference_time_sec"] = round(end_time - start_time, 3)

    return result_json


# =========================
# Streamlit UI
# =========================
st.set_page_config(
    page_title="Wind Blade VLM System",
    layout="centered"
)

st.title("🌬 Wind Turbine Blade VLM Inspection System (REAL)")
st.write("Now connected to LM Studio Qwen2.5-VL")

uploaded_file = st.file_uploader(
    "Upload blade image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Input Image", use_container_width=True)

    if st.button("Run Inference"):

        with st.spinner("Running VLM inference..."):
            result = run_inference(image)

        st.subheader("📊 Result")
        st.json(result)

        st.subheader("⏱ Inference Time")
        st.write(f"{result.get('inference_time_sec', 0)} seconds")

        # severity提示
        severity = result.get("severity", "unknown")

        if severity == "high":
            st.error("High severity damage detected")
        elif severity == "medium":
            st.warning("Medium severity damage detected")
        elif severity == "low":
            st.success("Low severity damage detected")
        else:
            st.info("Severity not detected")