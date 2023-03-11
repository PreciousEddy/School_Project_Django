from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import Student

def student_registration(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data.pop('csrfmiddlewaretoken')
        student = Student.objects.create(**form_data)
        return redirect('student_detail', pk=student.pk)
    return render(request, 'students/registration.html')

@login_required
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/detail.html', {'student': student})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('student_detail', pk=user.student.pk)
    else:
        form = AuthenticationForm()
    return render(request, 'students/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
