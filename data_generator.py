import lzma
import os
import queue
import threading

import UnityPy

import common


def load_worker(path, d_q, line_q):
    while True:
        cnt = 0
        f_name = d_q.get()
        env = UnityPy.load(os.path.join(path, f_name))
        for obj in env.objects:
            if obj.type.name == 'Texture2D' and obj.container is not None \
                    and obj.container.startswith("assets/resources/card/images/illust"):
                # remove prefix and postfix
                card_id = obj.container.split("/")[-1][:-4]
                origin_file_name = obj.assets_file.parent.name
                line_q.put(f"{card_id},{origin_file_name}")
                cnt += 1

        print(f"finish {f_name} -- {cnt}")


if __name__ == '__main__':
    base_path = common.get_md_data_path()
    sub_dirs = os.listdir(base_path)

    thread_num = 5

    q = queue.Queue()
    lines = queue.Queue()

    for d in sub_dirs:
        q.put(d)

    for i in range(thread_num):
        th = threading.Thread(
            target=load_worker,
            args=(base_path, q, lines)
        )
        th.daemon = True
        th.start()

    try:
        with open("card_id.dat", "a") as f:
            while True:
                line = lines.get(timeout=10, block=True)
                f.write(f"{line}\n")
    except queue.Empty:
        print("finish")

    with open("card_id", "wb") as f:
        data = open("card_id.dat", 'rb').read()
        f.write(lzma.compress(data))

