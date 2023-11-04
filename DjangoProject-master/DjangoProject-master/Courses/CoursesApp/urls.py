from django.urls import path
from . import views

urlpatterns = [
    path("", views.HelloWorld, name="home"), 
    path("registration/", views.Registration, name="registration"), 
    path("login/", views.Login, name="login"), 
    path("studentBio/", views.StudentBio, name="studentBio"), 
    path("teacherBio/", views.TeacherBio, name="teacherBio"), 
    path("subjects/", views.Subjects, name="subjects"),
    path("teachers/", views.Teachers, name="teachers"),
    path("teacher/<int:teacher_id>", views.SingleTeacher, name="teacher"),  
    path("myCourses/", views.MyCourses, name="myCourses"),
    path("allCourses/<int:subject_id>", views.AllCourses, name="allCourses"),
    path("course/<int:course_id>", views.SingleCourse, name="course"),
    path("teachCourses/<int:teacher_id>", views.TeachCourses, name="teachCourses")
]