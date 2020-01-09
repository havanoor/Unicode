from django.shortcuts import render
from django.http import HttpResponse
from .models import spaceClass
from . import models
from django.template.loader import render_to_string


import datetime

import requests

# stores dictionary of required values
final=[]


def spacef(request):


    connect=requests.get("https://api.spacexdata.com/v3/launches")
    result=connect.json()
    print(connect.status_code)
    for i in result:


        
        date_time=i['launch_date_utc'][0:10]
        #print(date_time)
        #converting date
        date_obj=datetime.datetime.strptime(date_time ,'%Y-%m-%d')
        date_obj2=datetime.datetime.strftime(date_obj,'%d-%b-%Y')
        #print(type(date_obj))   
        #dictionary of required values
        res={'flight_number':i['flight_number'],'mission_name':i['mission_name'],'time':(date_obj2),'rocket_name':i['rocket']["rocket_name"],'mission_patch':i['links']['mission_patch']}
        final.append(res)
        #print(res['launch_date_utc'])
        #  print(i)
    #dictionary to pass to html page    
    details={'detail':final}
    return render(request ,'hello.html',details)
    #return HttpResponse( "<p><h3>{}<h3></p><br>".format(i) for i in final)
    



#function to add data to the database 
def add_data(request):

        connect=requests.get("https://api.spacexdata.com/v3/launches")
        result=connect.json()
        print(connect.status_code)

        for i in result:
                date_time=i['launch_date_utc'][0:10]+" "+i['launch_date_utc'][11:22]
                print(date_time)
                date_obj=datetime.datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S.%f')



                #adding data to the database
                add=models.spaceClass()
                add.flight_number=i['flight_number']
                add.mission_name=i['mission_name']
                add.rocket_name=i['rocket']["rocket_name"]
                add.mission_patch=i['links']['mission_patch']
                add.time=date_obj
                add.save()
                

                data={"detail":spaceClass.objects.all()}
                ren=render_to_string('hello.html',data)
        print(ren)
        return HttpResponse(ren)
        #return render(request,'hello.html',data)
