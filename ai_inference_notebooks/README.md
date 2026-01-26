# AI Inference Notebooks

This folder contains **69** "In-Depth" Jupyter Notebooks. Each notebook is dedicated to a specific AI/ML task, using real-world datasets and models from the Hugging Face ecosystem.

**Features:**
- **No programming experience required**: Each step is explained.
- **In-Depth**: Covers installation, library imports, data loading (using `datasets` or real URLs), model loading, inference, and analysis.
- **Visual**: Includes image displays, audio playback, and structured outputs.

## Categories

### Multimodal
1.  `Multimodal_01_Speech_Translation.ipynb`: Translate spoken language directly into text in another language (e.g., French Audio -> English Text).
2.  `Multimodal_02_Document_Question_Answering.ipynb`: Answer questions about a document image (e.g., invoice, receipt) using the visual layout and text content.
3.  `Multimodal_03_Document_Layout_Analysis.ipynb`: Classify a document page into categories (e.g., email, resume, invoice) using its visual structure.
4.  `Multimodal_04_Image_Captioning.ipynb`: Generate a natural language description for an input image.
5.  `Multimodal_05_Image_Editing.ipynb`: Edit an image following a natural language instruction.
6.  `Multimodal_06_Image_to_Video.ipynb`: Animate a static image into a short video clip using Stable Video Diffusion.
7.  `Multimodal_07_Video_Content_Analysis.ipynb`: Analyze a video to understand the action taking place (Video Classification).
8.  `Multimodal_08_Visual_Question_Answering.ipynb`: Answer open-ended questions about an image.
9.  `Multimodal_09_Text_to_Video.ipynb`: Generate a video from a text description.
10.  `Multimodal_10_Vision_Language_Chat.ipynb`: Chat with an image using a Vision Language Model (VLM).

### Natural Language Processing (NLP)
1.  `NLP_01_Feature_Extraction.ipynb`: Convert text into vector representations (embeddings) suitable for downstream tasks like clustering or search.
2.  `NLP_02_Fill_Mask.ipynb`: Predict the most likely word to fill a [MASK] token in a sentence. Useful for understanding context.
3.  `NLP_03_Question_Answering.ipynb`: Extract the answer to a question from a given context paragraph.
4.  `NLP_04_Sentence_Similarity.ipynb`: Compute the semantic similarity score between pairs of sentences.
5.  `NLP_05_Summarization.ipynb`: Produce a concise summary of a long document.
6.  `NLP_06_Table_Question_Answering.ipynb`: Answer questions based on tabular data (TAPAS model).
7.  `NLP_07_Sentiment_Analysis.ipynb`: Determine the polarity (positive/negative) of text.
8.  `NLP_08_Topic_Classification.ipynb`: Classify text into categories using Zero-Shot Classification.
9.  `NLP_09_Text_Generation.ipynb`: Generate text using a modern Large Language Model (LLM).
10.  `NLP_10_Text_Ranking.ipynb`: Rank a list of documents based on relevance to a query using a Cross-Encoder.
11.  `NLP_11_Named_Entity_Recognition.ipynb`: Identify entities such as persons, locations, and organizations in text.
12.  `NLP_12_POS_Tagging.ipynb`: Tag each word in a sentence with its grammatical part of speech (Noun, Verb, Adjective, etc.).
13.  `NLP_13_Translation_En_Fr.ipynb`: Translate text from English to French using MarianMT.
14.  `NLP_14_Translation_En_De.ipynb`: Translate text from English to German using MarianMT.
15.  `NLP_15_Intent_Classification_Zero_Shot.ipynb`: Classify user intent without specific training data.
16.  `NLP_16_LLM_Fine_Tuning.ipynb`: Fine-tune a Large Language Model (LLM) on a custom dataset using Parameter-Efficient Fine-Tuning (PEFT) and Quantization (QLoRA).
17.  `NLP_17_RAG.ipynb`: Perform Retrieval Augmented Generation (RAG) to answer questions based on a specific document or context.
18.  `NLP_18_Agents.ipynb`: Build an AI Agent capable of using tools (like a calculator or Python interpreter) to solve complex problems.
19.  `NLP_19_Advanced_RAG.ipynb`: Improve RAG accuracy using a Cross-Encoder Re-ranker.
20.  `NLP_20_Reasoning.ipynb`: Perform complex reasoning tasks using Chain-of-Thought prompting with a strong small model.
21.  `NLP_21_State_Space_Models.ipynb`: Explore **State Space Models (SSMs)**, specifically the **Mamba** architecture, which offers linear-time scaling with sequence length (unlike Transformers which are quadratic).
22.  `NLP_22_Function_Calling.ipynb`: Demonstrate **Function Calling** (also known as Tool Use), where an LLM generates structured arguments to call external functions instead of just generating text.
23.  `NLP_23_Synthetic_Data_Generation.ipynb`: Use a Large Language Model (LLM) to generate a synthetic dataset for training other models.
24.  `NLP_24_Graph_RAG.ipynb`: Perform Graph RAG by extracting a Knowledge Graph from text and using it to answer questions.
25.  `NLP_25_LLM_Evaluation.ipynb`: Evaluate the quality of generated answers.
26.  `NLP_26_Explainable_AI.ipynb`: Sentiment Analysis & Explainability

