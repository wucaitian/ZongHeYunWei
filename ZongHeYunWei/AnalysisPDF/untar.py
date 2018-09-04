#coding=utf-8

import os
import tarfile

#遍历目录，获取所有tar文件
def extractTAR(find_dir):
    #改变当前工作目录
    os.chdir(find_dir)

    for file_name in os.listdir():
        if os.path.isfile(file_name):
            if tarfile.is_tarfile(file_name):
                try:
                    tar = tarfile.open(file_name,'r')
                    for tarMembers in tar.getmembers():
                        tar.extract(tarMembers,'.')
                except tarfile.TarError as err:
                    print(err,'the file is',file_name)
        
        if os.path.isdir(file_name):
            extractTAR(file_name)
            os.chdir(os.pardir)

if __name__ == '__main__':
    find_dir = input('input operation path:')
    extractTAR(find_dir)






