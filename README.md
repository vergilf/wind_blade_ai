# 🌬 VLM Wind Turbine Blade Damage Detection System

A Vision-Language Model (VLM) based industrial inspection system for automated wind turbine blade defect detection and reasoning.

This project implements a VLM-based inference and reasoning pipeline powered by a **locally deployed VLM (LM Studio)**, performing prompt-driven visual understanding instead of traditional classification.

---

## 📌 1. Project Overview

This system applies Vision-Language Models (VLMs) to industrial inspection tasks, specifically wind turbine blade damage analysis.

It simulates a real-world AI inspection workflow:

- Input: Wind turbine blade images
- Processing: Prompt-driven multimodal reasoning via VLM
- Output: Structured JSON diagnostic results

Unlike traditional computer vision classification models, this project focuses on **visual reasoning and structured generation**.

---

## ⚙️ 2. Key Features

- Vision-Language Model (VLM) based inference (local deployment via LM Studio)
- Batch image processing pipeline
- Structured JSON output generation
- Inference latency tracking per image
- Prompt engineering experiments (v1 → v3)
- Automatic result persistence
- Reproducible batch inference system

---

## ⚠️ 3. Runtime Dependency (IMPORTANT)

This project requires a locally running Vision-Language Model server.

It does NOT include model weights or cloud inference.

### Required Setup:

1. Install LM Studio:
   https://lmstudio.ai/

2. Download a Vision-Language Model:
   - Example: Qwen2.5-VL-3B-Instruct

3. Enable OpenAI-compatible API Server in LM Studio

4. Start server at:

http://localhost:1234/v1/chat/completions

If LM Studio is not running, the project will not work.

---

## 🏗 4. System Architecture

Input Images → Batch Inference → Base64 Encoding → LM Studio VLM API → Prompt Reasoning → JSON Parser → Output Files

### Pipeline Steps:

1. Load images from `data/examples/`
2. Encode images to base64 format
3. Send request to LM Studio VLM API
4. Apply prompt-based visual reasoning
5. Parse model response into structured JSON
6. Save per-image results
7. Generate batch summary report

---

## 🧪 5. Example Output

Each image produces a structured prediction:

```json
{
  "image_name": "blade01.jpg",
  "inference_time_sec": 1.12,
  "prediction": {
    "damage_type": "leading_edge_crack",
    "severity": "medium",
    "confidence": 0.86
  }
}

---

## 🚀 6. How to Run

## ⚠️ Runtime Dependency

This project requires a locally running Vision-Language Model served via LM Studio.

It does NOT include model weights or cloud inference access.

Without LM Studio running, inference scripts will fail.

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start LM Studio
Enable API server
Ensure endpoint:
http://localhost:1234/v1/chat/completions

### 3. Run batch inference
python src/inference/batch_inference.py

---

## 🧰 7. Tech Stack

- Python 3.10+
- Vision-Language Model (LM Studio local API)
- OpenAI-compatible API format
- Prompt engineering framework
- Batch inference pipeline
- JSON structured output system

---

## 📊 8. Output Structure

outputs/
├── blade01.json
├── blade02.json
├── summary_report.json

Each run generates:
- Per-image prediction
- Inference time tracking
- Batch-level summary statistics

---

## 🔬 9. Design Philosophy

This project is designed as a lightweight but extensible AI inspection system, focusing on:

- Prompt-driven visual reasoning instead of fixed classification
- Modular inference pipeline
- Structured outputs for downstream analysis
- Easy extensibility for future model upgrades

---

## 🧭 10. Future Improvements

- Add evaluation metrics (precision / recall / F1)
- Introduce model comparison framework
- Build web visualization dashboard
- Integrate active learning loop
- Improve prompt engineering strategy (v2 → v3 → production)

---

## 👤 Author

Built as a personal AI engineering project focusing on:

- Multimodal AI systems
- Industrial inspection applications
- Prompt engineering for Vision-Language Models
- Local deployment AI systems (LM Studio based)