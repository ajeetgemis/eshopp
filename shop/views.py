from onlinedemo.settings import ROZERPAY_ID,ROZERPAY_ACC_ID
from django.shortcuts import render,HttpResponseRedirect,redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models.product import products,categories
from .models.category import categories
from .models.cartmodel import cartmodel
from .models.register import registermodel
from django.contrib.auth.hashers import make_password,check_password
from django .db.models import Q
from django.contrib import sessions
from django .views import View
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay
from  .models.orders import orders
import random

orderid=random.randint(100000,10000000)


# Create your views here.
class orders_status(View):
    def get(self,request):
        ip=request.META.get('BASE_DIR')
        print(ip)
        return render(request,'orders.html')
class checkoutcart(View):
    def post(self,request):
        email=request.POST.get('email')
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        pnumber=request.POST.get('pnumber')
        print(email,address2,address1,pnumber)
        cart=request.session.get('cart')
        print(cart)
        print("keys are",list(cart.keys()))
        customer=request.session.get('customer_email')
        print(customer)
        print("####################")
        emailreg=registermodel.objects.get(email=email)
        print("emailreg",emailreg.email)
        prd=products.objects.filter(id__in=list(cart.keys()))
        if customer!=email:
            error_message="Your Email address are different"
            return render(request,'showcart.html',{'msg':error_message})
        else:

            for prod in prd:
                print(prod.id)
                print("qty",cart.get(prod.id))
                
                cm=cartmodel(customer=emailreg,
                product=prod,
                quantity=cart.get(str(prod.id)),
                price=prod.p_price,
                address1=address1,
                address2=address2,
                phonenumber=pnumber,
                )
                cm.save()
            request.session['cart']={}    
            return redirect('showcart')
    
class showcart(View):
    def get(self,request):
        session_email=request.session.get('customer_email')
        listvalue=list(request.session.get('cart'))
        print(listvalue)
        qset=products.objects.filter(id__in=listvalue)
        print(qset)
        return render(request,'showcart.html',{'product':qset,'email':session_email})

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('/')
def addto_cart(request):
    
    p_id=request.GET.get('prod_id')
    print("p_id",p_id)
    cart=request.session.get('cart')
    if cart:
        qty=cart.get(p_id)

       # print(qty)
        if qty:
            cart[p_id]=qty+1
            #print(qty)
        else:
            cart[p_id]=1    
    else:

        cart={}
        cart[p_id]=1

    request.session['cart']=cart
    print(request.session['cart'])
    return redirect('/')

        
        
def login_customer(request):
    if request.method=='POST':
        email=request.POST.get('email')
        print(email)
        password=request.POST.get('password')
        cust=registermodel.objects.get(email=email)
        
        if cust:
            print("success")
            message="success"
            flag=check_password(password,cust.password)
            if flag:
                request.session['customer_id']=cust.id
                request.session['customer_email']=cust.email
                print("you are:",request.session.get('customer_id'))
                print("you are:",request.session.get('customer_email'))
              #  print("you are:",request.session.META('customer_email'))
                
                
                return render(request,'signup.html',{'loginmsg':message})
        else:    
            return render(request,'signup.html',{'loginmsg':'invalid email or password'})
    return render(request,'login.html')    
def registe_customer(request):
    if request.method=='POST':  

        print("post request")
        email=request.POST.get('email')
        password=make_password(request.POST.get('password'))
        address1=request.POST.get('address1')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        print(email)
        if registermodel.objects.filter(email=email):
            error_message="Email Already Exists"
            return render(request,'signup.html',{'errmsg':error_message})
           
        regobj=registermodel(email=email,password=password,address1=address1,address2=address2,city=city)
        
        regobj.save()
        return render(request,'signup.html',{'msg':'Register Successfully......'})
    print(make_password('12345'))
    return render(request,'signup.html')
def index1(request,id=None):
   # request.session.clear()#.all session clear
    
    print(id)
    if id is not None:
        qset=products.objects.filter(p_category=id)
        print(qset)
        return render(request,'base.html',{'value':qset})

    qset=products.objects.all()
    cset=categories.objects.all()
    print(qset)
    return render(request,'base.html',{'value':qset,'category':cset})
def rozerpayment(request):
    if request.method=="POST":
        #product_cart=[p for p in cartmodel.objects.all]
        #print("all cart items",product_cart)
        customer=registermodel.objects.get(email=request.session.get('customer_email'))
        print("CUSTOMER NAME",customer)
        cartvalue=cartmodel.objects.get()
        total=cartmodel.objects.all()
        print("cart_items",total)
        total_price=0
        for pri in total:
            print(pri.price)
            total_price+= pri.price
        print(total_price)
        print("request for payment")
        callback_url="http://127.0.0.1:8000/handelrequestpaytm/"
        print(callback_url)
        amount=total_price
        order_id="bhjbhjb1234"
        currency="INR"
        phone_number="7041100397"
        email="ajeetchoudhary537@gmail.com"
       # print(settings.ROZERPAY_ID)
        roz_client=razorpay.Client(auth=(ROZERPAY_ID,ROZERPAY_ACC_ID))
        print("rozer auth",roz_client)        
        print(ROZERPAY_ID)
        rozerclinetorder=roz_client.order.create({'payment_capture':'0','receipt':order_id,'amount':amount,'currency':'INR'})
        print(rozerclinetorder['id'])
        request.session['order_id']=rozerclinetorder['id']
        createorder=orders.objects.create(customer=customer,order_items=cartvalue,total_price=amount,order_id=rozerclinetorder['id'])
        createorder.save()
        return render(request,'orders.html',{'callback_url':callback_url,'rozerobj':rozerclinetorder['id'],'api_key':ROZERPAY_ID})
    
@csrf_exempt
def handelrequestpaytm(request):
    if request.method=="POST":
        razorpay_paymen=request.POST.get('razorpay_payment_id')
        print(request.POST.get('razorpay_order_id'))
        razorpay_signature=request.POST.get('razorpay_signature')
        order_id=request.POST.get('razorpay_order_id')
        print(order_id)
       # alert(response.razorpay_signature)
        print("###########")
        print(request.session.get('order_id'))
        rozerupdate=orders.objects.get(order_id=request.session.get('order_id'))
        rozerupdate.payment_status=True
        rozerupdate.razorpay_payment_id=razorpay_paymen
        rozerupdate.razorpay_signature=razorpay_signature
        rozerupdate.save()
        #qset=cartmodel.objects.all()
        #qset.delete()
        request.session.clear()

        return render(request,'success.html')