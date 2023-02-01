from django.shortcuts import render, redirect
from .models import *

from random import randint  #this randint fuction use for otp


# Create your views here.

#--HOME PAGE--#
def homePage(request):
    return render(request, "index.html")


#==========- Condidate and Company -==========#
def signupPage(request):
    return render(request, "app/signup.html", {})

def registerUser(request):
    #--------------------register for condidate----------------#
    if request.POST['role']=="Condidate":
        role=request.POST['role']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        #check for alredy register or not
        user=UserMaster.objects.filter(Email=email)

        if user:
            message='user already exist'
            return render(request, "app/signup.html", {'msg':message})
         
        else:
            if password == cpassword:
                otp=randint(100000,999999)
                newuser=UserMaster.objects.create(role=role, Otp=otp, Email=email, Password=password)
                newcand=Condidate.objects.create(user_id=newuser, Firstname=fname, Lastname=lname)

                return render(request, "app/otpverify.html",{'email':email})

            else:
                message="password not match"
                return render(request, "app/signup.html", {'msg':message})

    #-------------- register for company---------------#
    elif request.POST['role']=='Company':
        role=request.POST['role']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        newcom = UserMaster.objects.filter(Email=email)
        if newcom:
            message="company already registered"
            return render(request, "app/signup.html", {'msg':message})

        else:
            if password == cpassword:
                otp=randint(100000,999999)  #otp genrate
                newuser=UserMaster.objects.create(role=role, Otp=otp, Email=email, Password=password)
                newcomp=Company.objects.create(user_id=newuser, Firstname=fname, Lastname=lname)

                return render(request, "app/otpverify.html",{'email':email})
            else:
                message="password not match"
                return render(request, "app/signup.html", {'msg':message})

    else:
        message="select role"
        return render(request, "app/signup.html", {'msg':message})


    #==========OTP Section=========#
def otpPage(request):
    return render(request, "app/otpverify.html")

def otpVerify(request):
    email=request.POST['email']
    otp=int(request.POST['otp'])
    user=UserMaster.objects.get(Email=email)    
    if user:
        if user.Otp==otp:
            message="otp verify successfully"
            return render(request,"app/login.html", {'msg':message})
        else:
            message="otp is incorrect"
            return render(request, "app/otpverify.html", {'msg':message})

    else:
        return render(request, "app/signup.html",{})
          #------=End otp=------#

    
    #=====----login part----=====#
def loginPage(request):
    return render(request, "app/login.html")

def loginUser(request):
    #------------login for condidate-------------#
    if request.POST['role']=="Condidate":
        email=request.POST['email']
        password=request.POST['password']

        #checking
        try:
            user=UserMaster.objects.get(Email=email)
        except UserMaster.DoesNotExist:
            user=None
             
        if user:
            if user.Password == password and user.role=='Condidate':
                #take data in session from table
                can = Condidate.objects.get(user_id=user)
                request.session['id']=user.id
                request.session['role']=user.role
                request.session['firstname']=can.Firstname
                request.session['lastname']=can.Lastname
                request.session['email']=user.Email
                
                #retrun index page
                return redirect('index')
            
            else:
                message="password does not match"
                return render( request, "app/login.html",{'msg':message})

        else:
            message="user doesnot exist"
            return render(request, "app/login.html",{'msg':message})

    #============login for company==========#
    elif request.POST['role']=='Company':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user=UserMaster.objects.get(Email=email)
        except UserMaster.DoesNotExist:
            user=None

        if user:   #checking in database email exist or not
            if user.Password == password:

                #taking data in session
                comp=Company.objects.get(user_id=user)

                request.session['id']=user.id
                request.session['role']=user.role
                request.session['firstname']= comp.Firstname
                request.session['lastname']=comp.Lastname
                request.session['email']=user.Email
                request.session['password']=user.Password

                return redirect('companyindex')
                
            else:
                message="password incorrect"
                return render(request, "app/login.html",{'msg':message})
            
        else:
            message="company does not exit"
            return render(request, "app/login.html",{'msg':message})

    else:
        message="select role"
        return render(request, "app/login.html",{'msg':message})
        
            #----------=End login part=-------------#

#===============-END-================#



#==========- Condidate Side -==========#
def indexpage(request):
    return render(request,"app/index.html")

   #-----=profile views =-----#
def profilePage(request,pk):
    if pk:
        user=UserMaster.objects.get(pk=pk)
        can=Condidate.objects.get(user_id=user)
    return render(request, "app/profile.html",{'user':user, 'can':can}) 


   #-----=update condidate profile=-----#
