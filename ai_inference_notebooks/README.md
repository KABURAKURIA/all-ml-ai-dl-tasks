# AI Inference Notebooks

This folder contains **51** Jupyter Notebooks, each dedicated to a specific AI/ML task using open-source models.

**No programming experience is required!** The notebooks are documented and explain every step.

## Categories

### Multimodal
1.  `Multimodal_01_Audio_Text_to_Text.ipynb`: Speech Translation.
2.  `Multimodal_02_Document_Question_Answering.ipynb`: Document QA (Donut).
3.  `Multimodal_03_Visual_Document_Retrieval.ipynb`: Document Feature Extraction.
4.  `Multimodal_04_Image_Captioning.ipynb`: Image-to-Text.
5.  `Multimodal_05_Image_Text_to_Image.ipynb`: InstructPix2Pix.
6.  `Multimodal_06_Image_Text_to_Video.ipynb`: Video Generation.
7.  `Multimodal_07_Video_Text_to_Text.ipynb`: Video Captioning.
8.  `Multimodal_08_Visual_Question_Answering.ipynb`: VQA.
9.  `Multimodal_09_LayoutLM_DocQA.ipynb`: Advanced Doc QA.

### Natural Language Processing (NLP)
1.  `NLP_01_Feature_Extraction.ipynb`: Text Embeddings.
2.  `NLP_02_Fill_Mask.ipynb`: Masked Language Modeling.
3.  `NLP_03_Question_Answering.ipynb`: Extractive QA.
4.  `NLP_04_Sentence_Similarity.ipynb`: Semantic Similarity.
5.  `NLP_05_Summarization.ipynb`: Text Summarization.
6.  `NLP_06_Table_Question_Answering.ipynb`: Table QA.
7.  `NLP_07_Sentiment_Analysis.ipynb`: Sentiment Classification.
8.  `NLP_08_Topic_Classification.ipynb`: Topic Classification.
9.  `NLP_09_Text_Generation.ipynb`: LLM Generation.
10. `NLP_10_Text_Ranking.ipynb`: Document Ranking.
11. `NLP_11_NER.ipynb`: Named Entity Recognition.
12. `NLP_12_POS_Tagging.ipynb`: Part-of-Speech Tagging.
13. `NLP_13_Translation_En_Fr.ipynb`: English to French.
14. `NLP_14_Translation_En_De.ipynb`: English to German.
15. `NLP_15_Zero_Shot_Classification.ipynb`: Zero-Shot Text Classification.

### Computer Vision (CV)
1.  `CV_01_Depth_Estimation.ipynb`: Monocular Depth.
2.  `CV_02_Image_Classification.ipynb`: Image Classification.
3.  `CV_03_Image_Feature_Extraction.ipynb`: ViT Features.
4.  `CV_04_Semantic_Segmentation.ipynb`: Pixel Classification.
5.  `CV_05_Instance_Segmentation.ipynb`: Object Segmentation.
6.  `CV_06_Style_Transfer.ipynb`: Image-to-Image.
7.  `CV_07_OCR.ipynb`: Text Recognition.
8.  `CV_08_Image_to_Video.ipynb`: Image Animation.
9.  `CV_09_Keypoint_Detection.ipynb`: Pose/Keypoints.
10. `CV_10_Mask_Generation.ipynb`: SAM (Segment Anything).
11. `CV_11_Object_Detection.ipynb`: Bounding Boxes.
12. `CV_12_Video_Classification.ipynb`: Action Recognition.
13. `CV_13_Text_to_Image.ipynb`: Stable Diffusion.
14. `CV_14_Text_to_Video.ipynb`: Video Generation.
15. `CV_15_Unconditional_Image_Generation.ipynb`: DDPM.
16. `CV_16_Video_to_Video.ipynb`: Video Transformation.
17. `CV_17_Zero_Shot_Image_Classification.ipynb`: CLIP.
18. `CV_18_Zero_Shot_Object_Detection.ipynb`: OwlViT.
19. `CV_19_Text_to_3D.ipynb`: 3D Generation.
20. `CV_20_Image_to_3D.ipynb`: Image to 3D.

### Audio
1.  `Audio_01_Classification.ipynb`: Audio Event Detection.
2.  `Audio_02_Audio_to_Audio.ipynb`: Enhancement.
3.  `Audio_03_ASR.ipynb`: Speech Recognition.
4.  `Audio_04_TTS.ipynb`: Text-to-Speech.

### Tabular & RL
1.  `Tabular_01_Classification.ipynb`: Tabular Classification.
2.  `Tabular_02_Regression.ipynb`: Tabular Regression.
3.  `RL_01_Reinforcement_Learning.ipynb`: Reinforcement Learning (PPO).

## How to use
Run `pip install -q transformers diffusers torch accelerate sentencepiece librosa soundfile pillow` (and others as needed per notebook).
Most notebooks include an installation cell at the top.
