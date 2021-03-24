import urllib.request
from bs4 import BeautifulSoup

from arxiv_downloader.classes import Paper


def find_paper_name(id_: str) -> str:
    """Returns the name of the paper according to the id."""
    url = f"https://arxiv.org/abs/{id_}"
    with urllib.request.urlopen(url) as res:
        html = res.read()
    soup = BeautifulSoup(html, "html.parser")
    paper_name = str(list(soup.find("h1", "title mathjax"))[1])
    return paper_name


def download_paper(paper: Paper) -> None:
    """Downloads the given paper."""
    url = f"https://arxiv.org/pdf/{paper.id_}"
    pdf_name = f"{paper.name.replace(': ', ' - ')}.pdf"
    urllib.request.urlretrieve(url, pdf_name)
