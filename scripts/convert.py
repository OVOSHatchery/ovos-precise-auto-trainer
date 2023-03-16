import subprocess
from os import listdir, makedirs, walk, remove
from os.path import join, isdir, isfile, dirname
from shutil import rmtree

DL = f"{dirname(dirname(__file__))}/dataset_dl"
makedirs(DL, exist_ok=True)
exts = ["mp3", "mp4", "wav"]


# this will convert all files to the correct format
def convert_dir(SOURCE_DIR, DEST_DIR):
    makedirs(DEST_DIR, exist_ok=True)

    for wav in listdir(SOURCE_DIR):
        if wav.split(".")[-1] not in exts:
            continue
        print("converting", wav)
        wav = join(SOURCE_DIR, wav)
        if wav.endswith(".wav"):
            converted = join(DEST_DIR, wav)
        else:
            converted = join(DEST_DIR, wav + ".wav")

        if isfile(converted):
            continue

        cmd = ["ffmpeg", "-i", wav, "-acodec", "pcm_s16le", "-ar",
               "16000", "-ac", "1", "-f", "wav", converted, "-y"]
        subprocess.call(cmd)
        if not wav.endswith(".wav"):
            remove(wav)


def convert_all_datasets(delete_original=True):
    to_del = []
    for dataset in listdir(DL):
        print(dataset)
        if dataset.endswith("__converted"):
            continue
        for root, _, files in walk(dataset):
            print(root, files)
            if not files:
                continue
            print("converting", root)
            dst = root.replace(dataset, dataset + "__converted")
            convert_dir(root, dst)
            to_del.append(root)

    if delete_original:
        for root in to_del:
            rmtree(root)


convert_all_datasets()
