from django.shortcuts import render, redirect,get_object_or_404
from loan_app.forms import LoanApplicationForm,SignUpForm
from loan_app.models import LoanApplication
from django.shortcuts import render, redirect
from loan_app.forms import LoanApplicationForm, BalanceSheetEntryForm
from loan_app.models import LoanApplication, BalanceSheetEntry
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
import json
# Create your views here.
# from app1.forms import ServiceRequestForm,SignUpForm
# from app1.models import ServiceRequest
from django.contrib.auth.decorators import login_required

def home(request):
    print("in home")
    return render(request , 'index.html' , context={"message":"Loan Application System"})

@login_required(login_url='login')
def loan_application(request):
    if request.method == 'POST':
        loan_form = LoanApplicationForm(request.POST)
        balance_sheet_form = BalanceSheetEntryForm(request.POST)
        if loan_form.is_valid(): #and balance_sheet_form.is_valid():
            loan_application = loan_form.save(commit=False)
            loan_application.user=request.user
            loan_application.save()
            balance_sheet_form.instance.loan_application = loan_application
            balance_sheet_form.save()
            print("balancesheet=",balance_sheet_form)
            pre_assessment = calculate_pre_assessment(loan_application)
            loan_application.pre_assessment=pre_assessment
            loan_application.save()
            print("pre=",pre_assessment)
            return redirect('application_success', pre_assessment=pre_assessment)
    else:
        loan_form = LoanApplicationForm()
        balance_sheet_form = BalanceSheetEntryForm()
    return render(request, 'application_form.html', {'loan_form': loan_form, 'balance_sheet_form': balance_sheet_form
                                                     })

@login_required(login_url='login')
def application_success(request, pre_assessment):
    print('in application_success',pre_assessment)
    return render(request, 'application_success.html', {'pre_assessment': pre_assessment})

def calculate_pre_assessment(loan_application):
    last_12_months_entries = BalanceSheetEntry.objects.filter(loan_application=loan_application).order_by('-year', '-month')[:12]
    profit_last_12_months = sum(entry.profit_or_loss for entry in last_12_months_entries if entry.profit_or_loss > 0)
    average_asset_value = sum(entry.assets_value for entry in last_12_months_entries) / len(last_12_months_entries)
    
    if profit_last_12_months > 0:
        if average_asset_value > loan_application.requested_loan_amount:
            return 100
        return 60
    
    return 20  

@login_required(login_url='login')
def requests_list(request):
    print("user:",request.user)
    if request.user.is_authenticated:
        user = request.user
        print("user after :",user)
        form = LoanApplicationForm()
        todos = LoanApplication.objects.filter(user = user).order_by('year_established')
        print("todos:",todos)
        return render(request , 'request.html' , context={'form' : form , 'todos' : todos})


def view_balance_sheet(request, id):
    loan_application = get_object_or_404(LoanApplication, pk=id)
    balance_sheet_entries = BalanceSheetEntry.objects.filter(loan_application=loan_application)
    return render(request, 'balance_sheet.html', {'loan_application': loan_application, 'balance_sheet_entries': balance_sheet_entries})

def balance_list(request):
    print("user:",request.user)
    if request.user.is_authenticated:
        user = request.user
        print("user after :",user)
        todos=[]
        form = BalanceSheetEntryForm()
        # todos = BalanceSheetEntry.objects.filter(user = user).order_by('year')
        # print("todos:",todos)
        loan_application = LoanApplication.objects.filter(user = user)
        todos=BalanceSheetEntry.objects.all()
        loan_application = get_object_or_404(LoanApplication, pk=loan_application_id)
        balance_sheet_entries = BalanceSheetEntry.objects.filter(loan_application=loan_application)
        for r in todos:
            r_ba=r.LoanApplication.objects.all()
            for a in r_ba:
                print("a=",a)
            print(r.id)
            print(r.__dict__)
        # print("loan application=",loan_application.id)
            # todo=(BalanceSheetEntry.objects.filter(id=4))
            # print(todo.__dict__)
            # todos.append(todo.__dict__)
            # todos.append(todo)
            # print(todos)
        # return HttpResponse("BalanceSheet")
        for t in todos:
            print("year=",t.__dict__)
        return render(request , 'balance_sheet.html' , context={'form' : form , 'todos' : todos})

def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                print("redirecting to home")
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )


# def signup(request):

#     if request.method == 'GET':
#         form = UserCreationForm()
#         print("form=",form)
#         context = {
#             "form" : form
#         }
#         return render(request , 'signup.html' , context=context)
#     else:
#         print(request.POST)
#         form = UserCreationForm(request.POST)  
#         context = {
#             "form" : form
#         }
#         if form.is_valid():
#             user = form.save()
#             print(user)
#             if user is not None:
#                 return redirect('login')
#         else:
#             return render(request , 'signup.html' , context=context)


def signup_custom(request):

    if request.method == 'GET':
        form = SignUpForm()
        print("form=",form)
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = SignUpForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print("user=",user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)



# @login_required(login_url='login')
# def add_todo(request):
#     if request.user.is_authenticated:
#         user = request.user
#         print(user)
#         form = ServiceRequestForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             todo = form.save(commit=False)
#             todo.user = user
#             todo.save()
#             print(todo)
#             return redirect("requests")
#         else: 
#             return render(request , 'index.html' , context={'form' : form})


def delete_balance_sheet(request , id ):
    print(id)
    LoanApplication.objects.get(pk = id).delete()
    return redirect('requests')

# def change_todo(request , id  , status):
#     todo = ServiceRequest.objects.get(pk = id)
#     todo.status = status
#     todo.save()
#     return redirect('home')

# def show_details(request , id ):
#     todo = ServiceRequest.objects.get(pk = id)
#     return render(request , 'details.html' , context={"todo":todo})

@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.method == 'GET':
        user = request.user
        print(user)
        # print("form\n",form)
        context={
            # "form":form,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "name":(user.first_name).upper()+" "+(user.last_name).upper(),
            "id":user.id,
            "email":user.email,
            "member_from":(user.date_joined).strftime('%Y-%m-%d %H:%M:%S'),
            # "m":user.date_joined,
            "username":user.username
                }
        # t=context['m']
        # print("m=",t,"\n",t.strftime('%Y-%m-%d %H:%M:%S'))
        return render(request , 'profile.html' , context=context)
    else:
        print("form=",request.POST)
        form = (request.POST)  
        print("first name=",form['first_name'])
        # user = {
        #     "form" : form
        # }
        
        user=request.user
        user.first_name=form['first_name']
        user.last_name=form['last_name']
        user.email=form['email']
        user.username=form['username']
        print("user in profile:",user)
        user.save()
        if user is not None:
            return redirect('profile')
        
@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        print("form=",request.POST)
        form = (request.POST)  
        print("first name=",form['first_name'])
        # user = {
        #     "form" : form
        # }
        
        user=request.user
        user.first_name=form['first_name']
        user.last_name=form['last_name']
        user.email=form['email']
        user.username=form['username']
        print("user in profile:",user)
        user.save()
        # if user is not None:
        return redirect('profile')
    else:
        print("in get edit profile")
        user = request.user
        print(user)
        # print("form\n",form)
        context={
            # "form":form,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "name":(user.first_name).upper()+" "+(user.last_name).upper(),
            "id":user.id,
            "email":user.email,
            "member_from":(user.date_joined).strftime('%Y-%m-%d %H:%M:%S'),
            # "m":user.date_joined,
            "username":user.username
                }
        return render(request , 'edit_profile.html' , context=context)





    