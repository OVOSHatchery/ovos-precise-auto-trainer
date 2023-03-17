import zipfile
from os import makedirs
from os.path import isdir, dirname
from shutil import rmtree

import requests

DL = f"{dirname(dirname(__file__))}/dataset_dl"
makedirs(DL, exist_ok=True)
exts = ["mp3", "mp4", "wav"]


def download_hey_ff():
    FOLDER = f"{DL}/hey-ff-data"
    ZIP_PATH = f"{DL}/hey-ff-data.zip"
    ZIP_URL = "https://nlp.nyc3.digitaloceanspaces.com/hey-ff-data.zip"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading hey-ff-data.zip")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    # extract .zip file
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(FOLDER)

    assert isdir(FOLDER)


def download_hey_ff_noise():
    FOLDER = f"{DL}/hey-ff-noise"
    ZIP_PATH = f"{DL}/hey-ff-noise"
    ZIP_URL = "https://nlp.nyc3.digitaloceanspaces.com/hey-ff-noise.zip"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading hey-ff-noise")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    # extract .zip file
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(FOLDER)

    assert isdir(FOLDER)


download_hey_ff()
download_hey_ff_noise()
