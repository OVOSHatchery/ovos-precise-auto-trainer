import zipfile
from os import listdir, makedirs
from os.path import isdir, dirname
from shutil import rmtree, move

import requests

DL = f"{dirname(dirname(__file__))}/dataset_dl"
makedirs(DL, exist_ok=True)
exts = ["mp3", "mp4", "wav"]


def download_building_106_kitchen():
    FOLDER = f"{DL}/building_106_kitchen"
    ZIP_PATH = f"{DL}/building_106_kitchen.zip"
    ZIP_URL = "https://www.csc.kth.se/~jastork/downloads/building_106_kitchen.zip"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading building_106_kitchen.zip")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    # extract .zip file
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(DL)

    rmtree(f"{DL}/__MACOSX")
    rmtree(f"{FOLDER}/test_sequence")
    for f in listdir(f"{FOLDER}/training_segments"):
        move(f"{FOLDER}/training_segments/{f}", f"{FOLDER}/{f}")
    rmtree(f"{FOLDER}/training_segments")
    assert isdir(FOLDER)


download_building_106_kitchen()
