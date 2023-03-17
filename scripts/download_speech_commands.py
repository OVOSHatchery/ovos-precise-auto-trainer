import tarfile
from os import makedirs
from os.path import isdir, dirname
from shutil import rmtree

import requests

DL = f"{dirname(dirname(__file__))}/dataset_dl"
makedirs(DL, exist_ok=True)
exts = ["mp3", "mp4", "wav"]


def download_speech_commands():
    FOLDER = f"{DL}/speech_commands_v001"
    ZIP_PATH = f"{DL}/speech_commands_v0.01.tar.gz"
    ZIP_URL = "http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading speech_commands_v0.01.tar.gz")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    # extract .zip file
    with tarfile.open(ZIP_PATH) as f:
        # extracting file
        f.extractall(FOLDER)

    assert isdir(FOLDER)


download_speech_commands()
