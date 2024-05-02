"""
This file is for sorting different files inside directory
Created by: Arman Hovhannisyan
Date: 29 april 2024
"""
import argparse
import os
import shutil

def get_argument():
    """
    Function: get_argument
    Brief: parsing arguments
    Return: filename
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="This is input file.")
    args = parser.parse_args()
    fname = args.file
    return fname

def sort_files(fname):
    """
    Function: sort_files
    Params: Entered directory name
    Brief: sorting files in given directory each one its type of file
    """
    for file_name in os.listdir(fname):
        f_path = os.path.join(fname, file_name)
        file_type = file_name.split(".")[-1]
        ddir = os.path.join(fname, file_type)
        if not os.path.exists(ddir):
            os.mkdir(ddir)
        shutil.move(f_path, ddir)

def main():
    """
    Function: main
    Brief: Entery point
    """
    fname = get_argument()
    sort_files(fname)


if __name__ == "__main__":
    main()
