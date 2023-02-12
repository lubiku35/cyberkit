import os

directory = "data_collect//mycom"

path = os.getcwd()
x =  ""
for i in path:
    if i == '\\':
        i = "/"
        x += i
    x += i

final_path = x + "//" + directory

os.mkdir(final_path)