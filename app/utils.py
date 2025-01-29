import fitz
import pandas as pd
import requests
from bs4 import BeautifulSoup


def parse_pdf(file_path):
    document = fitz.open(file_path)
    text = ""
    for page in document:
        text += page.get_text("text")
    return text

def parse_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string(df)

def parse_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response, "html.parser")
    return soup.get_text()

