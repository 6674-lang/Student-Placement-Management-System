from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Student, Company, Placement
# ==========================================
# LOGIN
# ==========================================

def login_view(request):
    
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        role = request.POST.get("role")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            # STAFF LOGIN
            if role == "Staff":

                if user.is_staff:

                    login(request, user)
                    return redirect("home")

                else:

                    return render(
                        request,
                        "login.html",
                        {
                            "error": "This account is not a Staff account"
                        }
                    )

            # STUDENT / PARENT LOGIN
            else:

                login(request, user)

                return redirect("home")

        else:

            return render(
                request,
                "login.html",
                {
                    "error": "Invalid ID or Password"
                }
            )

    return render(
        request,
        "login.html"
    )


# ==========================================
# HOME
# ==========================================

def home(request):

    total_students = Student.objects.count()
    total_companies = Company.objects.count()
    placed_students = Student.objects.filter(
        placed=True
    ).count()

    return render(
        request,
        "home.html",
        {
            "total_students": total_students,
            "total_companies": total_companies,
            "placed_students": placed_students,
        }
    )


# ==========================================
# STUDENTS
# ==========================================

def students(request):

    students = Student.objects.all()

    return render(
        request,
        "students.html",
        {
            "students": students
        }
    )


# ==========================================
# STUDENT DETAIL
# ==========================================

def student_detail(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    return render(
        request,
        "student_detail.html",
        {
            "student": student
        }
    )


# ==========================================
# EDIT STUDENT
# ==========================================

def edit_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.department = request.POST.get("department")
        student.cgpa = request.POST.get("cgpa")
        student.skills = request.POST.get("skills")

        if request.POST.get("placed") == "on":
            student.placed = True
        else:
            student.placed = False

        student.save()

        return redirect("students")

    return render(
        request,
        "student_edit.html",
        {
            "student": student
        }
    )


# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student(request, id):

    student = get_object_or_404(
        Student,
        id=id
    )

    student.delete()

    return redirect("students")


# ==========================================
# COMPANIES
# ==========================================

def companies(request):

    companies = Company.objects.all()

    return render(
        request,
        "companies.html",
        {
            "companies": companies
        }
    )


# ==========================================
# ADD COMPANY
# ==========================================

def add_company(request):

    if request.method == "POST":

        company = Company()

        company.name = request.POST.get("name")
        company.location = request.POST.get("location")
        company.role = request.POST.get("role")
        company.package = request.POST.get("package")

        company.save()

        return redirect("companies")

    return render(
        request,
        "add_company.html"
    )


# ==========================================
# EDIT COMPANY
# ==========================================

def edit_company(request, id):

    company = get_object_or_404(
        Company,
        id=id
    )

    if request.method == "POST":

        company.name = request.POST.get("name")
        company.location = request.POST.get("location")
        company.role = request.POST.get("role")
        company.package = request.POST.get("package")

        company.save()

        return redirect("companies")

    return render(
        request,
        "edit_company.html",
        {
            "company": company
        }
    )


# ==========================================
# DELETE COMPANY
# ==========================================

def delete_company(request, id):

    company = get_object_or_404(
        Company,
        id=id
    )

    company.delete()

    return redirect("companies")


# ==========================================
# PLACEMENTS
# ==========================================

def placements(request):

    placement_list = Placement.objects.select_related(
        "student",
        "company"
    ).all()

    return render(
        request,
        "placements.html",
        {
            "placements": placement_list
        }
    )


# ==========================================
# ADD PLACEMENT
# ==========================================

def add_placement(request):
    
    students = Student.objects.all()
    companies = Company.objects.all()

    if request.method == "POST":

        student_id = request.POST.get("student")
        company_id = request.POST.get("company")
        job_role = request.POST.get("job_role")
        package = request.POST.get("package")
        placement_date = request.POST.get("placement_date")

        # Create placement
        Placement.objects.create(
            student_id=student_id,
            company_id=company_id,
            job_role=job_role,
            package=package,
            placement_date=placement_date
        )

        # Mark student as placed
        student = get_object_or_404(
            Student,
            id=student_id
        )

        student.placed = True
        student.save()

        return redirect("placements")

    return render(
        request,
        "add_placement.html",
        {
            "students": students,
            "companies": companies
        }
    )
# ==========================================
# EDIT PLACEMENT
# ==========================================

def edit_placement(request, id):

    placement = get_object_or_404(
        Placement,
        id=id
    )

    students = Student.objects.all()
    companies = Company.objects.all()

    if request.method == "POST":

        placement.student_id = request.POST.get("student")
        placement.company_id = request.POST.get("company")
        placement.job_role = request.POST.get("job_role")
        placement.package = request.POST.get("package")
        placement.placement_date = request.POST.get("placement_date") or None

        placement.save()

        return redirect("placements")

    return render(
        request,
        "edit_placement.html",
        {
            "placement": placement,
            "students": students,
            "companies": companies
        }
    )


# ==========================================
# DELETE PLACEMENT
# ==========================================

def delete_placement(request, id):

    placement = get_object_or_404(
        Placement,
        id=id
    )

    placement.delete()

    return redirect("placements")


