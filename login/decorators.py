from django.shortcuts import render, redirect
from .models import User
def login_required(func):
    def wrapper(request, *args, **kwargs):
        id_user = request.session.get('user_id')
        user = User.objects.get(id=id_user)
        if user:
            if user.role.id ==1:
                return func(request,*args,**kwargs)
            else:
                message = 'Пользователь должен быть директором'
        else:
            message = 'Пользователь не найден в базе'
        return render(request,'error.html',{'message':message})
    return wrapper