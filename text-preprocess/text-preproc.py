"""
Exemplo de pré-processamento de texto com python.

Executar:
    python3 text-preproc.py
"""

import pandas as pd
import num2words as n2w
import spacy
import unidecode
import word2number as w2n
from bs4 import BeautifulSoup


# Remoção de caracteres acentuados

def deacc(corpus):
    """
    Recebe um corpus e remove a acentuação de todos os 
    seus documentos.

    Args:
        corpus (pd.DataFrame): Um DataFrame contendo um docuento
            por linha.

    Returns:
        pd.DataFrame: Um DataFrame contendo um docuento
            por linha.
    """

    return corpus_


# Tokenização

def tokenize(corpus, header="text"):
    """Tokeniza um dado corpus de documentos.

    O corpus recebido deve ser um DataFrame. A coluna a ser
    analizada deve possuir o nome `header`.

    Args:
        corpus (pd.DataFrame): Um DataFrame contendo um docuento
            por linha.
        header (str, opcional): Nome da coluna a tirar os valores
            do DataFrame.

    Returns:
        list of list: Lista onde cada entrada é um
            documento tokenizado.
    """

    nlp = spacy.load("en_core_web_md")
    
    tokens = []
    for index, row in corpus.iterrows():
        document = row[header]
        spacy_doc = nlp(document)
        
        tokens.append([token for token in spacy_doc])
            
    return tokens


# Tratamento para números

def treat_numbers(tokens):
    """

    Args:
        tokens (list of list): Lista onde cada entrada é um
            documento tokenizado.

    Returns:
        list of list: Lista onde cada entrada é um
            documento tokenizado.
    """

    return tokens_


# Remoção de Stop Words

def remove_stop_words(tokens):
    """
    Remove os tokens que são stop words.

    Args:
        tokens (list of list): Lista onde cada entrada é um
            documento tokenizado.

    Returns:
        list of list: Lista onde cada entrada é um
            documento tokenizado.
    """

    return tokens_


# Lematização

def lemmatize(tokens):
    """
    Lematiza um conjunto de tokens

    Args:
        tokens (list of list): Lista onde cada entrada é um
            documento tokenizado.

    Returns:
        list of list: Lista onde cada entrada é um
            documento tokenizado.
    """

    return tokens_

if __name__ == "__main__":
    # spacy.cli.download("en_core_web_md")

    raw_dataset = pd.read_csv(
            "../datasets/cbc-news-coronavirus/news.csv",
            nrows=15)

    # Carrega o corpus utilizando apenas o conteúdo das notícias
    corpus = pd.DataFrame(raw_dataset["text"])

    # 
    preprocessed_corpus = ""