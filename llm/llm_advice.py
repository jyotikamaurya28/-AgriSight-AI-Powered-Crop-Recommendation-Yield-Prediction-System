from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load the free Mistral model
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_advice(crop, risk, district):
    prompt = f"""
You are an agricultural expert. A farmer in {district} is planning to grow {crop}.
The predicted crop risk status is: {risk}.

Provide short, clear advice on:
- Precautions to take
- Any early warning signs to monitor
- Best practices for better yield

Keep it very simple and helpful for rural farmers.
"""
    result = pipe(prompt, max_new_tokens=150)[0]["generated_text"]
    return result

# Example usage
print(get_advice)
