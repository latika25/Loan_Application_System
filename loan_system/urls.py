from django.contrib import admin
from django.urls import path, include
from django.urls import path
from loan_app.views import signup_custom,home,login,loan_application,application_success
urlpatterns = [
    path('admin/', admin.site.urls),
    path('loan/', include('loan_app.urls')),
    path('' , home , name='home' ),
]