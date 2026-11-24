# 🤖 Production AI, Machine Learning & Deep Learning Inference Suite

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C.svg?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg?logo=huggingface&logoColor=white)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An extensive, production-ready collection of **300+ deep learning and artificial intelligence inference notebooks** covering the full spectrum of modern applied AI: Computer Vision, Audio/Speech Processing, Natural Language Understanding, and Generative Multimodal architectures.

---

## 🗂️ Multimodal AI Domain Coverage

### 👁️ Computer Vision (`ai_inference_notebooks/CV_*`)
- **Perception & Segmentation**: Monocular Depth Estimation, Semantic Segmentation, Instance Segmentation, Mask Generation (SAM), Pose Estimation.
- **Classification & Detection**: Zero-Shot Image Classification (CLIP), Object Detection (YOLO/DETR), Zero-Shot Object Detection (OWL-ViT), Video Classification.
- **Generative Vision**: Text-to-Image (Stable Diffusion / SDXL), Image-to-Video, Text-to-Video, Video-to-Video, Neural Style Transfer, Optical Character Recognition (OCR).

### 🎙️ Audio, Speech & Music (`ai_inference_notebooks/Audio_*`)
- **Speech Recognition (ASR)**: Whisper model fine-tuning and zero-shot transcription.
- **Text-to-Speech (TTS) & Voice Cloning**: Neural acoustic modeling, vocoder synthesis, zero-shot voice cloning.
- **Audio Processing**: Source separation (Demucs / Spleeter), Audio Latent Diffusion Models (AudioLDM), Environmental sound classification, Speech Emotion Recognition (SER).

---

## 🚀 Getting Started

```bash
git clone https://github.com/KABURAKURIA/all-ml-ai-dl-tasks.git
cd all-ml-ai-dl-tasks

python -m venv venv
source venv/bin/activate

pip install torch torchvision torchaudio transformers diffusers accelerate datasets
jupyter notebook
```

---

## 🔬 Core Frameworks

- **Deep Learning**: PyTorch, TorchVision, TorchAudio
- **Model Hubs**: Hugging Face `transformers`, `diffusers`, `timm`
- **Inference Acceleration**: ONNX Runtime, TensorRT, FlashAttention
- **Evaluation**: Scikit-Learn, SciPy

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
