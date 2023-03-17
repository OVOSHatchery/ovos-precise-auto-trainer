import tarfile
import zipfile
from os import listdir, makedirs, remove
from os.path import isdir, isfile, dirname
from shutil import rmtree, move

import requests
from pyunpack import Archive

DL = f"{dirname(dirname(__file__))}/dataset_dl"
makedirs(DL, exist_ok=True)
exts = ["mp3", "mp4", "wav"]



def download_NAR():
    FOLDER = f"{DL}/NAR_dataset"
    ZIP_PATH = f"{DL}/NAR_dataset.zip"
    ZIP_URL = "http://perception.inrialpes.fr/Free_Access_Data/Data/NAR_Dataset/NAR_dataset.zip"

    if isdir(FOLDER):
        rmtree(FOLDER)

    print("downloading NAR_dataset.zip")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        raise RuntimeError("download failed")
    with open(ZIP_PATH, "wb") as f:
        f.write(r.content)

    # extract .zip file
    with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(FOLDER)
    remove(ZIP_PATH)

    assert isdir(FOLDER)


download_NAR()
