from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Tolldetails
import datetime
import os
# import pyqrcode
import requests
import json
from .models import Orders,Users
from qrtools import QR

# Create your views here.
def Toll_Info(request):
    error = True
    qry1={}
    if 'HTTP_COOKIE' in request.META:

        vehicle = request.session['vehicle_type']
        vehicle = vehicle.lower()
        qry1 = Tolldetails.objects.extra(select={'id':'id','latitude':'latitude','longitude':'longitude','tollname':'tollname','tollplazaid':'tollplazaid','cost':vehicle}).values('id','latitude','longitude','tollname','tollplazaid','cost')

        if qry1.count() > 0:

            error = False
            msg = "Success"
        else:
            msg= "Oops!! Servers are Busy rigth now... Data Can't be fetched!"
    else:
        msg="Session expired!"
    data = {'AllTolls':list(qry1),'error':error,'msg':msg}
    #print(data)
    return JsonResponse(data,safe=False)


def request_qr(request):
    msg=""
    error=True
    if 'HTTP_COOKIE' in request.META:
        if request.GET:
            data=request.GET
            qr_s=data['orderid']
            tid=data['tollid']
            qr_s2=qr_S.split('?')
            qr_s3=qr_s2[1].split('#')
            
            qry=Orders.objects.filter(tollplazaid=tid,user_id=uid,type_value__gte=0,amount=qr_s3[0]).values('sno','type_value')
            if len(qry)>0:
                qry_u=Orders.objects.filter(sno=qry[0]['sno']).update(type_value=qry[0]['type_value']-1)
                error=False
                msg="Qr Valid"
            else:
                msg="QR Invalid"
        else:
            msg="Invallid Request!"
    else:
        msg = "Session Expired!"
    return JsonResponse(msg=msg,error=error)



def profile(request):
    msg=""
    error=True
    val={}
    if 'HTTP_COOKIE' in request.META:
        if(request.method == 'GET'):
            veh_no=request.session['VIN']
            qry_de=Users.objects.filter(vehicle_no=veh_no).values()
           # qry_de=Users.objects.get().values()
            if len(qry_de)>0:
                msg="User exist"
                error=False
                val=list(qry_de)
            else:
                msg="User Not Found"
        else:
            msg="Invalid Request!"
    else:
        msg="Session Expired!"
    data = {'msg':msg,'error':error,'data':val}    
    return JsonResponse(data,safe=False)



def previousOrders(request):
    msg=""
    error=True
    val={}
    if request.META['HTTP_COOKIE']:
        if request.session['VIN']:
            
            qry_pre=Orders.objects.filter(user_id=request.session['VIN']).values()
            if len(qry_de)>0:
                msg="User Details"
                error=False
                val=list(qry_pre)
            else:
                msg="User Not Found"
        else:
            msg="Authentication Failed"
    else:
        msg="Session Expired!"

    return JsonResponse(msg=msg,error=error,data=val)

def qr_generate(request):
    msg=""
    error=True
    data=""
    if 'HTTP_COOKIE' in request.META:
        if request.GET:
            data=request.GET
            route=data['route']
            amt=data['amount'].split(',')
            tid=data['tid'].split(',')
            vid=request.session['VIN']
            print(data)
            typ=int(data['type'])
            fd=datetime.datetime.today()

            for i in range(0,len(tid)):
                qry_id=Users.objects.filter(vehicle_no=vid).values('id')
                s=str(amt[i])+'#'+vid+'#'+str(qry_id[0]['id'])
                qry_ins=Orders.objects.create(route=route,amount=amt[i],tollid=tid[i],status='PENDING',fdate=fd,user_id=vid,type=typ,orderid=s)
            my_QR = QR(data = s,pixel_size=3)
            my_QR.encode()
            name=my_QR.filename.split('/')
            qry_ins=Orders.objects.filter(orderid=s).update(filename=my_QR.filename)
            msg="Success"
            error=False
            data=name[3]
            os.system("sudo mv " + my_QR.filename + " /opt/lampp/htdocs/qrcodes/")
            url="http://192.168.31.111/qrcodes/"+name[3]
            print(url)
        else:
            msg="Parameter problem"
    else:
        msg="Wrong Parameters"
    # with open(my_QR.filename, "rb") as f:
    #   return HttpResponse(f.read(), content_type="image/jpeg")
    return JsonResponse({'msg':msg,'error':error,'url':url},safe=False)
    # q=pyqrcode.create('qr code')
    # q.png('qr.png',scale=6)
    # print('generated')

def qr_read(request):
    data_value=json.loads(request.body)
    print(data_value)
    my_QR = QR(filename = "/opt/lampp/htdocs/qrcodes/"+data_value['name'])

    # decodes the QR code and returns True if successful
    my_QR.decode()

    # prints the data
    return HttpResponse(my_QR.data)

