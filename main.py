import sys

from command import *


def main(args):
    if len(args) <= 1:
        show_help()
        return

    command = args[0]
    work_dir = args[1]

    if command == "backup-all":
        if len(args) <= 2:
            backup_path = None
        else:
            backup_path = args[2]
        backup_all(work_dir, backup_path)
    elif command == "backup":
        backup_in_need(work_dir)
    elif command == "build":
        solve_img(work_dir)
    else:
        show_help()


if __name__ == '__main__':
    main(sys.argv[1:])
