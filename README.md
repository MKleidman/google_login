# google_login
Django Admin Google Login

This only works when you want to override /admin/login/ and /admin/logout/ to use google login and logout

1) add https://github.com/MKleidman/google_login/ to your requirements

2) add google_login to your INSTALLED_APPS

3) make sure GOOGLE_CLIENT_ID is in your django settings

4) add the following to your urls.py:

    from google_login.urls import urlpatterns as google_login_patterns
    
    urlpatterns = google_login_patterns + [your app or project's url patterns]
