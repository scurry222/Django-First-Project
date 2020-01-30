from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    my_dict = {'insert_me': "I am from views.py"}
    return render(request, 'second_app/index.html', context=my_dict)

def help(request):
    help_dict = {'help_insert': "Help Page"}
    return render(request, 'second_app/help.html', context=help_dict)