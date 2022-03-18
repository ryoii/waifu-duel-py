import lzma
import os
import sys
import winreg


def get_work_path():
    args = sys.argv
    if len(args) <= 1:
        raise Exception("Work path not found. Ensure you have input the argument.")
    return args[1]


def get_md_data_path():
    try:
        key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Valve\\Steam", reserved=0, access=winreg.KEY_READ)
        steam_path = winreg.QueryValueEx(key, "SteamPath")
    except FileNotFoundError:
        raise Exception("Can not found steam install location.")

    md_local_data_path = os.path.join(steam_path[0], "steamapps", "common", "Yu-Gi-Oh!  Master Duel", "LocalData")
    if not os.path.exists(md_local_data_path):
        raise Exception("Can not found master duel in steam.")

    sub_dir = os.listdir(md_local_data_path)
    if len(sub_dir) == 0:
        raise Exception("Can not found master duel data.")

    data_path = os.path.join(md_local_data_path, sub_dir[0], "0000")
    return data_path


def load_card_data():
    if not os.path.exists("card_id"):
        raise Exception("The file is missing: card_id.")

    data = open("card_id", 'rb').read()
    data = lzma.decompress(data)
    lines = str(data, encoding="utf8").splitlines(keepends=False)
    card_data = {}
    for l in lines:
        (card_id, file_id) = l.split(",")
        card_data[card_id] = file_id.strip('\n')
    return card_data
