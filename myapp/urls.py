from django.urls import path,include
from . import views
urlpatterns = [
    #===== Condidate Side and Company Side url =====#
    path('', views.homePage, name="homepage"),
    path('signup/', views.signupPage, name="signup"),
    path('register/', views.registerUser, name="register"),
    path('otppage/', views.otpPage, name="otppage"),
    path('otp/', views.otpVerify, name="otp"),
    path('loginpage/', views.loginPage, name="loginpage"),
    path('loginuser/', views.loginUser, name="login"),

    #======= Condidate Side url =====    
    path('index', views.indexpage, name="index"),    
    path('profile/<int:pk>', views.profilePage, name="profile"),
    path('updateprofile/<int:pk>', views.updateProfile, name="updateprofile"),
    path('joblist/', views.condidateJobListPage, name="joblist"),
    path('apply/<int:pk>', views.applyPage, name="apply"),
    path('applyjob/<int:pk>', views.applyJob, name="applyjob"),
    path('applyjoblist/', views.jobApplyList, name="applyjoblist"),
    path('condidatelogout/', views.condidateLogout, name="condidatelogout"),


    #============= Company side url ================#
    path('companyindex/', views.companyIndexPage, name="companyindex"),
    path('companyprofile/<int:pk>', views.companyProfilePage, name="companyprofile"),
    path('updatecompanyprofile/<int:pk>', views.updateCompanyProfile, name="updatecompanyprofile"),
    path('jobpostpage/', views.jobPostPage, name="jobpostpage"),
    path('jobpost/<int:pk>', views.jobDetailSubmit, name="jobpost"),
    path('jobpostlistpage/', views.jobListPage, name="jobpostlistpage"),
    path('companylogout/', views.companyLogout, name="companylogout"),
    #============= END ================#

    #============-Admin side-==========#
    path('adminloginpage/',views.adminLoginPage, name='adminloginpage' ),
    path('adminindex/', views.adminIndexPage, name="adminindexpage"),
    path('adminlogin/', views.adminLogin, name="adminlogin"),
    path('adminuserlist/', views.adminUserList, name="userlist"),
    path('admincompanylist', views.adminCompanyList, name="companylist"),
    path('deleteuser/<int:pk>', views.userDelete, name="deleteuser"),
    path('deletecompany/<int:pk>', views.companyDelete, name="deletecompany"),
    path('verifypage/<int:pk>', views.verifyCompanyPage, name="verifypage"),
    path('verify/<int:pk>', views.verifyCompany, name="verify"),

    

    

    

    

    

    



    ###===only for rough url===###
    path('show/', views.show, name="show"),
    ###===endrough===###
]