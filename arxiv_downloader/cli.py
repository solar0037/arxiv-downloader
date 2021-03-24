import argparse

from arxiv_downloader import find_paper_name, download_paper
from arxiv_downloader.classes import Paper


def main():
    """Main executable function."""
    parser = argparse.ArgumentParser()
    parser.add_argument('ids', nargs='+', help='the id of the paper to download')
    args = parser.parse_args()

    ids = args.ids
    for id_ in ids:
        paper_name = find_paper_name(id_)
        paper = Paper(id_, paper_name)
        download_paper(paper)


if __name__ == '__main__':
    main()
