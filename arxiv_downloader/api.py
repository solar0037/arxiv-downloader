import requests
from bs4 import BeautifulSoup

from arxiv_downloader.classes import Paper
from arxiv_downloader.errors import StatusCodeError, ParsingError, SavingError


def find_paper_name(id_: str) -> str:
    """Finds the name of the paper according to the id.

    If the title cannot be found, returns id_ instead.

    Parameters:
        - id_(str) - The id of the paper.

    Return type: str
    """

    try:
        html = _get_paper_html(id_)
        paper_name = _find_title_from_paper_html(html)
    except ParsingError:
        paper_name = id_

    return paper_name


def download_paper(paper: Paper) -> None:
    """Downloads the given paper.

    Parameters:
        - paper(arxiv_downloader.classes.Paper) - The paper to download.

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


def _get_paper_html(id_: str) -> str:
    """Gets the paper html from https://arxiv.org/abs/{id_}.

    Parameters:
        id_ - The id of the paper.

    Return type: str

    Raises:
        - arxiv_downloader.errors.StatusCodeError - If received wrong status code.
    """
    url = f"https://arxiv.org/abs/{id_}"
    res = requests.get(url)
    if res.status_code != 200:
        raise StatusCodeError
    html = res.text
    return html


def _find_title_from_paper_html(html: str) -> str:
    """Finds the title from the paper html.

    Parameters:
        - html(str) - The html to parse.

    Return type: str

    Raises:
        - arxiv_downloader.ParsingError - If failed to parse html.
    """
    try:
        soup = BeautifulSoup(html, "html.parser")
        paper_name = str(list(soup.find("h1", "title mathjax"))[1])
        return paper_name
    except:
        raise ParsingError
