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

    for root, _, files in walk(SOURCE_DIR):
        if not files:
            continue
        for f in files:
            if f.split(".")[-1] not in exts:
                continue
            wav = join(root, f)
            converted = join(root.replace(SOURCE_DIR, DEST_DIR), f)
            if not converted.endswith(".wav"):
                converted += ".wav"

            if isfile(converted):
                continue
            print("converting", wav, converted)

            cmd = ["ffmpeg", "-i", wav, "-acodec", "pcm_s16le", "-ar",
                   "16000", "-ac", "1", "-f", "wav", converted, "-y"]
            subprocess.call(cmd)


def convert_all_datasets(delete_original=True):
    to_del = []
    for dataset in listdir(DL):
        dataset_path = f"{DL}/{dataset}"
        if dataset.endswith("__converted"):
            continue
        print(dataset)

        print("converting", dataset_path)
        dst = dataset_path + "__converted"
        convert_dir(dataset_path, dst)
        to_del.append(dataset_path)

    if delete_original:
        for root in to_del:
            rmtree(root, ignore_errors=True)


convert_all_datasets()
