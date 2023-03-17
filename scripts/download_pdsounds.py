from os import makedirs
from os import makedirs
from os.path import isdir, dirname
from shutil import rmtree, move

import requests
from pyunpack import Archive

DL = f"{dirname(dirname(__file__))}/dataset_dl"
makedirs(DL, exist_ok=True)
exts = ["mp3", "mp4", "wav"]


def download_pdsounds():
    FOLDER = f"{DL}/pdsounds_march2009"
    ZIP_PATH = f"{DL}/pdsounds_march2009.7z"
    ZIP_URL = "http://downloads.tuxfamily.org/pdsounds/pdsounds_march2009.7z"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading pdsounds_march2009.7z")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    Archive(ZIP_PATH).extractall(DL)
    move(f"{DL}/mp3", FOLDER)
    rmtree(f"{DL}/otherformats")

    assert isdir(FOLDER)


download_pdsounds()
