from django.urls import path
from rims_form import views

app_name = "rims_form"
urlpatterns = [
    path('', views.home_page, name='homepage'),
    path('<int:pk>/', views.issues_detail, name="issue_detail"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('resolved/', views.resolved_issues, name='resolved'),
    path('dashboard/<int:pk>/', views.issues_detail, name="issue_detail"),
    path('<int:pk>/update/', views.issue_update, name='issue_update'),
    path('<int:pk>/delete/', views.issue_delete, name='issue_delete'),
    path('create/', views.issue_create, name='issue_create'), 

    # path('rimsform/', views.rims_form, name='rims_form')
]