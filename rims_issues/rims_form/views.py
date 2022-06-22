from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import IssuesModel
from .forms import RimsForm, RimsModelForm, CustomUserCreationForm

# Create your views here.


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


def home_page(request):

    return render(request, 'index.html', {})


@login_required
def dashboard(request):
    if request.user.is_superuser:
        issues = IssuesModel.objects.all()
    else:
        issues = IssuesModel.objects.filter(
            user__port=request.user.port)

    # lagos_list = IssuesModel.objects.filter(port__)
    # lagos_issues = IssuesModel.objects.filter(port_id=1)

    context = {
        'issues': issues,
        # 'lagos_issue': lagos_issues
    }

    return render(request, 'dashboard.html', context)


@login_required
def issues_detail(request, pk):
    issue = IssuesModel.objects.get(id=pk)
    if issue.user != request.user:
        return HttpResponse("fuck off")

    context = {
        'issue': issue
    }
    return render(request, "issues_detail.html", context)


@login_required
def rims_form(request):
    issues = IssuesModel.objects.all()
    context = {
        'issues': issues
    }
    return render(request, 'issues_form.html', context)
    # return render(request, 'index.html', context)


@login_required
def issue_create(request):
    form = RimsForm()
    if request.method == "POST":
        form = RimsForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            subject = form.cleaned_data['subject']
            status = form.cleaned_data['status']
            sen_no = form.cleaned_data['sen_no']
            issues = form.cleaned_data['issues']
            IssuesModel.objects.create(
                subject=subject,
                status=status,
                sen_no=sen_no,
                issues=issues,
                user=request.user
            )
            return redirect("/dashboard")

    context = {
        "form": form
    }
    return render(request, "issue_create.html", context)


@login_required
def issue_update(request, pk):
    issue = IssuesModel.objects.get(id=pk)
    if issue.user != request.user:
        return HttpResponse("fuck off")

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


@login_required
def issue_delete(request, pk):
    issue = IssuesModel.objects.get(id=pk)
    issue.delete()
    return redirect("/dashboard")
