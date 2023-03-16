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
    for root, _, files in walk(DL):
        if not files:
            continue
        if root.endswith("__converted"):
            continue
        print("converting", root)
        dst = root + "__converted"
        convert_dir(root, dst)
        to_del.append(root)

    if delete_original:
        for root in to_del:
            rmtree(root)


# split big noise files into smaller chunks of N seconds more similar to the duration of a wake word
def split_into_chunks(SOURCE_DIR, DEST_DIR, seconds=3):
    makedirs(DEST_DIR, exist_ok=True)

    for wav in listdir(SOURCE_DIR):
        if wav.split(".")[-1] not in exts:
            # non audio file, skip
            if isdir(join(SOURCE_DIR, wav)):
                # TODO recursive
                print("skipping directory", wav)
            else:
                print("unrecognized format, skipping", wav)
            continue
        print("chunking", wav)

        converted = join(DEST_DIR, wav)
        wav = join(SOURCE_DIR, wav)

        cmd = ["ffmpeg", "-i", wav, "-f", "segment", "-segment_time",
               str(seconds), "-c", "copy", converted + "%03d.wav"]

        subprocess.call(cmd)


def chunk_building_106_kitchen(delete_original=True):
    src = f"{DL}/building_106_kitchen/background"
    dst = f"{DL}/building_106_kitchen/background_crops"
    if isdir(dst):
        return
    for root, dirs, files in walk(src, topdown=False):
        path = root
        dest = path.replace(src, dst)
        split_into_chunks(root, dest)
    if delete_original:
        rmtree(src)


def chunk_pdsounds(delete_original=True):
    src = f"{DL}/pdsounds_march2009"
    dst = f"{DL}/pdsounds_march2009_crops"
    if isdir(dst):
        return
    for root, dirs, files in walk(src, topdown=False):
        path = root
        dest = path.replace(src, dst)
        split_into_chunks(root, dest)
    if delete_original:
        rmtree(src)


def chunk_speech_commands(delete_original=True):
    src = f"{DL}/speech_commands_v001/_background_noise_"
    dst = f"{DL}/speech_commands_v001/background_noise"
    if isdir(dst):
        return
    for root, dirs, files in walk(src, topdown=False):
        path = root
        dest = path.replace(src, dst)
        split_into_chunks(root, dest)
    if delete_original:
        rmtree(src)


def chunk_all_datasets():
    chunk_building_106_kitchen()
    chunk_pdsounds()
    chunk_speech_commands()


chunk_all_datasets()
convert_all_datasets()
