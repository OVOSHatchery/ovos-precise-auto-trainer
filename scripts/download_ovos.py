import zipfile
from os import makedirs
from os.path import isdir, dirname
from shutil import rmtree

import requests

DL = f"{dirname(dirname(__file__))}/dataset_dl"
makedirs(DL, exist_ok=True)
exts = ["mp3", "mp4", "wav"]


def download_ww_community():
    FOLDER = f"{DL}/ovos-ww-community-dataset-master"
    ZIP_PATH = f"{DL}/ovos-ww-community-dataset.zip"
    ZIP_URL = "https://github.com/OpenVoiceOS/ovos-ww-community-dataset/archive/refs/heads/master.zip"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading ovos-ww-community-dataset.zip")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    # extract .zip file
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(DL)

    assert isdir(FOLDER)


def download_ww_synth():
    FOLDER = f"{DL}/ovos-ww-auto-synth-dataset-dev"
    ZIP_PATH = f"{DL}/ovos-ww-auto-synth-dataset.zip"
    ZIP_URL = "https://github.com/OpenVoiceOS/ovos-ww-auto-synth-dataset/archive/refs/heads/dev.zip"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading ovos-ww-auto-synth-dataset.zip")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    # extract .zip file
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(DL)

    assert isdir(FOLDER)


download_ww_community()
download_ww_synth()
