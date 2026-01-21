# AI Inference Notebooks

This folder contains **61** "In-Depth" Jupyter Notebooks. Each notebook is dedicated to a specific AI/ML task, using real-world datasets and models from the Hugging Face ecosystem.

**Features:**
- **No programming experience required**: Each step is explained.
- **In-Depth**: Covers installation, library imports, data loading (using `datasets` or real URLs), model loading, inference, and analysis.
- **Visual**: Includes image displays, audio playback, and structured outputs.

## Categories

### Multimodal
1.  `Multimodal_01_Speech_Translation.ipynb`: Speech Translation (Whisper).
2.  `Multimodal_02_Document_Question_Answering.ipynb`: Document QA (Donut).
3.  `Multimodal_03_Document_Layout_Analysis.ipynb`: Document Layout (DiT).
4.  `Multimodal_04_Image_Captioning.ipynb`: Image-to-Text.
5.  `Multimodal_05_Image_Editing.ipynb`: InstructPix2Pix.
6.  `Multimodal_06_Image_to_Video.ipynb`: Stable Video Diffusion.
7.  `Multimodal_07_Video_Content_Analysis.ipynb`: VideoMAE.
8.  `Multimodal_08_Visual_Question_Answering.ipynb`: VQA.
9.  `Multimodal_09_Text_to_Video.ipynb`: Text-to-Video Generation.
10. `Multimodal_10_Vision_Language_Chat.ipynb`: Vision Language Chat (Moondream2).

### Natural Language Processing (NLP)
1.  `NLP_01_Feature_Extraction.ipynb`: Text Embeddings.
2.  `NLP_02_Fill_Mask.ipynb`: Masked Language Modeling.
3.  `NLP_03_Question_Answering.ipynb`: Extractive QA.
4.  `NLP_04_Sentence_Similarity.ipynb`: Semantic Similarity.
5.  `NLP_05_Summarization.ipynb`: Text Summarization (CNN/DailyMail).
6.  `NLP_06_Table_Question_Answering.ipynb`: Table QA (TAPAS).
7.  `NLP_07_Sentiment_Analysis.ipynb`: Sentiment Classification (IMDB).
8.  `NLP_08_Topic_Classification.ipynb`: Zero-Shot Topic Classification.
9.  `NLP_09_Text_Generation.ipynb`: LLM Generation (SmolLM2).
10. `NLP_10_Text_Ranking.ipynb`: Re-Ranking (Cross-Encoder).
11. `NLP_11_Named_Entity_Recognition.ipynb`: NER.
12. `NLP_12_POS_Tagging.ipynb`: POS Tagging.
13. `NLP_13_Translation_En_Fr.ipynb`: English to French.
14. `NLP_14_Translation_En_De.ipynb`: English to German.
15. `NLP_15_Intent_Classification_Zero_Shot.ipynb`: Intent Classification.
16. `NLP_16_LLM_Fine_Tuning.ipynb`: LLM Fine-Tuning (QLoRA).
17. `NLP_17_RAG.ipynb`: Retrieval Augmented Generation (RAG).
18. `NLP_18_Agents.ipynb`: AI Agents (smolagents).
19. `NLP_19_Advanced_RAG.ipynb`: Advanced RAG with Re-ranking.
20. `NLP_20_Reasoning.ipynb`: Chain-of-Thought Reasoning (CoT).

### Computer Vision (CV)
1.  `CV_01_Depth_Estimation.ipynb`: Monocular Depth.
2.  `CV_02_Image_Classification.ipynb`: Image Classification (ResNet).
3.  `CV_03_Image_Feature_Extraction.ipynb`: ViT Features.
4.  `CV_04_Semantic_Segmentation.ipynb`: Pixel Classification (SegFormer).
5.  `CV_05_Instance_Segmentation.ipynb`: Object Segmentation (MaskFormer).
6.  `CV_06_Style_Transfer.ipynb`: Style Transfer (InstructPix2Pix).
7.  `CV_07_OCR.ipynb`: Text Recognition (TrOCR).
8.  `CV_08_Image_to_Video.ipynb`: Image Animation (SVD).
9.  `CV_09_Pose_Estimation.ipynb`: Pose/Keypoints (YOLOv8).
10. `CV_10_Mask_Generation.ipynb`: SAM (Segment Anything).
11. `CV_11_Object_Detection.ipynb`: Bounding Boxes (DETR).
12. `CV_12_Video_Classification.ipynb`: Action Recognition (VideoMAE).
13. `CV_13_Text_to_Image.ipynb`: Stable Diffusion.
14. `CV_14_Text_to_Video.ipynb`: Video Generation.
15. `CV_15_Unconditional_Generation.ipynb`: DDPM Faces.
16. `CV_16_Video_to_Video.ipynb`: Video Transformation (Concept).
17. `CV_17_Zero_Shot_Image_Classification.ipynb`: CLIP.
18. `CV_18_Zero_Shot_Object_Detection.ipynb`: OwlViT.
19. `CV_19_Text_to_3D.ipynb`: 3D Generation (Shap-E).
20. `CV_20_Image_to_3D.ipynb`: Image to 3D (Shap-E).
21. `CV_21_Fast_Image_Generation_LCM.ipynb`: Fast Image Generation (LCM).

### Audio
1.  `Audio_01_Classification.ipynb`: Audio Keyword Spotting (SUPERB).
2.  `Audio_02_Audio_Separation.ipynb`: Speech Separation (SpeechBrain).
3.  `Audio_03_ASR.ipynb`: Speech Recognition (LibriSpeech).
4.  `Audio_04_TTS.ipynb`: Text-to-Speech (Bark).
5.  `Audio_05_Music_Generation.ipynb`: Text-to-Music (MusicGen).

### Tabular, Graphs & RL
1.  `Tabular_01_Classification.ipynb`: Tabular Classification (Iris).
2.  `Tabular_02_Regression.ipynb`: Tabular Regression.
3.  `Tabular_03_Time_Series_Forecasting.ipynb`: Time Series (Chronos).
4.  `Graph_01_Node_Classification.ipynb`: Graph Neural Networks (GCN).
5.  `RL_01_Reinforcement_Learning.ipynb`: Reinforcement Learning (CartPole PPO).

## Usage
Run the installation cell at the top of each notebook.
Most notebooks require a GPU for optimal performance (especially Video and Image generation tasks).
