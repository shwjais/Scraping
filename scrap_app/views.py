from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import headlines

# Create your views here.
import urllib.request
import csv
from datetime import datetime
from bs4 import BeautifulSoup
link = 'https://www.indiatoday.in/sports/cricket'
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page,'html.parser')
# for i in soup.find_all('h3'):
#     j=i.text
#     print(j)
def index(request):
   with open('title.csv','a') as csv_file:
    writer=csv.writer(csv_file)
    headlines.objects.all().delete()
    for title_box in soup.find_all('h2'):
        title = title_box.text
        print(title)
        title_instance = headlines.objects.create(top_name = title )
    title_instance.save()
    title_list = headlines.objects.order_by('top_name')
    records = {'access':title_list}
    # index(repeat=10)
    return render(request,'index.html',context=records)

        # writer.writerow([title,datetime.now()])
     # new_instance.save()
#
# def hello(request):
#     return HttpResponse('this is my check')
# def InfoDelete(request,top_name):
#         headlines.objects.filter(top_name=top_name).delete()
#         return redirect(request,'index.html')