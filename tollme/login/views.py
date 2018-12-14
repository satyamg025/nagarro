# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import hashlib
from django.shortcuts import render
import plivo
from django.http import HttpResponse,JsonResponse
import random
from .models import Users
# Create your views here.


def login(request):  #validates the user's VIN and if verified sends OTP to the RMN
	data={}
	error=True

	if(request.method == 'GET'):
		VIN=request.GET['VIN']
		qry_check_VIN_Exists=Users.objects.filter(vehicle_no=VIN).values('contact_no','vehicle_type')

		if qry_check_VIN_Exists.count()>0:
			otp=generate_otp(qry_check_VIN_Exists[0]['contact_no'])
			request.session['otp']=otp[0]
			request.session['mob_no']=otp[1]
			#print(request.session['otp'])
			request.session['VIN']=VIN
			request.session['vehicle_type']=qry_check_VIN_Exists[0]['vehicle_type']
			error=False
			msg="OTP Sent!"
		else:
			msg = "Vehicle Identification Number not Found!!"
	else:
		msg= "Request Not Identified!"
	data={'error':error,'msg':msg}	
	return JsonResponse(data)

def logout(request):
	
	request.session.clear()
	error = False
	msg = "Session deleted"
	data = {'error':error,'msg':msg}
	return JsonResponse(data)	



def generate_otp(mobile_no): #generates random otp of 6 characters
	data=[]
	mob_no=mobile_no
	otp=''
	
	characters2='0123456789'
	n2=6
	for i in range(0,n2):
		num2=random.randint(0,len(characters2)-1)
		otp=otp+characters2[num2]
	print(otp)
	otp_first=hashlib.sha1(otp).hexdigest()
	#print(otp_first)
	send_sms(otp,mob_no)
	data.append(otp_first)
	data.append(mob_no)
	return data
	

# def generate_token(mobile,VIN): #generate token of 30 characters
# 	token=''
# 	characters2='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# 	n2=30
# 	for i in range(0,n2):
# 		num2=random.randint(0,len(characters2)-1)
# 		token=token+characters2[num2]
# 	qry_store_token = VehicleDetails.objects.filter(mob_no=mobile).filter(vehicle_id=VIN).update(token=token)
# 	return token
			
			
def send_sms(text, phone_number):
	try:
		p = plivo.RestAPI('MAMZRJZMMWM2RLNTG2MD','ZWZlZTA2YTZkZjEzNmJjZmFmYjQyYTc3NGY0NDU4')
		params = {
			'src': 'TOLL-ME',
			'dst': '+91' + str(phone_number),
			'text': "Your OTP for Verification is: "+text
		}
		#print(params)
		p.send_message(params)
	except plivo.exceptions.PlivoRestError as e:
		print(e)




def checking_otp(request):
	error=True
	token=""
	if 'HTTP_COOKIE' in request.META:
		if request.method == 'GET':
			# if 'otp' in request.body:
			#incoming_data=request.body
			#i_data=json.loads(incoming_data)
			otp=request.GET['otp']#i_data['otp']
			#print(otp)
			otp=hashlib.sha1(otp).hexdigest()
			hashed_otp=request.session['otp']
			#print(hashed_otp)
			if otp == hashed_otp:
				error=False
				msg='OTP Matched!'
				request.session['otp']=""
				
			else:
				msg='Incorrect OTP!'
			# else:
			# 	msg="wrong parameters"
		else:
			msg='request invalid'
	else:
		msg = "Session Expired!"
	result={"error":error,"msg":msg}
	
	return JsonResponse(result)


def check_token(request):
	error=True
	if 'HTTP_COOKIE' in request.META:
		if(request.method == 'POST'):
			data=json.loads(request.body)
			token=data['token']
			qry_token_check=VehicleDetails.objects.filter(vehicle_id=request.session['VIN']).filter(mob_no=request.session['mob_no']).values('token')
			if(qry_token_check.count()>0):
				if(qry_token_check[0]['token'] == token):
					error=False
					msg="Token Matched!"
				else:
					msg="Mismatched token!"
			else:
				msg="User Not Found!"
		else:
			msg = "Invalid Request!"
	else:
		msg= 'Session Expired!'
	data={'error':error,'msg':msg}
	return JsonResponse(data)
