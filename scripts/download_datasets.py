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


# download datasets of interest
def download_ww_community():
    FOLDER = f"{DL}/ovos-ww-community-dataset-master"
    ZIP_PATH = f"{DL}/ovos-ww-community-dataset.zip"
    ZIP_URL = "https://github.com/OpenVoiceOS/ovos-ww-community-dataset/archive/refs/heads/master.zip"

    if not isfile(ZIP_PATH) and not isdir(FOLDER):
        print("downloading ovos-ww-community-dataset.zip")
        r = requests.get(ZIP_URL)
        if r.status_code != 200:
            raise RuntimeError("download failed")
        with open(ZIP_PATH, "wb") as f:
            f.write(r.content)

    # extract .zip file
    if not isdir(FOLDER):
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(DL)
        remove(ZIP_PATH)
        rmtree(f"{FOLDER}/licenses")
        remove(f"{FOLDER}/readme.md")
        remove(f"{FOLDER}/convert.py")

    assert isdir(FOLDER)


def download_ww_synth():
    FOLDER = f"{DL}/ovos-ww-auto-synth-dataset-dev"
    ZIP_PATH = f"{DL}/ovos-ww-auto-synth-dataset.zip"
    ZIP_URL = "https://github.com/OpenVoiceOS/ovos-ww-auto-synth-dataset/archive/refs/heads/dev.zip"

    if not isfile(ZIP_PATH) and not isdir(FOLDER):
        print("downloading ovos-ww-auto-synth-dataset.zip")
        r = requests.get(ZIP_URL)
        if r.status_code != 200:
            raise RuntimeError("download failed")
        with open(ZIP_PATH, "wb") as f:
            f.write(r.content)

    # extract .zip file
    if not isdir(FOLDER):
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(DL)
        remove(ZIP_PATH)
        rmtree(f"{FOLDER}/scripts")
        rmtree(f"{FOLDER}/.github")
        rmtree(f"{FOLDER}/tts_voices")
        rmtree(f"{FOLDER}/ww_configs")
        remove(f"{FOLDER}/README.md")
        remove(f"{FOLDER}/requirements.txt")
        remove(f"{FOLDER}/.gitignore")

    assert isdir(FOLDER)


def download_pdsounds():
    FOLDER = f"{DL}/pdsounds_march2009"
    ZIP_PATH = f"{DL}/pdsounds_march2009.7z"
    ZIP_URL = "http://downloads.tuxfamily.org/pdsounds/pdsounds_march2009.7z"

    if not isfile(ZIP_PATH) and not isdir(FOLDER):
        print("downloading pdsounds_march2009.7z")
        r = requests.get(ZIP_URL)
        if r.status_code != 200:
            raise RuntimeError("download failed")
        with open(ZIP_PATH, "wb") as f:
            f.write(r.content)

    if not isdir(FOLDER):
        Archive(ZIP_PATH).extractall(DL)
        move(f"{DL}/mp3", FOLDER)
        rmtree(f"{DL}/otherformats")
        remove(f"{DL}/pdsounds_march2009_list.html")
        remove(f"{DL}/license_note.txt")
        remove(ZIP_PATH)

    assert isdir(FOLDER)


def download_NAR():
    FOLDER = f"{DL}/NAR_dataset"
    ZIP_PATH = f"{DL}/NAR_dataset.zip"
    ZIP_URL = "http://perception.inrialpes.fr/Free_Access_Data/Data/NAR_Dataset/NAR_dataset.zip"

    if not isfile(ZIP_PATH) and not isdir(FOLDER):
        print("downloading NAR_dataset.zip")
        r = requests.get(ZIP_URL)
        if r.status_code != 200:
            raise RuntimeError("download failed")
        with open(ZIP_PATH, "wb") as f:
            f.write(r.content)

    # extract .zip file
    if not isdir(FOLDER):
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(FOLDER)
        remove(ZIP_PATH)

    assert isdir(FOLDER)


def download_building_106_kitchen():
    FOLDER = f"{DL}/building_106_kitchen"
    ZIP_PATH = f"{DL}/building_106_kitchen.zip"
    ZIP_URL = "https://www.csc.kth.se/~jastork/downloads/building_106_kitchen.zip"

    if not isfile(ZIP_PATH) and not isdir(FOLDER):
        print("downloading building_106_kitchen.zip")
        r = requests.get(ZIP_URL)
        if r.status_code != 200:
            raise RuntimeError("download failed")
        with open(ZIP_PATH, "wb") as f:
            f.write(r.content)

    # extract .zip file
    if not isdir(FOLDER):
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(DL)
        remove(ZIP_PATH)
        rmtree(f"{DL}/__MACOSX")
        rmtree(f"{FOLDER}/test_sequence")
        remove(f"{FOLDER}/README.txt")
        for f in listdir(f"{FOLDER}/training_segments"):
            move(f"{FOLDER}/training_segments/{f}", f"{FOLDER}/{f}")
        rmtree(f"{FOLDER}/training_segments")
    assert isdir(FOLDER)


def download_speech_commands():
    FOLDER = f"{DL}/speech_commands_v001"
    ZIP_PATH = f"{DL}/speech_commands_v0.01.tar.gz"
    ZIP_URL = "http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz"

    if not isfile(ZIP_PATH) and not isdir(FOLDER):
        print("downloading speech_commands_v0.01.tar.gz")
        r = requests.get(ZIP_URL)
        if r.status_code != 200:
            raise RuntimeError("download failed")
        with open(ZIP_PATH, "wb") as f:
            f.write(r.content)

    # extract .zip file
    if not isdir(FOLDER):
        with tarfile.open(ZIP_PATH) as f:
            # extracting file
            f.extractall(FOLDER)
        remove(ZIP_PATH)

    assert isdir(FOLDER)


def download_all_datasets():
    download_ww_community()
    download_ww_synth()
    download_NAR()
    download_building_106_kitchen()
    download_pdsounds()
    download_speech_commands()


download_all_datasets()
