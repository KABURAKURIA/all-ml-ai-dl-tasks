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

# 1. Speculative Decoding
spec_steps = {
    'installation': "!pip install transformers torch accelerate bitsandbytes -q",
    'imports': """import torch
import time
from transformers import AutoModelForCausalLM, AutoTokenizer""",
    'load_data': """prompt = "Write a short story about a robot discovering a flower in a post-apocalyptic wasteland."
print(f"Prompt: {prompt}")""",
    'data_cleaning': """pass""",
    'load_model': """# We use a larger target model and a smaller draft model
target_model_id = "Qwen/Qwen2.5-3B-Instruct"
draft_model_id = "Qwen/Qwen2.5-0.5B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(target_model_id)

# Load Target (optimized for T4)
target_model = AutoModelForCausalLM.from_pretrained(
    target_model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Load Draft
draft_model = AutoModelForCausalLM.from_pretrained(
    draft_model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

print("Models loaded.")""",
    'inference': """inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# 1. Standard Generation
print("Running Standard Generation...")
start_time = time.time()
output_standard = target_model.generate(**inputs, max_new_tokens=100)
standard_time = time.time() - start_time
print(f"Standard Time: {standard_time:.4f}s")

# 2. Speculative Decoding
print("\\nRunning Speculative Decoding...")
start_time = time.time()
output_spec = target_model.generate(**inputs, max_new_tokens=100, assistant_model=draft_model)
spec_time = time.time() - start_time
print(f"Speculative Time: {spec_time:.4f}s")

# Check speedup
speedup = standard_time / spec_time
print(f"\\nSpeedup: {speedup:.2f}x")
print("Generated Text:")
print(tokenizer.decode(output_spec[0], skip_special_tokens=True))

results = f"Speedup: {speedup:.2f}x"
"""
}

create_notebook(
    "NLP_31_Speculative_Decoding.ipynb",
    "NLP: Speculative Decoding",
    "Accelerate text generation using a small 'draft' model to predict tokens for a larger 'target' model.",
    spec_steps
)

# 2. ModernBERT
mbert_steps = {
    'installation': """# ModernBERT requires recent transformers
!pip install -q "transformers>=4.48.0" torch accelerate""",
    'imports': """from transformers import pipeline, AutoTokenizer, AutoModelForMaskedLM""",
    'load_data': """text = "ModernBERT is a powerful model that can process [MASK] sequences efficiently."
print(f"Input: {text}")""",
    'data_cleaning': """pass""",
    'load_model': """model_id = "answerdotai/ModernBERT-base"
# ModernBERT supports 8k context natively
pipe = pipeline("fill-mask", model=model_id, device=0) # device=0 for GPU
print(f"Loaded {model_id}")""",
    'inference': """# Basic Inference
outputs = pipe(text)
for out in outputs:
    print(f"Prediction: {out['token_str']} (Score: {out['score']:.4f})")

# Long Context Demo (Simulated)
long_text = "The " * 4000 + "ModernBERT is a powerful model that can process [MASK] sequences efficiently."
# Note: In a real notebook we might not run full 4000 tokens to save time, but it works.
# outputs_long = pipe(long_text)
# print("Long context processed.")

results = str(outputs)
""",
}

create_notebook(
    "NLP_32_ModernBERT.ipynb",
    "NLP: ModernBERT (8k Context)",
    "Explore ModernBERT, a replacement for BERT/RoBERTa with 8k context window and improved architectural efficiency.",
    mbert_steps
)

# 3. DeepSeek Reasoning
deepseek_steps = {
    'installation': "!pip install transformers torch accelerate -q",
    'imports': """import torch
from transformers import AutoModelForCausalLM, AutoTokenizer""",
    'load_data': """prompt = "If a train travels 60mph for 2 hours and then 30mph for 1 hour, what is the average speed?"
# Chat template format is handled by tokenizer typically, but R1-Distill is a CausalLM often used directly or with chat template.
# We will use the chat template.
messages = [
    {"role": "user", "content": prompt}
]
print(f"Prompt: {prompt}")""",
    'data_cleaning': """pass""",
    'load_model': """model_id = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
print("Loaded DeepSeek-R1-Distill-Qwen-1.5B")""",
    'inference': """text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

# Parse <think> tags
if "<think>" in response and "</think>" in response:
    parts = response.split("</think>")
    reasoning = parts[0].replace("<think>", "").strip()
    answer = parts[1].strip()
    print("=== Reasoning Process ===")
    print(reasoning)
    print("\\n=== Final Answer ===")
    print(answer)
else:
    print("=== Response ===")
    print(response)

results = response
""",
}

create_notebook(
    "NLP_33_DeepSeek_Reasoning.ipynb",
    "NLP: DeepSeek Reasoning (Chain-of-Thought)",
    "Use DeepSeek-R1 Distill to generate Chain-of-Thought reasoning, extracting the internal `<think>` process.",
    deepseek_steps
)
