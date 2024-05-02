"""
This file is countiong words in given txt file
Created by: Arman Hovhannisyan
Date: 29 april 2024
"""
import re

def get_content(fname):
    """
    Function: get_content
    Params: given txt file name
    Brief: opening file, reading and removing non aplphanumeric characters
    Return: returns a list of strings
    """
    with open(fname) as f:
        ket = r"[^\w\s]"
        return re.sub(ket, "", f.read()).split()

def count_words(content):
    """
    Function: count_words
    Params: content: a list of strings
    Brief: counting each word
    return: returns a dictionary of each word how many times used
    """
    word_count = {}
    for word in content:
        if word.isalpha():
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    return word_count


def show_data(sorted_list):
    """
    Function: show_data
    Params: sorted_list
    Brief: printing sorted_list
    """
    for i in sorted_list:
        print(i[0],"-",i[1])


def main():
    """
    Function: main
    Brief: Entery point
    """
    fname = "a.txt"
    content = get_content(fname)
    word_count = count_words(content)
    sorted_list = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    show_data(sorted_list)

if __name__ == "__main__":
    main()

