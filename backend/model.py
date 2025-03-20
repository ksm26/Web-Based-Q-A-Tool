from llama_cpp import Llama
import os

MODEL_PATH = "models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Model file not found. Download a GGUF model and place it in the 'models/' folder.")

# Load TinyLlama (Smaller and Faster)
llm = Llama(model_path=MODEL_PATH, n_ctx=1024)

def answer_question(context: str, question: str) -> str:
    prompt = f"Answer the question using ONLY this information:\n{context}\n\nQ: {question}\nA:"
    
    response = llm(prompt, max_tokens=200)
    
    return response["choices"][0]["text"].strip()
