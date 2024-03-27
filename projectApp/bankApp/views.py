import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from .models import Customer, Account

def home(request):
    return HttpResponse('Bienvenidos a su banco Cash')

#----<----json-----<------Metodo getAllCustomer-------<-------Request-------<--------

def getAllCust(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        if not customers:
            return HttpResponseBadRequest('No existen clientes en la base de datos')
        dataList = []
        for i in customers:
            dataDict = {
                'Documento':i.ID,
                'Apellido':i.lName,
                'Nombre':i.fName,
                'email':i.email,
                'Telefono':i.phone,
                'password':i.passW
            }
            dataList.append(dataDict)
        dataJson = json.dumps(dataList)
        resp = HttpResponse()
        resp.headers['content-type'] = 'text/json'
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed('GET', 'Metodo no valido')
    
#----<----json-----<------Metodo getOneCustomer-------<-------Request-------<--------

def getOneCust(request, id):
    if request.method == 'GET':
        customer = Customer.objects.filter(ID = id).first()
        if not customer:
            return HttpResponseBadRequest('No existe cliente con esa cedula')
        accounts = Account.objects.all()
        dataList = []
        for e in accounts:
            data = {'cuentaNumero':e.accNumber, 'tipoCuenta':e.accType, 'Saldo':str(e.balance)}
            dataList.append(data)
        dataDict = {
            'Documento':customer.ID,
            'Apellido':customer.lName,
            'Nombre':customer.fName,
            'email':customer.email,
            'Telefono':customer.phone,
            'password':customer.passW,
            'Cuentas':dataList
        }
        print (dataDict)
        dataJson = json.dumps(dataDict)
        respuesta = HttpResponse()
        respuesta.headers['content-type'] = 'text/json'
        respuesta.content = dataJson
        return respuesta
    else:
        return HttpResponseNotAllowed('GET', 'Metodo no valido')
    
#---->----json----->------Metodo newCustomer------->-------Request------->--------
    
def newCust(request):
    if request.method == 'POST':
        try:
            datalist = json.loads(request.body)
            cust = Customer(
                ID = datalist['Documento'],
                lName = datalist['Apellido'],
                fName = datalist['Nombre'],
                email = datalist['email'],
                phone = datalist['Telefono'],
                passW = datalist['password']
                )
            cust.save()
            return HttpResponse('Cliente agregado satisfactoriamente')
        except:
            return HttpResponseBadRequest('Error en los datos enviados')
    else:
        return HttpResponseNotAllowed('POST', 'Metodo no valido')
    
#---->----json----->------Metodo upDateCustomer------->-------Request------->--------
    
def upDateCust(request, id):
    if request.method == 'PUT':
        try:
            customer = Customer.objects.filter(ID = id).first()
            if not customer:
                return HttpResponseBadRequest('No existe cliente con esa cedula')
            dataDict = json.loads(request.body)
            customer.ID = dataDict['Documento']
            customer.lName = dataDict['Apellido']
            customer.fName = dataDict['Nombre']
            customer.email = dataDict['email']
            customer.phone = dataDict['Telefono']
            customer.passW = dataDict['password']

            customer.save()
            return HttpResponse('Cliente actualizado')
        except:
            return HttpResponseBadRequest('Error en los datos enviados')
    else:
        return HttpResponseNotAllowed('PUT', 'Metodo no valido')
    
#-------------------------Metodo deleteCustomer------->-------Request------->--------
    
def deleteCust(request, id):
    if request.method == 'DELETE':
        try:
            cust = Customer.objects.filter(ID = id).first()
            if not cust:
                return HttpResponseBadRequest('No existe cliente con esa cedula')
            cust.delete()
            return HttpResponse('Cliente eliminado...')
        except:
            return HttpResponseBadRequest('Error en los datos enviados')
    else:
        return HttpResponseNotAllowed('DELETE', 'Metodo no valido')
    
#---->----json----->------Metodo newAccount------->-------Request------->--------
    
def newAcc(request):
    if request.method == 'POST':
        try:
            dataDict = json.loads(request.body)
            cust = Customer.objects.filter(ID = dataDict['userID']).first()
            if not cust:
                return HttpResponseBadRequest('No existe cliente con esa cedula')
            acc = Account(
                accNumber = dataDict['cuentaNumero'],
                accType = dataDict['tipoCuenta'],
                lastChangeDate = datetime.datetime.now(),
                custID = cust
            )

            acc.save()
            return HttpResponse('Nueva cuenta agregada')
        except:
            return HttpResponseBadRequest('Error en los datos enviados')
    else:
        return HttpResponseNotAllowed('POST', 'Metodo no valido')
    
#---->----json----->------Metodo upDateAccount------->-------Request------->--------
    
def upDateAcc(request, num):
    if request.method == 'PUT':
        try:
            acc = Account.objects.filter(accNumber = num).first()
            if not acc:
                return HttpResponseBadRequest('No existe numero de cuenta')
            dataDict = json.loads(request.body)
            acc.balance = dataDict['Saldo']
            acc.isActive = dataDict['Estado']

            acc.save()
            return HttpResponse('Cuenta actualizada')
        except:
            return HttpResponseBadRequest('Error en los datos enviados')
    else:
        return HttpResponseNotAllowed('PUT', 'Metodo no valido')
    
#---->----json----->------Metodo deleteAccount------->-------Request------->--------
    
def deleteAcc(request, num):
    if request.method == 'DELETE':
        try:
            acc = Account.objects.filter(accNumber = num).first()
            if not acc:
                return HttpResponseBadRequest('No existe el numero de cuenta')
            acc.delete()
            return HttpResponse('Cuenta eliminada')
        except:
            return HttpResponseBadRequest('Error en los datos enviados') 
    else: 
        return HttpResponseNotAllowed('DELETE', 'Metodo no valido')