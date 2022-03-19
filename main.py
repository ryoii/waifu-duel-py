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

    if command == "backup-all":
        check_args(args, expect_len=2)
        if len(args) <= 2:
            backup_path = None
        else:
            backup_path = args[2]
        work_dir = args[1]
        backup_all(work_dir, backup_path)
    elif command == "backup":
        check_args(args, expect_len=2)
        work_dir = args[1]
        backup_in_need(work_dir)
    elif command == "build":
        check_args(args, expect_len=2)
        work_dir = args[1]
        solve_img(work_dir)
    elif command == "md":
        check_args(args, expect_len=1)
        os.startfile(common.get_md_data_path())
    else:
        show_help()


if __name__ == '__main__':
    main(sys.argv[1:])
