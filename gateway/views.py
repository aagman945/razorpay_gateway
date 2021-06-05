import razorpay

from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import payments
from .forms import paymentForm
from .keyconfig import clientd
# Create your views here.
def home(request):
    return render(request,'home.html')

def donate(request):
    if request.method =='POST':
        form= paymentForm(request.POST)
        
        amount = int(request.POST['amount'])*100
        name = request.user
    
        # if form.is_valid():
        client = clientd
        response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
            
        order_id = response['id']
        order_status = response['status']
        

        if order_status == 'created':
                payment = payments(name=name,amount=amount,order_id=order_id)
                payment.save()
                context = {'response':response}
                return render(request,'donate.html',context)    

    else:
        form=paymentForm()
        return render(request,'donate.html',{'form':form})    
        
def logout(request):
    auth.logout(request)
    return redirect('/')

def success(request):
    return render(request,'success.html')

def transaction(request):
    transaction=payments.objects.filter(name=request.user).all()
    return render(request,'transaction.html',{'transaction':transaction})