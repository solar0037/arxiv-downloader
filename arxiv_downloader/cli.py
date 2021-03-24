import argparse

from arxiv_downloader import find_paper_name, download_paper
from arxiv_downloader.classes import Paper


def main():
    """Main executable function."""
    parser = argparse.ArgumentParser()
    parser.add_argument("id_", help="the id of the paper you want to download")
    args = parser.parse_args()

    id_ = args.id_
    paper_name = find_paper_name(id_)
    paper = Paper(id_, paper_name)
    download_paper(paper)
