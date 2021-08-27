Tradexa Assignment 

Please install the dependecies in "requirements.txt".

Here is the list of URLs.

    path('admin/', admin.site.urls),
    path('add_post/', add_post, name='add_post'),
    path('view_all/', view_all, name='view_all'),
    path('register/', registration),
    path('login/', authentication_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
