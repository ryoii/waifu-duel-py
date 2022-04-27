import json
import os.path
import re
import shutil

import UnityPy
import requests
from PIL import Image

from common import load_card_data, get_md_data_path


def show_help():
    print("backup-all [output directory]\n"
          "    Backup all card image asset data. About 2.5 GB.\n"
          "    [output directory]  ---  The path of the backup saved.")
    print("backup [work directory] [backup path]\n"
          "    Backup the asset data in need according to the images you supplied.\n"
          "    [work directory]  ---  Backup the asset data in need according to the images you supplied.\n"
          "    [backup path]     ---  Where are the backup sources from. From steam data by default. You can backup from the data you save by backup-all command.")
    print("build [work directory]\n"
          "    Build the asset data that compressed with the images you supplied. And output to [work directory]/output.\n"
          "    [work directory]  ---  Build the asset data in need according to the images you supplied.")


def backup_single_file(base_path, file_id, dest_dir):
    key = file_id[:2]
    dest_parent = os.path.join(dest_dir, key)
    if not os.path.exists(dest_parent):
        os.makedirs(dest_parent)

    src = os.path.join(base_path, key, file_id)
    dest = os.path.join(dest_parent, file_id)
    shutil.copyfile(src, dest)


def backup_all(dest_dir):
    base_path = get_md_data_path()

    card_data = load_card_data()
    file_ids = card_data.values()

    total = len(file_ids)
    current = 0

    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for file_id in file_ids:
        backup_single_file(base_path, file_id, dest_dir)

        current += 1
        progress = current / total
        cnt = 50 * current // total
        print(f"\r{'=' * cnt}>{' ' * (50 - cnt)} {round(progress * 100, 2)}%", end="")


def is_number_file(work_dir, file_name):
    if not os.path.isfile(os.path.join(work_dir, file_name)):
        return False
    (name, ext) = os.path.splitext(file_name)
    return re.match("^\\d+$", name)


def get_img_files(work_dir):
    return [f for f in os.listdir(work_dir) if is_number_file(work_dir, f)]


def backup_in_need(work_dir, backup_path):
    img_files = get_img_files(work_dir)

    card_data = load_card_data()

    for f in img_files:
        card_id, _ = os.path.splitext(f)
        file_id = card_data[card_id]
        if file_id is None:
            print(f"Unknown card: {card_id}")

        backup_single_file(backup_path, file_id, os.path.join(work_dir, "backup"))


def solve_single_img(base_path, file_id, img_file, dest_dir):
    key = file_id[:2]
    dest_parent = os.path.join(dest_dir, key)
    if not os.path.exists(dest_parent):
        os.makedirs(dest_parent)

    env = UnityPy.load(os.path.join(base_path, key, file_id))
    for obj in env.objects:
        if obj.type.name == 'Texture2D':
            data = obj.read()
            img = Image.open(img_file).convert(mode="RGBA")
            img = img.resize((512, 512), Image.ANTIALIAS)
            data.image = img
            data.save()
    with open(os.path.join(dest_parent, file_id), 'wb') as f:
        f.write(env.file.save())


def solve_img(work_dir):
    img_files = get_img_files(work_dir)

    base_path = get_md_data_path()
    card_data = load_card_data()

    total = len(img_files)
    current = 0

    for f in img_files:
        card_id, _ = os.path.splitext(f)
        file_id = card_data[card_id]
        if file_id is None:
            print(f"Unknown card: {card_id}")

        solve_single_img(base_path, file_id, os.path.join(work_dir, f), os.path.join(work_dir, "output"))

        current += 1
        progress = current / total
        cnt = 50 * current // total
        print(f"\r{'=' * cnt}>{' ' * (50 - cnt)} {round(progress * 100, 2)}%", end="")


def install(work_dir):
    base_path = get_md_data_path()
    output_dir = os.path.join(work_dir, "output")

    shutil.copytree(output_dir, base_path)
    print("finished.")

def search(keyword):
    api = "https://ygocdb.com/api/v0/?search="
    res = requests.get(api + keyword)
    cards = json.loads(res.content.decode("UTF8"))["result"]
    if len(cards) > 0:
        for card in cards:
            print("{: <8}{: <30}   {: <30}   {}".format(card["cid"], card["jp_name"], card["cn_name"], card.get("en_name", "")))
    else:
        print("Not found.")