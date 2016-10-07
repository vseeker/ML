# coding=utf-8
import os


def GetFileList(dir, fileList):
    newDir = dir
    tmp = []
    if os.path.isfile(dir) and 'exceptions.py' in dir and 'exceptions.pyc' not in dir:  # 若是文件，转化为中文，直接添加
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):  # 若是文件夹，递归遍历添加其下的文件
        for s in os.listdir(dir):
            # 如果需要忽略某些文件夹，使用以下代码
            # if '' == "xxx":
                # continue
            newDir = os.path.join(dir, s)
            GetFileList(newDir, fileList)
    return fileList


# list = GetFileList('D:\\workspace\\PyDemo\\fas', [])
list_path = GetFileList('X:\\', [])
print len(list_path)

with open("path.txt", 'w+') as f:

    for e in list_path:
        f.writelines(e)
        f.writelines('\n')




