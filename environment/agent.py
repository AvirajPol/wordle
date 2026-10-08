from llama_cpp import Llama

MODEL_PATH = "/Users/ailab/.lmstudio/models/lmstudio-community/Qwen2.5-Coder-7B-Instruct-GGUF/Qwen2.5-Coder-7B-Instruct-Q4_K_M.gguf"

model = Llama(
    model_path=MODEL_PATH,
    n_ctx=2048,
    verbose=False
)
def get_word():
    response = model.create_chat_completion(
        messages=[
            {
            "role": "user",
            "content": "return a random 5 letter word in english and nothing else. dont repeat the word already given by you."
            }
        ],
        max_tokens=20,
        temperature=0.2
    )
    response_text = response["choices"][0]["message"]["content"].split()
    if len(response_text[-1].strip(".,!?*&^%$#@:;/|").lower()) != 5:
        return get_word()
    else:
        return response_text[-1].strip(".,!?*&^%$#@:;/|").lower()

text = get_word()
print(text)