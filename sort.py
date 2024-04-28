import argparse
import os
import shutil

def get_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="This is input file.")
    args = parser.parse_args()
    fname = args.file
    return fname

def sort_files(fname):
    for i in os.listdir(fname):
        f_path = os.path.join(fname, i)
        if os.path.isfile(f_path):
            file_type = i.split(".")[-1]
            ddir = os.path.join(fname, file_type)
        if not os.path.exists(ddir):
            os.mkdir(ddir)
        shutil.move(f_path, ddir)

def main():
    fname = get_argument()
    sort_files(fname)


if __name__ == "__main__":
    main()
