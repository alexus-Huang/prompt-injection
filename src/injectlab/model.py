import ollama

MODEL_NAME = "llama3.2:3b"

def generate(prompt: str) -> str:
    result = ollama.generate(model = MODEL_NAME, prompt = prompt)
    return result.response

if __name__ == "__main__":
    print(generate("Say hello in five words."))