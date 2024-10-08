import json
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def users_list(request):
    if request.method == 'GET':
        # listar un solo usuario
        # defino que voy a usar el modelo de usuario personalizado
        User = get_user_model()
        users_list = list(User.objects.all().values("id","username",
        "password",
        "email",
        "birth_date",
        "biography"))
        return JsonResponse(users_list, safe=False)
            
    

def user_detail(request, username):
    pass

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        # Getting data
        decoded_body = request.body.decode('utf-8')
        body = json.loads(decoded_body)

        # Data validation
        errors = []
        if body['username'] == "":
            errors.append({'username': 'username cannot be empty'})

        if body['birth_date'] == "":  # TODO: Validate date format
            errors.append({'birth_date': 'Incorrect date format'})

        if body['email'] == "":  # TODO: Validate email format
            errors.append({'birth_date': 'Incorrect email format'})

        if len(errors) > 0:
            return JsonResponse({'errors': errors}, status=400)

        # Saving data in DB:
        # Cuando se usa un modelo de usario personalizado se debe usar el get_user_model()
        User = get_user_model()
        # Usar el create_user en lugar del create
        user = User.objects.create_user(
            username=body['username'],
            password=body['password'],
            email=body['email'],
            birth_date=body['birth_date'],
            biography=body['biography']
        )

        return JsonResponse(data={'message': 'Created user', 'id': user.id, 'username': user.username})

    return HttpResponse("Method not allowed", status=405)

def update_user(request, username):
    pass

def delete_user(request, username):
    pass

