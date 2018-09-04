#coding=utf-8

import os
import shutil

def search_pdf_file(find_dir,file_extension_name,storePDF_path,file_induction):
    #改变工作目录
    os.chdir(find_dir)
    #获取当前工作目录
    #getcwd = os.getcwd()

    #存放pdf文件的位置
    #storePDF_path = storeDIR

    #列举当前目录，获取所有文件名（含子目录名）
    for each_file_name in os.listdir(path=os.curdir):
        #判断当前文件名是否为一个文件
        if os.path.isfile(each_file_name):
            get_file_name = os.path.splitext(each_file_name)[0]
            get_file_ext = os.path.splitext(each_file_name)[1]

            if get_file_ext in file_extension_name:
                get_file_induction = get_file_name.split('_',2)[2]
                if get_file_induction == file_induction:
                    #移动pdf文件到指定目录
                    shutil.move(each_file_name,storePDF_path)

        #判断当前文件名是否为一个目录
        if os.path.isdir(each_file_name):
            #是一个子目录，调用函数（递归函数），读取子目录
            search_pdf_file(each_file_name,file_extension_name,storePDF_path=storePDF_path,file_induction=file_induction)
            #需要返回上一级目录（目的：最后返回到工作目录）
            os.chdir(os.pardir)
    
if __name__ == '__main__':
    find_dir = input('请输入操作的工作目录：')
    file_induction = 'TQQSYJS'
    #设置存储pdf文件的路径，并创建目录
    storePDF_path = find_dir + os.sep + 'PDF'
    if not os.path.exists(storePDF_path):
        os.mkdir(storePDF_path)
    file_extension_name = ['.pdf']
    search_pdf_file(find_dir,file_extension_name,storePDF_path=storePDF_path,file_induction=file_induction)


