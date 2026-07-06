# VLM Wind Turbine Blade Damage Detection System

A local Vision-Language Model (VLM) inspection project for wind turbine blade defect detection, structured reasoning, and JSON result generation.

The project uses an OpenAI-compatible local VLM API provided by LM Studio. It focuses on prompt-driven visual reasoning instead of training a traditional image classifier.

---

## 1. Project Overview

This system analyzes wind turbine blade images and asks a local VLM to identify visible defects based on inspection rules.

Main workflow:

1. Load blade images from `data/examples/`
2. Encode each image as base64
3. Send the image and inspection prompt to the LM Studio API
4. Parse the model response as JSON
5. Save per-image results to `outputs/`
6. Generate a batch-level `summary_report.json`

The latest batch prompt is defined in `src/prompts/blade_prompt_v3.py`.

---

## 2. Features

- Local VLM inference through LM Studio
- OpenAI-compatible chat completions API
- Batch processing for blade inspection images
- Streamlit single-image demo UI
- Prompt versions for iterative prompt engineering
- Structured JSON output
- Per-image inference time tracking
- Batch summary report generation
- Automatic skipping of already processed images

---

## 3. Runtime Dependency

This repository does not include model weights and does not use cloud inference by default.

You need a locally running LM Studio server before using the batch script or Streamlit app.

Required setup:

1. Install [LM Studio](https://lmstudio.ai/)
2. Download and load a vision-language model, such as Qwen2.5-VL or Qwen3-VL
3. Enable the OpenAI-compatible API server in LM Studio
4. Make sure this endpoint is available:

```text
http://localhost:1234/v1/chat/completions
```

The batch script uses `"model": "local-model"`, while `app.py` currently uses `"model": "qwen3-vl-8b-instruct-mlx"`. Adjust these values in the code if your LM Studio model name is different.

---

## 4. Project Structure

```text
.
├── app.py                         # Streamlit single-image demo
├── configs/
│   └── model_config.py            # Experimental model config
├── data/
│   └── examples/                  # Example blade images
├── experiments/
│   └── prompt_experiment_log.md   # Prompt experiment notes
├── outputs/                       # Runtime outputs, ignored by git
├── src/
│   ├── api/                       # API test scripts
│   ├── inference/
│   │   ├── batch_inference.py     # Main batch inference entry
│   │   └── inference.py           # Experimental direct local HF inference
│   └── prompts/                   # Prompt versions
└── README.md
```

---

## 5. Installation

Create and activate a Python environment, then install the packages used by the current scripts:

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests streamlit pillow torch transformers
```

If you only run the LM Studio batch pipeline, the core dependency is `requests`. `streamlit` and `pillow` are required by `app.py`; `torch` and `transformers` are used by the experimental direct local inference script.

---

## 6. How to Run

### Test the LM Studio API

```bash
python src/api/api_test.py
```

### Run batch inference

```bash
python src/inference/batch_inference.py
```

The script reads all `.jpg`, `.jpeg`, and `.png` files from `data/examples/` and writes JSON results into `outputs/`.

### Run the Streamlit demo

```bash
streamlit run app.py
```

Upload a blade image in the browser UI and click `Run Inference`.

---

## 7. Output Format

Each processed image is saved as:

```text
outputs/<image_filename>.json
```

For example:

```text
outputs/blade01.jpg.json
outputs/叶片雷击.jpg.json
outputs/summary_report.json
```

Example per-image output:

```json
{
  "image_name": "blade01.jpg",
  "timestamp": "2026-07-03T10:00:00.000000",
  "inference_time_sec": 1.1234,
  "prediction": {
    "defect_detected": true,
    "region": "叶片前缘",
    "defect_type": "开裂",
    "severity": "中度损伤",
    "confidence": 0.86,
    "description": "观察到连续裂纹，因此判断为开裂。"
  }
}
```

Batch summary output:

```json
{
  "total_images": 12,
  "total_time_sec": 18.4321,
  "avg_time_per_image_sec": 1.536,
  "timestamp": "2026-07-03T10:05:00.000000",
  "summary": []
}
```

---

## 8. Notes and Limitations

- The model must return valid JSON. If the model adds Markdown or extra text, `batch_inference.py` may fail to parse that image.
- Already processed images are skipped when their output JSON file exists.
- `outputs/` is treated as runtime data and is ignored by git.
- `src/inference/inference.py` uses a hard-coded local Hugging Face snapshot path and is experimental.
- The system is a VLM reasoning prototype, not a validated industrial safety system.

---

## 9. Future Improvements

- Add `requirements.txt`
- Improve JSON extraction and error recovery
- Add evaluation metrics such as precision, recall, and F1
- Add model and prompt comparison reports
- Add visualization for batch results
- Move model names and API URL into a unified config file

---

## Author

Built as a personal AI engineering project focused on multimodal AI, industrial inspection, prompt engineering, and local VLM deployment.
