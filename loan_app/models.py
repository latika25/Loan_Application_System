from django.db import models
from django.db import models
from django.contrib.auth.models import User


class LoanApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=100)
    year_established = models.PositiveIntegerField(default=None)
    requested_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    pre_assessment = models.IntegerField(default=20)
    

class BalanceSheetEntry(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_application = models.ForeignKey(LoanApplication, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    month = models.PositiveIntegerField()
    profit_or_loss = models.DecimalField(max_digits=10, decimal_places=2)
    assets_value = models.DecimalField(max_digits=10, decimal_places=2)
    

class LoanApplication2(models.Model):
    user = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    requested_loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    has_profit_last_12_months = models.BooleanField()
    average_asset_value = models.DecimalField(max_digits=10, decimal_places=2)
    pre_assessment = models.IntegerField(default=20)



# class ServiceRequest(models.Model):
#     status_choices = [
#     ('C', 'COMPLETED'),
#     ('P', 'PENDING'),
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     request_type = models.CharField(max_length=100)
#     details = models.TextField()
#     attachment = models.FileField(upload_to='service_request_attachments/', blank=True, null=True)
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     resolved_at = models.DateTimeField(null=True, blank=True)
#     status = models.CharField(max_length=20, default='Pending',choices=status_choices)


# class ServiceRequest1(models.Model):
#     status_choices = [
#     ('C', 'COMPLETED'),
#     ('P', 'PENDING'),
#     ]
#     priority_choices = [
#     ('1', '1️⃣'),
#     ('2', '2️⃣'),
#     ('3', '3️⃣'),
#     ('4', '4️⃣'),
#     ('5', '5️⃣'),
#     ('6', '6️⃣'),
#     ('7', '7️⃣'),
#     ('8', '8️⃣'),
#     ('9', '9️⃣'),
#     ('10', '🔟'),
#     ]
#     title = models.CharField(max_length=50)
#     status = models.CharField(max_length=2 , choices=status_choices)
#     user  = models.ForeignKey(User  , on_delete= models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     priority = models.CharField(max_length=2 , choices=priority_choices)