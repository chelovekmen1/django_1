from django.http import HttpResponse


def accounts_home(request):
    return HttpResponse("Это страница аккаунтов нашего сайта с машинами.")


def user_view(request):
    name = request.GET.get('name', 'Не указано')
    age = request.GET.get('age', 'Не указано')
    email = request.GET.get('email', 'Не указано')
    phone = request.GET.get('phone', 'Не указано')


    html_content = f"<h1>{name}</h1><p>Возраст: {age}</p><p>Email: {email}</p><p>Phone: {phone}</p>"

    return HttpResponse(html_content)


from django.shortcuts import render

# Create your views here.
