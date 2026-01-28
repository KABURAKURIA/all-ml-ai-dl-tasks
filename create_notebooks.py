import nbformat as nbf
import os

NOTEBOOKS_DIR = "ai_inference_notebooks"

def create_notebook(filename, title, task_desc, steps_content):
    nb = nbf.v4.new_notebook()

    # Step 0: Title & Task
    nb.cells.append(nbf.v4.new_markdown_cell(f"# {title}\n\n## Task Description\n{task_desc}"))

    # Step 1: Installation
    nb.cells.append(nbf.v4.new_markdown_cell("## 1. Installation\nInstall necessary libraries."))
    nb.cells.append(nbf.v4.new_code_cell(steps_content['installation']))

    # Step 2: Imports
    nb.cells.append(nbf.v4.new_markdown_cell("## 2. Imports\nImport libraries."))
    nb.cells.append(nbf.v4.new_code_cell(steps_content['imports']))

    # Step 3: Load Data
    nb.cells.append(nbf.v4.new_markdown_cell("## 3. Load Data\nLoad dataset or input data."))
    nb.cells.append(nbf.v4.new_code_cell(steps_content['load_data']))

    # Step 4: Data Cleaning
    nb.cells.append(nbf.v4.new_markdown_cell("## 4. Data Cleaning\nPreprocess the data."))
    nb.cells.append(nbf.v4.new_code_cell(steps_content['data_cleaning']))

    # Step 5: Load Model
    nb.cells.append(nbf.v4.new_markdown_cell("## 5. Load Model\nLoad the model from Hugging Face."))
    nb.cells.append(nbf.v4.new_code_cell(steps_content['load_model']))

    # Step 6: Inference
    nb.cells.append(nbf.v4.new_markdown_cell("## 6. Inference\nRun the model."))
    nb.cells.append(nbf.v4.new_code_cell(steps_content['inference']))

    # Step 7: Save Results (Placeholder, update_notebooks.py will fix/replace)
    nb.cells.append(nbf.v4.new_markdown_cell("## 7. Save Results\nSave outputs."))
    nb.cells.append(nbf.v4.new_code_cell("# Kitchen Sink placeholder\nprint('Saving...')"))

    # Step 8: Advanced Usage
    nb.cells.append(nbf.v4.new_markdown_cell("## 8. Advanced Usage\nExplore further."))
    nb.cells.append(nbf.v4.new_code_cell("print('Try different inputs!')"))

    filepath = os.path.join(NOTEBOOKS_DIR, filename)
    with open(filepath, 'w') as f:
        nbf.write(nb, f)
    print(f"Created {filepath}")

# 1. Audio_06_Voice_Cloning
audio_steps = {
    'installation': "!pip install git+https://github.com/huggingface/transformers sentencepiece datasets torch soundfile librosa -q",
    'imports': """import torch
import soundfile as sf
from transformers import SpeechT5Processor, SpeechT5ForSpeechToSpeech, SpeechT5HifiGan
from datasets import load_dataset""",
    'load_data': """# Load a sample audio from the validation split of the dataset
dataset = load_dataset("hf-internal-testing/librispeech_asr_demo", "clean", split="validation")
example_speech = dataset[0]["audio"]["array"]
sampling_rate = dataset[0]["audio"]["sampling_rate"]
print(f"Loaded audio with sampling rate: {sampling_rate}")""",
    'data_cleaning': """# No specific cleaning needed for this demo, ensuring format
import numpy as np
if len(example_speech) == 0:
    print("Empty audio!")""",
    'load_model': """processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_vc")
model = SpeechT5ForSpeechToSpeech.from_pretrained("microsoft/speecht5_vc")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
print("Models loaded.")""",
    'inference': """# Load Speaker Embeddings (xvectors)
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

# Process Input
inputs = processor(audio=example_speech, sampling_rate=sampling_rate, return_tensors="pt")

# Generate
speech = model.generate_speech(inputs["input_values"], speaker_embeddings, vocoder=vocoder)
audio = (16000, speech.numpy()) # tuple for kitchen sink
print("Voice conversion complete.")"""
}

create_notebook(
    "Audio_06_Voice_Cloning.ipynb",
    "Audio: Zero-Shot Voice Cloning",
    "Convert an input voice to a target speaker's voice using Zero-Shot Voice Conversion with `microsoft/speecht5_vc`.",
    audio_steps
)

# 2. RL_02_Preference_Optimization
rl_steps = {
    'installation': "!pip install trl peft bitsandbytes accelerate datasets transformers -q",
    'imports': """from transformers import AutoTokenizer, TrainingArguments
from trl import DPOTrainer
from datasets import load_dataset""",
    'load_data': """# Load a small DPO dataset
dataset = load_dataset("trilogy/queer-diff", split="train[:100]") # Small subset for demo
print(f"Loaded {len(dataset)} examples.")
print(dataset[0])""",
    'data_cleaning': """# Format dataset for DPO (prompt, chosen, rejected)
def process(row):
    return {
        "prompt": row["prompt"],
        "chosen": row["chosen"],
        "rejected": row["rejected"]
    }
dataset = dataset.map(process)""",
    'load_model': """# Use a tiny model for demonstration purposes on Colab
model_id = "Qwen/Qwen2.5-0.5B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
print(f"Loaded {model_id}")""",
    'inference': """# We simulate a DPO training setup (Inference here is effectively 'Run Training')
# Note: Real training takes time. We set steps to 1 for demonstration.
training_args = TrainingArguments(
    output_dir="./dpo_results",
    per_device_train_batch_size=1,
    max_steps=1, # Demo only
    learning_rate=1e-3,
    logging_steps=1,
    report_to="none"
)

trainer = DPOTrainer(
    model=model_id, # passing ID allows TRL to load it
    ref_model=None, # TRL will load a copy
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
    beta=0.1,
)

print("Starting DPO step...")
trainer.train()
results = "Training complete (1 step demo)."
print(results)"""
}

create_notebook(
    "RL_02_Preference_Optimization.ipynb",
    "RL: Direct Preference Optimization (DPO)",
    "Fine-tune an LLM to align with human preferences using DPO (Direct Preference Optimization), a stable alternative to RLHF.",
    rl_steps
)

# 3. NLP_27_Structured_Output
nlp_steps = {
    'installation': "!pip install outlines transformers accelerate torch -q",
    'imports': """import outlines
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer""",
    'load_data': """prompt = "Generate a character profile for a RPG game."
print(f"Prompt: {prompt}")""",
    'data_cleaning': """# Define the schema
schema = '''
{
  "title": "Character",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "class": { "type": "string", "enum": ["Warrior", "Mage", "Thief"] },
    "level": { "type": "integer" }
  },
  "required": ["name", "class", "level"]
}
'''
print("Schema defined.")""",
    'load_model': """model_id = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
model = outlines.models.transformers(model_id, device="cuda" if torch.cuda.is_available() else "cpu")
print(f"Loaded {model_id} with Outlines.")""",
    'inference': """# Generate structured output
generator = outlines.generate.json(model, schema)
result = generator(prompt)
print("Generated Result:")
print(result)
results = str(result) # For Kitchen Sink"""
}

create_notebook(
    "NLP_27_Structured_Output.ipynb",
    "NLP: Structured Output Generation",
    "Force an LLM to generate valid JSON output adhering to a specific schema using `outlines`.",
    nlp_steps
)
