from langchain.document_loaders import PyMuPDFLoader, CSVLoader, WebBaseLoader

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


