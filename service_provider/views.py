from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required #method base
from django.utils.decorators import method_decorator #class base

# def home(request):
#  return render(request, 'home.html')
class ProductView(View): 
 def get(self,request):
    homecleaning=Product.objects.filter(category='H')
    electric=Product.objects.filter(category='E')
    plambing=Product.objects.filter(category='P')
    carcare=Product.objects.filter(category='CS')
    painting=Product.objects.filter(category='HP')
    salon=Product.objects.filter(category='S')
    carpentry=Product.objects.filter(category='C')
    return render(request,'home.html',{'homecleaning':homecleaning, 'electric': electric, 'plambing':plambing, "carcare":carcare, "painting":painting ,"salon":salon,"carpentry":carpentry})



# def product_detail(request):
#  return render(request, 'productdetail.html')
class ProductDetailView(View):
    def get(self,request,id):
        product=Product.objects.get(id=id)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        
        return render(request,'productdetail.html',{'product':product,'item_already_in_cart':item_already_in_cart})
@login_required
def add_to_cart(request):
    user=request.user
    product_id =request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save() 
    return redirect('/cart')

@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=0.0
        total_amount=0.0
        cart_product= [p for p in Cart.objects.all() if p.user==user]
        # print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount =(p.quantity * p.product.discount_price )
                amount += tempamount
                total_amount = amount + shipping_amount
            return render(request, 'addtocart.html',{'carts':cart,'total_amount':total_amount,'amount':amount,'shipping_amount':shipping_amount})
        else:
            return render(request,'emptycart.html')



def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user) )
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount= 0.0
        cart_product= [p for p in Cart.objects.all() if p.user== request.user]
        for p in cart_product:
            tempamount =(p.quantity * p.product.discount_price )
            amount += tempamount 


        data ={
            'quantity': c.quantity,
            'amount':amount,
            'total_amount':amount + shipping_amount
            }    
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user) )
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount= 0.0
        cart_product= [p for p in Cart.objects.all() if p.user== request.user]
        for p in cart_product:
            tempamount =(p.quantity * p.product.discount_price )
            amount += tempamount
               


        data ={
            'quantity': c.quantity,
            'amount':amount,
            'total_amount':amount + shipping_amount
            }    
        return JsonResponse(data)

@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c =Cart.objects.get(Q(product=prod_id) & Q(user=request.user) )
        c.delete()
        amount = 0.0
        shipping_amount= 0.0
        cart_product= [p for p in Cart.objects.all() if p.user== request.user]
        for p in cart_product:
            tempamount =(p.quantity * p.product.discount_price )
            amount += tempamount

        data ={

            'amount':amount,
            'total_amount':amount + shipping_amount
            }    
        return JsonResponse(data)


def buy_now(request):
 return render(request, 'buynow.html')


# def address(request):
#     address = Customer.objects.filter(user=request.user)
#     return render(request, 'address.html',{'address':address,'active':'btn-primary'})
@login_required
def address(request):
    user=request.user
    address = Customer.objects.filter(user=user)
    return render(request, 'address.html',{'address':address,'active':'btn-primary'})

@login_required
def orders(request):
    op = OrderPlaced.objects.filter(user= request.user)
    return render(request, 'orders.html',{'order_place':op})

# def change_password(request):
#  return render(request, 'changepassword.html')

def mobile(request):
 return render(request, 'mobile.html')

def login(request):
 return render(request, 'login.html')

# def customerregistration(request):
#  return render(request, 'customerregistration.html')
class CustomerRegistrationView(View):
    def get(self,request):
        form =CustomerRegistrationForm()
        return render(request,'customerregistration.html',{'form':form})
    def post(self,request):
        form =CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulation ! Registration Successfully.')
            form.save()
        return render(request,'customerregistration.html',{'form':form})
        
@login_required
def checkout(request):
    user = request.user
    address = Customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 0.0
    total_amount = 0.0
    cart_product= [p for p in Cart.objects.all() if p.user== request.user]
    if cart_product:
        for p in cart_product:
            tempamount =(p.quantity * p.product.discount_price )
            amount += tempamount 
        total_amount = amount + shipping_amount
    return render(request, 'checkout.html',{'address':address,'amount':amount,'total_amount':total_amount,'cart_items':cart_items})

@login_required
# (class base)use this if user can directly accses profile page then it shows/redirect login page 
def payment_done(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customer.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect('orders') 



@method_decorator(login_required,name='dispatch')# (class base)use this if user can directly accses profile page then it shows/redirect login page 
class ProfileView(View):
  def get(self, request):
    form = CustomerProfileForm()
    return render(request,'profile.html',{'form':form,})
  def post(self, request):
    form = CustomerProfileForm()
    messages.success(request,"Congratulation!! Profile Updated Successfully.")
    return render(request,'profile.html',{'form':form,'active':'btn-primary'})
  def post(self,request):
    form= CustomerProfileForm(request.POST)
    if form.is_valid():
        # messages.success(request,'Congratulation ! Registration Successfully.')
        # form.save()
        user= request.user
        name= form.cleaned_data['name']
        locality= form.cleaned_data['locality']
        city= form.cleaned_data['city']
        state= form.cleaned_data['state']
        zipcode= form.cleaned_data['zipcode']
        reg=Customer(user=user,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
        reg.save()
        messages.success(request,"Congratulation!! Profile Updated Successfully.")
    return render(request,'profile.html',{'form':form,'active':'btn-primary'})
def about_us(request):
    return render(request,"about.html")