### Computer Vision (CV)
1.  `CV_01_Depth_Estimation.ipynb`: Estimate the depth of each pixel in an image to create a depth map using the state-of-the-art **Depth Anything** model.
2.  `CV_02_Image_Classification.ipynb`: Classify an image into one of 1000 categories (ImageNet).
3.  `CV_03_Image_Feature_Extraction.ipynb`: Extract high-level features from an image using a Vision Transformer (ViT).
4.  `CV_04_Semantic_Segmentation.ipynb`: Assign a label to every pixel in the image.
5.  `CV_05_Instance_Segmentation.ipynb`: Detect and segment distinct objects in an image.
6.  `CV_06_Style_Transfer.ipynb`: Transfer style to an image using instruction-based editing.
7.  `CV_07_OCR.ipynb`: Read text from an image using TrOCR (Transformer OCR).
8.  `CV_08_Image_to_Video.ipynb`: Animate an image using Stable Video Diffusion.
9.  `CV_09_Pose_Estimation.ipynb`: Detect human keypoints (pose) in an image using YOLOv8.
10.  `CV_10_Mask_Generation.ipynb`: Generate masks for every object in the image using Segment Anything Model (SAM).
11.  `CV_11_Object_Detection.ipynb`: Detect objects with bounding boxes using DETR (Detection Transformer).
12.  `CV_12_Video_Classification.ipynb`: Classify actions in a video file.
13.  `CV_13_Text_to_Image.ipynb`: Generate images from text using Stable Diffusion.
14.  `CV_14_Text_to_Video.ipynb`: Generate a video from a text prompt.
15.  `CV_15_Unconditional_Generation.ipynb`: Generate random face images using a Denoising Diffusion Probabilistic Model (DDPM).
16.  `CV_16_Video_to_Video.ipynb`: Demonstrating video processing structure. (Note: Dedicated V2V pipelines are complex, often requiring ControlNet).
17.  `CV_17_Zero_Shot_Image_Classification.ipynb`: Classify an image into arbitrary categories using CLIP.
18.  `CV_18_Zero_Shot_Object_Detection.ipynb`: Detect objects defined by text queries using OwlViT.
19.  `CV_19_Text_to_3D.ipynb`: Generate a 3D asset from a text prompt using Shap-E.
20.  `CV_20_Image_to_3D.ipynb`: Convert an image into a 3D asset using Shap-E.
21.  `CV_21_Fast_Image_Generation_LCM.ipynb`: Generate images in seconds using Latent Consistency Models (LCM).
22.  `CV_22_Zero_Shot_Video_Classification.ipynb`: Classify a video into arbitrary categories without specific training, using a Zero-Shot model.
23.  `CV_23_Explainable_AI.ipynb`: Image Classification & Explainability

### Audio
1.  `Audio_01_Classification.ipynb`: Classify the category of a sound or perform Keyword Spotting.
2.  `Audio_02_Audio_Separation.ipynb`: Separate multiple speakers from a single audio recording using SpeechBrain.
3.  `Audio_03_ASR.ipynb`: Transcribe spoken English into text using state-of-the-art models.
4.  `Audio_04_TTS.ipynb`: Synthesize speech from text using the Bark model.
5.  `Audio_05_Music_Generation.ipynb`: Generate music from a text description.

### Tabular, Graphs & RL
1.  `Graph_01_Node_Classification.ipynb`: Classify nodes in a graph using a Graph Convolutional Network (GCN).
2.  `RL_01_Reinforcement_Learning.ipynb`: Train an agent to balance a pole on a cart (CartPole) using Proximal Policy Optimization.
3.  `Tabular_01_Classification.ipynb`: Classify data points in a table (e.g., predicting flower species) using Random Forest.
4.  `Tabular_02_Regression.ipynb`: Predict a continuous value based on input features using Linear Regression.
5.  `Tabular_03_Time_Series_Forecasting.ipynb`: Perform zero-shot time series forecasting using the Chronos model.

## Usage
Run the installation cell at the top of each notebook.
Most notebooks require a GPU for optimal performance (especially Video and Image generation tasks).
