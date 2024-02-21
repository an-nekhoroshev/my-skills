from django.shortcuts import render


def home(request):
    return render(request, 'main.html', {'title': 'MySkills'})


def todo_list(request):
    return render(request, 'to-do_list/to-do_list.html', {'title': 'Список дел'})


def calculator(request):
    return render(request, 'calculator/calc.html', {'title': 'Калькулятор'})
