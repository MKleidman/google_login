# google_login
Django Admin Google Login

This only works when you want to override /admin/login/ and /admin/logout/ to use google login and logout

1) add https://github.com/MKleidman/google_login/ to your requirements

2) add google_login to your INSTALLED_APPS

3) make sure GOOGLE_CLIENT_ID and HOSTNAME are in your django settings

4) add the following to your urls.py:

    from google_login.urls import urlpatterns as google_login_patterns
    
    urlpatterns = google_login_patterns + [your app or project's url patterns]

5) add a HOSTNAME setting that google will send you back to upon login completion


For now, this will get_or_create a django auth contrib User with email = google email, is_staff=True, defaults={"first_name": name_bits[0], "last_name": " ".join(name_bits[1:]), "password": set_unusable_password, "username": google email})
