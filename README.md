# 🌬 VLM Wind Turbine Blade Damage Detection System

A Vision-Language Model (VLM) based industrial inspection system for automated wind turbine blade defect detection and analysis.

This project implements a full multimodal inference pipeline that processes blade images and generates structured diagnostic results using prompt-driven reasoning.

---

## 📌 1. Project Overview

This system applies Vision-Language Models (VLMs) to industrial inspection scenarios, specifically wind turbine blade damage detection.

It simulates a real-world AI inspection workflow:

- Input: Wind turbine blade images
- Processing: VLM-based visual reasoning
- Output: Structured diagnostic JSON results

Unlike traditional computer vision classification models, this project focuses on prompt-based visual understanding and reasoning.

---

## ⚙️ 2. Key Features

- Vision-Language Model (VLM) based inference
- Batch image processing pipeline
- Structured JSON output generation
- Inference latency tracking per image
- Automatic result persistence
- Prompt versioning and experimentation logs

---

## 🏗 3. System Architecture

Input Images → Batch Inference → VLM API → Response Parser → JSON Outputs

Pipeline Steps:

1. Load images from dataset directory  
2. Encode images (base64 / binary format)  
3. Send request to VLM inference API  
4. Parse model response into structured format  
5. Save per-image results + batch summary report  

---

## 🧪 4. Example Output

Each image generates a structured prediction:

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

## 🚀 5. How to Run

### 1. Install dependencies
pip install -r requirements.txt

### 2. Start VLM inference service
python run_vlm_server.py

### 3. Run batch inference
python src/inference/batch_inference.py

---

## 🧰 6. Tech Stack

- Python 3.10+
- Vision-Language Model (local API / inference service)
- JSON structured output pipeline
- Batch inference system
- Prompt engineering framework

---

## 📊 7. Output Structure

outputs/
├── blade01.json
├── blade02.json
├── summary_report.json

Each run generates:
- Per-image prediction
- Inference time tracking
- Batch-level summary statistics

---

## 🔬 8. Design Philosophy

This project is designed as a lightweight but extensible AI inspection system, focusing on:

- Prompt-driven visual reasoning instead of fixed classification
- Modular inference pipeline
- Structured outputs for downstream analysis
- Easy extensibility for future model upgrades

---

## 🧭 9. Future Improvements

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