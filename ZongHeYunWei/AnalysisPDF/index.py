#coding=utf-8
#引入外部自写的模块
import analyze_PDF
from analyze_PDF import *
import cp_pdf_file
from cp_pdf_file import *
import untar
from untar import *

import os

find_dir = input('请输入操作的工作目录：')
file_extension_name = input('请输入需要操作的文档类型【.扩展名】:')
file_induction = input('请输入要存放的文件分类_induction.pdf:')

#遍历目录，找出所有tar压缩包，并解压
extractTAR(find_dir)

#创建统一存放需要操作文档的路径
storePDF_path = find_dir + os.sep + 'PDFS' + file_induction
if not os.path.exists(storePDF_path):
        os.mkdir(storePDF_path)
file_ext_name_list = []
file_ext_name_list.append(file_extension_name)
try:
    #调用cp_pdf_file.py内部的函数
    cp_pdf_file.search_pdf_file(find_dir=find_dir,file_extension_name=file_ext_name_list,storePDF_path=storePDF_path,file_induction=file_induction)
except shutil.Error as err:
    print(err)

#获取路径下的所有pdf
pdfs = glob.glob("{}/*.pdf".format(storePDF_path))
print('案件数量：共有',len(pdfs),'宗')
for pdf in pdfs:
    try:
        analyze_PDF.analyze_pdf(pdf)
    except:
        print('该文件已损坏，',pdf)
        os.system('rm -rf {}/{}'.format(storePDF_path,pdf))
        continue

content_list = [list for list in open(r'./report.txt','r')]
for get_suspects in content_list:
    if get_suspects[2:7] == '犯罪嫌疑人':
        print(get_suspects[:10])

rmReport = os.system('rm -rf ./report.txt')
if rmReport == 0:
    print('已删除临时文件report.txt')
else:
    print('删除临时文件失败，请手动删除')



