
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import os
# ex1
# path = "new file"
# os.makedirs(path)
#ex2
# def remove_empty(file):
#     if len(os.listdir(file))==0:
#          os.removedirs(file)
#
# remove_empty(path)
#ex3
# os.open("path","x")
# try:
#     with open("Z:\יד תשפו\הלוי דבורה\פייתון\lesson5\שיעורי בית/new file/new_exclusive_file.txt", "x") as f:
#         f.write("This is a new file created exclusively.")
# except FileExistsError:
#         print("File 'new_exclusive_file.txt' already exists.")

#ex4
# with open("Z:\יד תשפו\הלוי דבורה\פייתון\lesson5\שיעורי בית/new file/new_exclusive_file.txt", "a") as f:
#     f.write(" hi what's happen? ")

#ex5
# path5="Z:\יד תשפו\הלוי דבורה\פייתון\lesson5\שיעורי בית/new file/new_exclusive_file.txt"
# os.remove(path)

#ex6
path6="Z:\יד תשפו\הלוי דבורה\פייתון\lesson5"
for item in os.listdir(path6):
    print(item)

#ex7
path7=os.getcwd()
print(path7)


