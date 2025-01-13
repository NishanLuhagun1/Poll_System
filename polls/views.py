from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'polls/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('polls:index')  # Redirect to index1 after login
        else:
            error = 'Invalid username or password'
    return render(request, 'login.html', {'error': error})

def logout_view(request):
    logout(request)
    return redirect('polls:home')  # Redirect to home after logout

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('polls/login')  # Redirect to login page after registration
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})

def index(request):
    return render(request, 'polls/index1.html')

def index2(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index2.html', context)

def detail(request):
    question_id = request.GET.get('question_id')  # Get from query parameters
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request):
    question_id = request.GET.get('question_id')  # Get from query parameters
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request):
    question_id = request.GET.get('question_id')  # Get from query parameters
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results') + f"?question_id={question.id}")
    
