from django.shortcuts import render, HttpResponse
from .models import Teacher, Student, Subject, Enrollment, Course
from django.contrib import messages
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

def HelloWorld(request):
    """
    A view that returns a simple "Hello World" response.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response with "Hello World" as the content.
    """
    return HttpResponse("Hello World")

def Registration(request):
    """
    Handles user registration.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response indicating the registration result.
    """
    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']
        name = request.POST['nameInput']
        surname = request.POST['surNameInput']
        photo = request.FILES.get('photoInput')

        if len(Student.objects.filter(Username=username)) > 0:
            error_message = "Username already exists"
            return render(request, 'registration.html', {'error_message': error_message})

        user = Student(Username=username, Password=password,
                       Name=name, Surname=surname, Photo=photo)

        user.save()

        return render(request, "registration.html", {"success_message": "User registered successfully"})

    return render(request, "registration.html")

def Login(request):
    """
    Handles user login.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response indicating the login result.
    """
    if request.method == "POST":
        username = request.POST['usernameInput']
        password = request.POST['passwordInput']

        try:
            teacher = Teacher.objects.get(Username=username, Password=password)
            request.session['username'] = teacher.Username
            request.session['currentRole'] = "t"
            return redirect("teacherBio")
        except:
            print("teacher login failed")

        try:
            student = Student.objects.get(Username=username, Password=password)

            request.session['username'] = student.Username
            request.session['currentRole'] = "s"
            return redirect("studentBio")
        except:
            print("student login failed")

        error_message = "Bad credentials"
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, "login.html")

def StudentBio(request):
    """
    Shows student information and links to other pages.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response with student information.
    """
    if request.session['currentRole'] == 's':
        username = request.session['username']
        student = Student.objects.get(Username=username)

        return render(request, "studentBio.html", {"user": student})
    else:
        return HttpResponse("Bad request")

def Subjects(request):
    """
    Shows a list of all subjects.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response with a list of subjects.
    """
    subjects = Subject.objects.all()
    return render(request, "subjects.html", {"subjects": subjects})

def MyCourses(request):
    """
    Shows courses that the student is enrolled in.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response with the student's enrolled courses.
    """
    username = request.session['username']
    if username:
        student = Student.objects.get(Username=username)
        enrollments = Enrollment.objects.filter(Student=student)
        courses = Course.objects.filter(enrollment__in=enrollments)
        return render(request, "myCourses.html", {"myCourses": courses})
    else:
        return HttpResponse("Bad request")

def AllCourses(request, subject_id):
    """
    Shows all courses related to a subject.

    Args:
        request: The HTTP request object.
        subject_id: The ID of the subject to display courses for.

    Returns:
        HttpResponse: A response with a list of courses related to the subject.
    """
    courses = Course.objects.filter(Subject__id=subject_id)
    subject = Subject.objects.get(id=subject_id)
    
    if request.method == 'POST':
        username = request.session['username']
        student = Student.objects.get(Username=username)
        course = Course.objects.get(id=request.POST["course_id"])

        try:
            enroll = Enrollment(Student=student, Course=course)
            enroll.save()
            success_message = f"Successfully enrolled to course {course.Name}"
            return render(request, 'allCourses.html', {'success_message': success_message, "courses": courses, "subject": subject})
        except:
            print("can't enroll")
            error_message = f"Can't enroll to course {course.Name}"
            return render(request, 'allCourses.html', {'error_message': error_message, "courses": courses, "subject": subject})
    else:
        return render(request, "allCourses.html", {"courses": courses, "subject": subject})

def SingleCourse(request, course_id):
    """
    Displays details of a single course.

    Args:
        request: The HTTP request object.
        course_id: The ID of the course to display.

    Returns:
        HttpResponse: A response with details of the course.
    """
    course = Course.objects.get(id=course_id)

    if request.method == 'POST':
        try:
            username = request.session['username']
            student = Student.objects.get(Username=username)
            course = Course.objects.get(id=course_id)

            enroll = Enrollment(Student=student, Course=course)
            enroll.save()
            success_message = f"Successfully enrolled to course {course.Name}"
            return render(request, 'course.html', {'success_message': success_message, "course": course})
        except:
            print("can't enroll")
            error_message = f"Can't enroll to course {course.Name}"
            return render(request, 'course.html', {'error_message': error_message, "course": course})

    return render(request, 'course.html', {"course": course})

def TeacherBio(request):
    """
    Displays teacher information.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response with teacher information.
    """
    if request.session['currentRole'] == 't':
        username = request.session['username']
        teacher = Teacher.objects.get(Username=username)

        return render(request, "teacherBio.html", {"user": teacher})
    else:
        return HttpResponse("Bad request")

def Teachers(request):
    """
    Displays a list of all teachers.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: A response with a list of teachers.
    """
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"teachers": teachers})

def SingleTeacher(request, teacher_id):
    """
    Displays details of a single teacher and the courses they teach.

    Args:
        request: The HTTP request object.
        teacher_id: The ID of the teacher to display.

    Returns:
        HttpResponse: A response with teacher information and their courses.
    """
    teacher = Teacher.objects.get(id=teacher_id)
    courses = Course.objects.filter(Teacher__id=teacher_id)
    return render(request, 'teacher.html', {"teacher": teacher, "courses": courses})

def TeachCourses(request, teacher_id):
    """
    Displays the courses taught by a specific teacher.

    Args:
        request: The HTTP request object.
        teacher_id: The ID of the teacher whose courses to display.

    Returns:
        HttpResponse: A response with a list of courses taught by the teacher.
    """
    teacher = Teacher.objects.get(id=teacher_id)
    courses = Course.objects.filter(Teacher=teacher)

    for course in courses:
        course.enrollment_count = Enrollment.objects.filter(
            Course=course).count()

    return render(request, "teachCourses.html", {"courses": courses, "teacher": teacher})
