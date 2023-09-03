from django.urls import path
# from . import views
from django.contrib import admin
from django.urls import path
from loan_app.views import signup_custom,home,login,view_balance_sheet,delete_balance_sheet,edit_profile,balance_list,loan_application,application_success,requests_list,signout,profile

urlpatterns = [
    # path('apply/', views.loan_application, name='loan_application'),
    # path('success/', views.application_success, name='application_success'),
     path('' , home , name='home' ), 
   path('login/' ,login  , name='login'),
   path('application/',loan_application,name='application'), 
   path('application_success/<int:pre_assessment>',application_success,name='application_success'), 
   path('profile/' ,profile  , name='profile'), 
   path('edit/' ,edit_profile , name='edit_profile'), 
   path('signup/' , signup_custom ), 
   path('requests/' , requests_list,name='requests' ), 
   path('balance_sheet/' , balance_list,name='balance_sheet' ), 
   path('requests/show_balance_sheet/<int:id>/',view_balance_sheet,name='view_balance_sheet'),
   path('requests/delete_balance_sheet/<int:id>/',delete_balance_sheet,name='view_balance_sheet'),
#    path('add-todo/' , add_todo ), 
#    path('delete-todo/<int:id>' , delete_todo ), 
#    path('show_details/<int:id>' , show_details ), 
#    path('change-status/<int:id>/<str:status>' , change_todo ), 
   path('logout/' , signout ), 
]





