import os


def count_file(dir_path):
    dir_count= os.listdir(dir_path)
    return len(dir_count)


print(count_file("./word"),type(count_file("./word")))