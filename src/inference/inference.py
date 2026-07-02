from PIL import Image
import torch
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration


# 🚨 关键：必须是你本地 snapshot 路径（替换成你自己的）
MODEL_PATH = "/Users/vergil/.cache/huggingface/hub/models--Qwen--Qwen2.5-VL-3B-Instruct/snapshots/66285546d2b821cf421d4f5eb2576359d3770cd3"


# -----------------------
# 1. 读取图片
# -----------------------
def load_image(image_path):
    return Image.open(image_path).convert("RGB")


# -----------------------
# 2. 加载模型（核心）
# -----------------------
def load_model():

    print("📦 STEP 1: loading processor from local snapshot...")

    processor = AutoProcessor.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True,
        local_files_only=True
    )

    print("✅ STEP 2: processor loaded")

    print("📦 STEP 3: loading model from local snapshot...")

    model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
        MODEL_PATH,
        trust_remote_code=True,
        torch_dtype=torch.float32,   # Mac稳定模式
        device_map=None,             # 禁用 accelerate，避免卡死
        local_files_only=True
    )

    model.eval()

    print("✅ STEP 4: model loaded successfully")

    return model, processor


# -----------------------
# 3. 推理函数
# -----------------------
def run_inference(model, processor, image):

    prompt = "Describe this image in detail."

    inputs = processor(
        text=prompt,
        images=image,
        return_tensors="pt"
    )

    print("🧠 running inference...")

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=128
        )

    result = processor.batch_decode(
        outputs,
        skip_special_tokens=True
    )[0]

    return result


# -----------------------
# 4. 主函数
# -----------------------
def run():

    print("🚀 starting inference pipeline...")

    image = load_image("../../data/examples/blade.jpg")

    print("🖼 image loaded:", image.size)

    model, processor = load_model()

    result = run_inference(model, processor, image)

    print("\n🔥 RESULT:")
    print(result)


if __name__ == "__main__":
    run()