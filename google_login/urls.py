from django.http import HttpResponse, HttpResponseForbidden
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import authenticate, login, models, logout
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from oauth2client import client, crypt

def complete_login(request):
    try:
        idinfo = client.verify_id_token(request.POST['idtoken'], settings.GOOGLE_CLIENT_ID)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")

        # If auth request is from a G Suite domain:
        #if idinfo['hd'] != GSUITE_DOMAIN_NAME:
        #    raise crypt.AppIdentityError("Wrong hosted domain.")
    except crypt.AppIdentityError:
        # Invalid token
        return HttpResponseForbidden()
    userid = idinfo['sub']
    name_bits = request.POST['name'].split()
    user, created = models.User.objects.get_or_create(email=request.POST['email'], defaults={
        "first_name": name_bits[0], "last_name": " ".join(name_bits[1:])})
    if created:
        user.set_unusable_password()
        user.is_staff = True
        user.username = user.email
        user.save()
    models.Group.objects.get(name='All').user_set.add(user)
    login(request, user)
    return HttpResponse('<html><body>{}</body></html>'.format(user.id), content_type='text/html')

@ensure_csrf_cookie
def login_view(request):
    return render_to_response('google-login.html',
                              {"next": request.GET.get('next', '/admin/'), "google_client_id": settings.GOOGLE_CLIENT_ID})

def logout_view(request):
    logout(request)
    return render_to_response('google-logout.html', {"google_client_id": settings.GOOGLE_CLIENT_ID})


urlpatterns = [
    url(r'^login/', login_view),
    url(r'^logout/', logout_view),
    url(r'^complete_login/$', complete_login),
]
