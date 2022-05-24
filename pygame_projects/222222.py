import os


def human_read_format(size):
    qe = 0
    while size >= 1024:
        size /= 1024
        size = round(size)
        qe += 1
    if qe == 0:
        return f"{size}Б"
    elif qe == 1:
        return f"{size}КБ"
    elif qe == 2:
        return f"{size}МБ"
    elif qe == 3:
        return f"{size}ГБ"


def get_files_sizes():
    for el in os.listdir():
        if  os.path.isfile(el):
            print(el, human_read_format(os.path.getsize(el)))

get_files_sizes()