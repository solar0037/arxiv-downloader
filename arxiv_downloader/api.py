import requests
from bs4 import BeautifulSoup

from arxiv_downloader.classes import Paper
from arxiv_downloader.errors import StatusCodeError, ParsingError, SavingError


def find_paper_name(id_: str) -> str:
    """Returns the name of the paper according to the id.

    Parameters:
        - id_(str) - The id of the paper.

    Return type: str

    Raises:
        - arxiv_downloader.StatusCodeError - If recieved wrong status code.
        - arxiv_downloader.ParsingError - If failed to parse html.
    """

    url = f"https://arxiv.org/abs/{id_}"
    res = requests.get(url)
    if res.status_code != 200:
        raise StatusCodeError
    html = res.text

    try:
        soup = BeautifulSoup(html, "html.parser")
        paper_name = str(list(soup.find("h1", "title mathjax"))[1])
    except:
        raise ParsingError

    return paper_name


def download_paper(paper: Paper) -> None:
    """Downloads the given paper.

    Parameters:
        paper(arxiv_downloader.classes.Paper) - The paper to download.

    Raises:
        - arxiv_downloader.StatusCodeError - If recieved wrong status code.
        - arxiv_downloader.SavingError - If failed to save pdf.
    """

    url = f"https://arxiv.org/pdf/{paper.id_}"
    pdf_name = f"{paper.name.replace(': ', ' - ')}.pdf"
    res = requests.get(url)
    if res.status_code != 200:
        raise StatusCodeError

    try:
        with open(pdf_name, "wb") as f:
            res = requests.get(url)
            f.write(res.content)
    except:
        raise SavingError
