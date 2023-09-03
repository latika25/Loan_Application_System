# Loan_Application_System
Loan_Application_System using django
## To run the application through Docker use the following commands:
### pull the Docker image  
docker pull latika25/loan-application:0.1
### Start the container from this image
sudo docker run --publish 8000:8000  latika25/loan-application:0.1 

The Application contains the following functionalities:
1.SignUP
2.Login/Logout
3.Home Page
4.Apply for Loan Form
5. My Applications -> this contains all the applications by the user till now witht their Pre Assessment value given by Decesion Engine. This also gives the option to show the balance sheet and withdraw the appliation if any.
7. Balance Sheet Details Page
8. My Profile
9. Update the Profile 

