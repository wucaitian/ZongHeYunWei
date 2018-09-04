#!/Users/Chatin/anaconda3/bin/python
#coding=utf-8

import glob
import os

#获取pdf文件路径
pdf_path = '/Volumes/SanDisk/python3/运维脚本(python,shell)/检索电子卷宗对账/pdf_tmp_2'

#获取路径下的所有pdf
pdfs = glob.glob("{}/*.pdf".format(pdf_path))

#pdfminer3k
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument

#PDF内容分析。
def analyze_pdf(pdffile):
    #打开一个pdf文件
    open_pdf_file = open(pdffile,'rb')

    #创建一个PDF对象和文件对象联系起来：分析提取数据
    parser = PDFParser(open_pdf_file)

    #创建一个pdf文档
    document = PDFDocument()

    #连接分析器 与文档对象
    parser.set_document(document)
    document.set_parser(parser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    document.initialize()

    #检查文档是否允许提取内容，不允许就忽略
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        #创建PDF资源管理对象，存储共享资源
        rsrcmgr = PDFResourceManager()

        #创建pdf参数分析器
        laparams = LAParams()

        #创建PDF设备对象,：翻译为需要的内容
        device = PDFPageAggregator(rsrcmgr,laparams=laparams)

        #创建PDF翻译对象：处理页面内容
        interpreter = PDFPageInterpreter(rsrcmgr,device)

        #处理每一页,document.get_pages()获取page列表
        for page in document.get_pages():
            interpreter.process_page(page)

            # 接受该页面的LTPage对象
            layout = device.get_result()

            '''
            这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象 一般包括
            LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文
            本就获得对象的text属性
            '''
            for output in layout:
                if (isinstance(output,LTTextBoxHorizontal)):
                    with open(r'./report.txt','a+') as f:
                        results = output.get_text()
                        f.write(results)
    open_pdf_file.close()
    f.close()

if __name__ == '__main__':
    for pdf in pdfs:
        try:
            analyze_pdf(pdf)
        except:
            print('该文件已损坏，',pdf)
    
    content_list = [list for list in open(r'./report.txt','r')]
    for get_suspects in content_list:
        if get_suspects[2:7] == '犯罪嫌疑人':
            print(get_suspects[:10])

    rmReport = os.system('rm -rf ./report.txt')
    if rmReport == 0:
        print('已删除临时文件report.txt')
    else:
        print('删除临时文件失败，请手动删除')
