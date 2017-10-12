# YOUTUBE TO M3U PLAYLIST CONVERTER

Converts a Youtube playlist URL to a M3U playlist (for VLC for example).

## Requirements

- Python3
- requests
- beautifulsoup4


## Installation

Install like so:

```
pip3 install -r requirements.txt
```

## USAGE

```
python ytplaylist.py '<url to youtube playlist>'
```

This will create a `m3u` file named after the youtube playlist. Open
with something like VLC.
