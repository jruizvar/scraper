""" Raspatela para pegar a descrição dos videos mais
    populares de um determinado youtuber.


    O resultado é um arquivo CSV com duas colunas:
      - coluna 1: vid (vídeo-ID)
      - coluna 2: descrição do vídeo
"""
from bs4 import BeautifulSoup
from collections import defaultdict
import pandas as pd
import requests
import sys


def get_video_description(vid):
    """ Para um video-ID (vid) obtém a descrição
    """
    url = f"https://www.youtube.com/watch?v={vid}"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    description = soup.find(id="eow-description").get_text()
    return description


def get_popular_videos(youtuber):
    """ Retorna lista com os vídeo-ids mais populares
    """
    url = f"https://www.youtube.com/{youtuber}/videos?sort=p"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    watch_ids = [s[9:] for s in links if s.startswith("/watch")]
    return set(watch_ids)


def iterate_over_videos(video_ids):
    """ Retorna um dicionário com os textos da descrição
    """
    descriptions = defaultdict(str)
    for vid in video_ids:
        try:
            descriptions[vid] = get_video_description(vid)
        except AttributeError:
            descriptions[vid] = None
    return descriptions


def main(youtuber):
    popular_videos = get_popular_videos(youtuber)
    descriptions = iterate_over_videos(popular_videos)
    out = f"{youtuber}_video_descriptions.csv"
    pd.Series(descriptions, name="description", dtype=str).to_csv(out)


if __name__ == "__main__":
    youtuber = sys.argv[1]
    main(youtuber)
