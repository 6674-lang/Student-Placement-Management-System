from django.contrib import admin
from django.urls import path

from core import views


urlpatterns = [

    # Home
    path(
        "",
        views.home,
        name="home"
    ),

    # Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Students
    path(
        "students/",
        views.students,
        name="students"
    ),

    path(
        "students/<int:id>/",
        views.student_detail,
        name="student_detail"
    ),

    path(
        "students/<int:id>/edit/",
        views.edit_student,
        name="edit_student"
    ),

    path(
        "students/<int:id>/delete/",
        views.delete_student,
        name="delete_student"
    ),

    # Companies
    path(
        "companies/",
        views.companies,
        name="companies"
    ),

    path(
        "companies/<int:id>/edit/",
        views.edit_company,
        name="edit_company"
    ),

    path(
        "companies/<int:id>/delete/",
        views.delete_company,
        name="delete_company"
    ),
    path(
    "companies/add/",
    views.add_company,
    name="add_company"
),

    # Placements
    path(
        "placements/",
        views.placements,
        name="placements"
    ),

    path(
    "placements/add/",
    views.add_placement,
    name="add_placement"
    ),
    
path(
    "placements/edit/<int:id>/",
    views.edit_placement,
    name="edit_placement"
),

path(
    "placements/delete/<int:id>/",
    views.delete_placement,
    name="delete_placement"
),
path("login/", views.login_view, name="login"),
]



