from transformers import pipeline
try:
    pipe = pipeline("text-to-audio", model="facebook/musicgen-small")
    print("Pipeline loaded successfully")
except Exception as e:
    print(f"Error: {e}")
