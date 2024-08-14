from llama_index.llms.ollama import Ollama

llm = Ollama(model="mistral", request_timeout=30.0)


response = llm.complete("What is the capital of France?")
print(response)
