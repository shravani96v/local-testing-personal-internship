'''from openpyxl import load_workbook
from transfer.models.major_model import Major
from django.shortcuts import render
from openpyxl import Workbook
from transfer.views.major_views.major_load_data import major_load_data
from transfer.views.school_views.school_load_data import school_load_data
from transfer.views.course_views.course_load_data import course_load_data
from transfer.views.transfer_evaluation_views.evaluation_load_data import evaluation_load_data


def load_file(request):
    if request.method=='POST':
        file = request.FILES['document']
        #print(f'filename is {file}')
        load_data(request,file)
    return render(request, 'import.html')


def load_data(request, file_name):
    wb_obj= load_workbook(filename = file_name, data_only=True)
    major_load_data(request, wb_obj)
    school_load_data(request, wb_obj)
    evaluation_load_data(request, wb_obj)
    course_load_data(request, wb_obj)
'''
