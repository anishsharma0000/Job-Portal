from django.db import models

# Create your models here.
class UserMaster(models.Model):
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=50)
    Otp=models.IntegerField()
    role=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_created=models.DateTimeField(auto_now_add=True)
    is_updated=models.DateTimeField(auto_now_add=True)




class Condidate(models.Model):
    user_id=models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Address=models.CharField(max_length=200)
    Dob=models.CharField(max_length=50)
    Gender=models.CharField(max_length=50)
    min_salary=models.BigIntegerField(default=0)
    max_salary=models.BigIntegerField(default=0)
    job_type=models.CharField(max_length=150, default="")
    job_cotegory=models.CharField(max_length=150, default="")
    Country=models.CharField(max_length=50, default="")
    highest_edu=models.CharField(max_length=150, default="")
    Exprience=models.CharField(max_length=150, default="")
    Website=models.CharField(max_length=150, default="")
    Shift=models.CharField(max_length=150, default="")
    Jobdescription=models.CharField(max_length=500, default="")
    Profile_pic=models.ImageField(upload_to="myapp/img/condidate")

    def __str__(self):
        return self.Firstname


class Company(models.Model):
    user_id=models.ForeignKey(UserMaster, on_delete=models.CASCADE)
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Company_name=models.CharField(max_length=150)
    State=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Contact=models.CharField(max_length=50)
    Address=models.CharField(max_length=200)
    Website=models.CharField(max_length=200, default="")
    Description=models.CharField(max_length=500, default="")
    Logo_pic=models.ImageField(upload_to="myapp/img/company")

    def __str__(self):
        return self.Firstname



class JobDetail(models.Model):
    company_id=models.ForeignKey(Company, on_delete=models.CASCADE)
    Job_name=models.CharField(max_length=150)
    Company_name=models.CharField(max_length=150)
    Company_address=models.CharField(max_length=250)
    Job_description=models.TextField(max_length=500)
    Qualification=models.CharField(max_length=250)
    Responsibilities=models.CharField(max_length=250)
    Location=models.CharField(max_length=250)
    Company_website=models.CharField(max_length=150)
    Company_email=models.CharField(max_length=150)
    Company_contact=models.CharField(max_length=20)
    Salary_package=models.CharField(max_length=250)
    Experience=models.IntegerField()
    Comapany_logo=models.ImageField(upload_to="myapp/img/company")

    def __str__(self):
        return self.Job_name



class ApplyList(models.Model):
    Condidate=models.ForeignKey(Condidate, on_delete=models.CASCADE)
    Job=models.ForeignKey(JobDetail, on_delete=models.CASCADE)
    website=models.CharField(max_length=150)
    Min_salary=models.CharField(max_length=100)
    Max_salary=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100)
    Resume=models.FileField(upload_to="app/resume")

