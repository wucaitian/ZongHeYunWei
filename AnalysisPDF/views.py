from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest, HttpResponse
def index(request):
    return render(request,'index.html')

def PDF(request):
    from AnalysisPDF import analyze_PDF
    from AnalysisPDF import cp_pdf_file
    from AnalysisPDF import untar
    import glob
    import os
    import shutil
    find_dir = request.POST.get('workpath')
    file_extension_name = request.POST.get('extension')
    file_induction = request.POST.get('induction')
    #遍历目录，找出所有tar压缩包，并解压
    untar.extractTAR(find_dir)

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
    CASEcount = len(pdfs)
    PDFSbad = []
    for pdf in pdfs:
        try:
            analyze_PDF.analyze_pdf(pdf)
        except:
            PDFSbad.append(pdf)
            os.system('rm -rf {}/{}'.format(storePDF_path,pdf))
            continue

    content_list = [list for list in open(r'./report.txt','r')]
    suspects = []
    for get_suspects in content_list:
        if get_suspects[2:7] == '犯罪嫌疑人':
            suspects.append(get_suspects[:10])

    rmReport = os.system('rm -rf ./report.txt')
    if rmReport == 0:
        DEL = '已删除临时文件report.txt'
    else:
        DEL = '删除临时文件失败，请手动删除'
    return render(request,'pdfstatus.html',locals())
