import os, string

# 1 Write a Python program to list only directories, files and all directories, files in a specified path.
def test1():
    print("Directories: \t", [dirc for dirc in os.listdir(path) if os.path.isdir(os.path.join(path, dirc))])
    print("Files: \t\t", [dirc for dirc in os.listdir(path) if not os.path.isdir(os.path.join(path, dirc))])
    print("All together: \t", [dirc for dirc in os.listdir(path)])


# 2 Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path
def test2():
    print("File Exists: \t", os.access(path, os.F_OK))
    print("For Read: \t", os.access(path, os.R_OK))
    print("For Writing: \t", os.access(path, os.W_OK))
    print("Executable: \t", os.access(path, os.X_OK))

# 3 Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
def test3():
    print("Path exists: \t\t", os.path.exists(path))
    print("Filename: \t\t", os.path.basename(path))


# 4 Write a Python program to count the number of lines in a text file.
def test4():
    with open("Sample.txt", "r") as f:
        print("The number of lines: ", len(f.readlines()))

# 5 Write a Python program to write a list to a file.
def test5():
    list = ["fsdf","fdsfdsafsad",'fsdfdsaf',"fdsgdfs"]
    with open("Sample.txt", "a") as f:
        for i in list:
            f.write(f"\n {i}")

# 6 Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt
def test6():
    os.chdir("Letters")
    for i in string.ascii_letters:
        with open(i + ".txt", "w") as f:
            f.writelines(i)


# 7 Write a Python program to copy the contents of a file to another file
def test7():
    with open(input("enter filepath to copy from\n"), "r") as f:
        text = f.read()
    with open(input("filepath to copy to\n"), "a") as s:
        s.write(text)

# 8 Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
def test8():
    delpath = input("Enter filepath to delete\n")
    if not os.path.exists(delpath): print("Filepath does not exists"); return
    os.remove(delpath)



path = ""
# path = input("Enter path\n")
# test1() 
# test2() 
# test3()
# test4() 
# test5()
# test6()
# test7()
# test8()