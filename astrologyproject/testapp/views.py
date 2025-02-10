from django.shortcuts import render
import datetime,random
# Create your views here.
def request_view(request):
    time = datetime.datetime.now()
    names_list =['Sunny','Katrina','Kareena','Deepika','Malika','Alia']
    msg_list =[
        'The Golden days a head',
        'Better to sleep more time in class',
        'Tommorrow is the perfect day to purpose you GF',
        'Very soon you will get job',
        'Very soon you will get marriage..........'
    ]
    h = int(time.strftime('%H'))
    if h<12:
        s = 'Good Morning'
    elif h<16:
        s ='Good Afternoon'
    elif h<21:
        s ='Good Evening'
    else:
        s ='Good Night'
    name = random.choice(names_list)
    msg = random.choice(msg_list)
    my_dict = {'time':time,'name':name,'msg':msg,'wish':s}
    return render(request,'testapp/astrology.html',my_dict)