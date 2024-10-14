import os
import ollama
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.readers.file import PDFReader
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
os.environ['CURL_CA_BUNDLE'] = ''
embed_model = HuggingFaceEmbedding(model_name="nomic-ai/nomic-embed-text-v1.5",
                                   trust_remote_code=True)
Settings.embed_model = embed_model

def get_index(data, index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        index = VectorStoreIndex.from_documents(data, show_progress=True)
        index.storage_context.persist(persist_dir=index_name)
    else:
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
            )

    return index

pdf_path = os.path.join("data", "Canada.pdf")
canada_pdf = PDFReader().load_data(file=pdf_path)
canada_index = get_index(canada_pdf, "canada")
canada_egine = canada_index.as_query_engine()
