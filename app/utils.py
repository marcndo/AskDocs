from langchain.document_loaders import PyMuPDFLoader, CSVLoader, WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter


# Load pdf document
def load_pdf(file_path):
    loader = PyMuPDFLoader(file_path)
    document = loader.load()
    return document

# Load csv file 
def load_csv(file_path):
    loader = CSVLoader(file_path)
    document = loader.load()
    return document

# Load url
def load_url(url):
    loader = WebBaseLoader(url)
    document = loader.load()
    return document

# Split document
def split_document(documents, chunk_size=1000, overlap=200):
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)
    split_documents = splitter.split_documents(documents)
    return split_documents

# Process the doucuments
def process_document(file_path=None, url=None, file_type=None):
    documents = []

    if file_type == "pdf" and file_path:
        documents = load_pdf(file_path)
    elif file_type == "csv" and file_path:
        documents = load_csv(file_path)
    elif file_type == "url" and url:
        documents = load_url(url)
    
    split_documents = split_document(documents)
    return split_documents


