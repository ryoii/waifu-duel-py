import sys

import common
from command import *


def check_args(args, expect_len):
    if len(args) < expect_len:
        show_help()
        exit(0)


def main(args):
    check_args(args, expect_len=1)
    command = args[0]
    args = args[1:]

    if command == "backup-all":
        check_args(args, expect_len=1)
        if len(args) <= 1:
            backup_path = None
        else:
            backup_path = args[1]
        work_dir = args[0]
        backup_all(work_dir, backup_path)
    elif command == "backup":
        check_args(args, expect_len=1)
        if len(args) <= 1:
            backup_path = None
        else:
            backup_path = args[1]
        work_dir = args[0]
        backup_in_need(work_dir, backup_path)
    elif command == "build":
        check_args(args, expect_len=1)
        work_dir = args[0]
        solve_img(work_dir)
    elif command == "install":
        check_args(args, expect_len=1)
        work_dir = args[0]
        install(work_dir)
    elif command == "md":
        check_args(args, expect_len=1)
        os.startfile(common.get_md_data_path())
    else:
        show_help()


if __name__ == '__main__':
    main(sys.argv[1:])
