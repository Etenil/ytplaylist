import sys

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from pprint import pprint


def extract(url):
    urlinfo = urlparse(url)
    baseurl = '{}://{}'.format(urlinfo.scheme, urlinfo.netloc)
    r = requests.get(url)
    playlist_page = BeautifulSoup(r.text, 'html.parser')
    playlist_filename = '{}.m3u'.format(playlist_page.title.text)
    with open(playlist_filename, 'w') as playlist:
        playlist.write('#EXTM3U\r\n')
        for video in reversed(playlist_page.find_all('a', class_='pl-video-title-link')):
            playlist.write('#EXTINF:99,{}\r\n'.format(video.text.strip().replace('-', '')))
            playlist.write('{}{}\r\n'.format(baseurl, video['href']))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise "Script requires a youtube playlist as argument"
    extract(sys.argv[1])
