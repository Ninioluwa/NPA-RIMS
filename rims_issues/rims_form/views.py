from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views import generic
from .models import IssuesModel, Branch
from .forms import RimsForm, RimsModelForm, CustomUserCreationForm

# Create your views here.



def home_page(request):
    
    return render(request, 'index.html', {})

def dashboard(request):
    issues = IssuesModel.objects.all()

    # lagos_list = IssuesModel.objects.filter(port__)
    # lagos_issues = IssuesModel.objects.filter(port_id=1)

    context = {
        'issues': issues,
        # 'lagos_issue': lagos_issues
    }

    return render(request, 'dashboard.html', context)

def issues_detail(request, pk):
    issue = IssuesModel.objects.get(id=pk)

    context = {
        'issue': issue
    }
    return render(request, "issues_detail.html", context)

def rims_form(request):
    issues = IssuesModel.objects.all()
    context = {
        'issues': issues
    }
    return render(request, 'issues_form.html', context)
    # return render(request, 'index.html', context) 

def issue_create(request):
    form = RimsForm()
    if request.method == "POST":
        print("iNCOMING post request")
        form = RimsForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            subject = form.cleaned_data['subject']
            status = form.cleaned_data['status']
            sen_no = form.cleaned_data['sen_no']
            issues = form.cleaned_data['issues']
            port = Branch.objects.first()
            IssuesModel.objects.create(
                subject=subject,
                status=status,
                sen_no=sen_no,
                issues=issues,
                port=port
            )
            return redirect("/dashboard")

    context = {
        "form": form
    }
    return render(request, "issue_create.html", context)

def issue_update(request, pk):
    issue = IssuesModel.objects.get(id=pk)
    form = RimsModelForm(instance=issue)
    if request.method == 'POST':
        form = RimsModelForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect("/dashboard")

    context = {
        "form": form,
        "issue": issue
    }

    return render(request, "issue_update.html", context)

  

def issue_delete(request, pk):
    issue = IssuesModel.objects.get(id=pk)
    issue.delete()
    return redirect("/dashboard")