def updateProfile(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user.role== 'Condidate':
        can=Condidate.objects.get(user_id=user)
        can.Country = request.POST['country']
        #can['State']=request.POST['country']
        can.City=request.POST['city']
        can.min_salary=request.POST['minimums']
        can.max_salary=request.POST['maximums']
        can.job_type=request.POST['jobtype']
        can.job_cotegory=request.POST['category']
        can.highest_edu=request.POST['education']
        can.Exprience=request.POST['exprience']
        can.Website=request.POST['website']
        can.Shift=request.POST['shift']
        can.Jobdescription=request.POST['jobdescription']
        can.Contact=request.POST['contact']
        can.Gender=request.POST['gender']
        can.Profile_pic=request.FILES['image']#use "FILES" instead of "POST" because 
                                              #we take image of any files document

        can.save()
        #formating url(for passing key with url)
        url = f'/profile/{pk}'
        return redirect(url)
        #===END===#

    #-----=Job Apply=-----#
def applyPage(request,pk):  #here pk use to access jobdetails model
    user=request.session['id']
    if user:
        cand=Condidate.objects.get(user_id=user)
        job=JobDetail.objects.get(id=pk)

    return render(request, "app/apply.html", {'user':user, 'cand':cand, 'job':job})

def applyJob(request,pk):
    user=request.session['id']
    if user:
        cand=Condidate.objects.get(user_id=user)
        job=JobDetail.objects.get(id=pk)
        minsalary=request.POST['minimums']
        maxsalary=request.POST['minimums']
        gender=request.POST['gender']
        website=request.POST['website']
        resume=request.FILES['resume']

        newapply=ApplyList.objects.create(
            Condidate=cand,
            Job=job,
            website=website,
            Min_salary=minsalary,
            Max_salary= maxsalary,
            Gender=gender,
            Resume=resume,

        )
        message = "apply done"
        return render(request, "app/apply.html", {'msg':message})

    #---Job List Show---#
def condidateJobListPage(request):
    all_job=JobDetail.objects.all()
    return render(request, "app/job-list.html",{'all_job':all_job} )

#===============-END-================#




#==========-company side-==========#
def companyIndexPage(request):
    return render(request, "app/company/index.html")

def companyProfilePage(request,pk):
    user=UserMaster.objects.get(pk=pk)
    comp=Company.objects.get(user_id=user)
    return render(request, "app/company/profile.html",{'user':user, 'comp':comp})
    
    #----Update----#
def updateCompanyProfile(request,pk):
    user=UserMaster.objects.get(pk=pk)
    if user.role=="Company":
        comp=Company.objects.get(user_id=user)
        comp.Firstname=request.POST['firstname']
        comp.Lastname=request.POST['lastname']
        comp.Company_name=request.POST['companyname']
        comp.State=request.POST['state']
        comp.City=request.POST['city']
        comp.Contact=request.POST['contact']
        comp.Address=request.POST['address']
        comp.Website=request.POST['website']
        comp.Description=request.POST['description']
        comp.Logo_pic=request.FILES['image'] #use FILES instead of POST because we take image
        comp.save()

        url = f"/companyprofile/{pk}" #formating url to redirect because we gave extra value "pk" with "url"
        return redirect(url)


    #---Job Post Form---#
def jobPostPage(request):
    return render(request, "app/company/jobpost.html")

def jobDetailSubmit(request, pk):
    user=UserMaster.objects.get(id=pk)

    if user.role=="Company":
        comp=Company.objects.get(user_id=user)

        Job_name=request.POST['jobname']
        Company_name=request.POST['companyname']
        Company_address=request.POST['companydaddress']
        Job_description=request.POST['jobdescription']
        Qualification=request.POST['qualification']
        Responsibilities=request.POST['responbilities']
        Location=request.POST['location']
        Company_website=request.POST['companywebsite']
        Company_email=request.POST['companyemail']
        Company_contact=request.POST['companycontact']
        Salary_package=request.POST['salarypackage']
        Experience=request.POST['experience']
        companylogo=request.FILES['image']

        newuser=JobDetail.objects.create(

        company_id=comp,
        Job_name=Job_name,
        Company_name=Company_name,
        Company_address=Company_address,
        Job_description=Job_description,
        Qualification=Qualification,
        Responsibilities=Responsibilities,
        Location=Location,
        Company_website=Company_website,
        Company_email=Company_email,
        Company_contact=Company_contact,
        Salary_package=Salary_package,
        Experience=Experience,
        Comapany_logo=companylogo,
        )

        message="job post successFully"
        return render(request, "app/company/jobpost.html", {'msg':message})

    #-----joblist show----#
def jobListPage(request):
    all_job=JobDetail.objects.all()
    return render(request, "app/company/jobpostlist.html", {'all_job':all_job})
    
    #------apply list show------#
def jobApplyList(request):
    all_jobapply=ApplyList.objects.all()
    return render(request, "app/company/jobapplylist.html", {'all_job':all_jobapply})
#===============-END-================#



#====- logout -====#
    #------condidate logout-------#
def condidateLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('homepage')

#------company logout-------#
def companyLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('homepage')
#------END-------#

      #====- END -====#


#============-Admin side-==========#
def adminLoginPage(request):
    return render(request, "app/admin/login.html")

def adminIndexPage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request, "app/admin/index.html")
    else:
        return redirect('adminloginpage')

def adminLogin(request):
    username=request.POST['username']
    password=request.POST['password']

    if username == "admin" and password == "admin":#give admin creditential
        request.session['username']=username
        request.session['password']=password
        return redirect('adminindexpage')

    else:
        message="user name and password does not match"
        return render(request, "app/admin/login.html", {'msg':message})

def adminUserList(request):
    all_user=UserMaster.objects.filter(role='Condidate')
    return render(request,"app/admin/userlist.html", {'all_user': all_user})

def adminCompanyList(request):
    all_company=UserMaster.objects.filter(role='Company')
    return render(request,"app/admin/companylist.html", {'all_company': all_company})

def userDelete(request, pk):
    user= UserMaster.objects.get(id=pk)
    user.delete()
    return redirect('userlist')

def companyDelete(request, pk):
    user= UserMaster.objects.get(id=pk)
    user.delete()
    return redirect('companylist')

def verifyCompanyPage(request,pk):
    company=UserMaster.objects.get(id=pk)
    if company:
        return render(request, "app/admin/verify.html", {'company':company})

def verifyCompany(request,pk):
    company=UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified=request.POST.get('verify')
        return redirect('companylist')
 


  
  
 #===============-END-================#


        

            






