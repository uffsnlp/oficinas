"""
Exemplo de pré-processamento de texto com python.

Executar:
    python3 text-preproc.py
"""

import spacy
import unidecode
import num2words as n2w
import word2number as w2n
from bs4 import BeautifulSoup

spacy.cli.download("en_core_web_md")
