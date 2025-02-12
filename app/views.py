from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import UserForm, ChangePassword, ProfilePageForm, UserEditForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User registered successfully.'}, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@login_required
@csrf_exempt
def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return JsonResponse({'message': 'Your password was successfully updated!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@login_required
@csrf_exempt
def edit_profile(request):
    if request.method == 'POST':
        form = ProfilePageForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Your profile was successfully updated!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)

@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def list_users(request):
    users = User.objects.all().values('id', 'username', 'email', 'is_active', 'is_staff', 'is_superuser')
    return JsonResponse({'users': list(users)}, status=200)

@user_passes_test(lambda u: u.is_superuser)
@csrf_exempt
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'User details were successfully updated!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)