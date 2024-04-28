import re

def get_content(fname):
    with open(fname) as f:
        ket = r"[^\w\s]"
        return re.sub(ket, "", f.read()).split()

def count(content):
    md = {}
    for i in content:
        if i.isalpha():
            if i in md:
                md[i] += 1
            else:
                md[i] = 1
    return md


def show_data(ml):
    for i in ml:
        print(i[0],"-",i[1])


def main():
    fname = "a.txt"
    content = get_content(fname)
    md = count(content)
    ml = sorted(md.items(), key=lambda x: x[1], reverse=True)
    show_data(ml)

if __name__ == "__main__":
    main()
