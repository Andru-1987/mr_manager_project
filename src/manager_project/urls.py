from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


from .views import LandingPage , Custom404View


from app_manager_user.views import ManagerUserCreateView
from app_manager_user.views import ManagerUserLoginView
from app_manager_user.views import ManagerUserProfileView
from app_manager_user.views import ManagerUserUpdateView



from django.views.static import serve
from django.urls import re_path


urlpatterns = [
    path( "admin/", admin.site.urls),
    path( "", LandingPage.as_view(), name="index"),

    path( "logout/", LogoutView.as_view(), name="logout"),
    
    path( "login/", ManagerUserLoginView.as_view(), name="login"),
    path( "register/", ManagerUserCreateView.as_view(), name="register"),
    path( "profile/", ManagerUserProfileView.as_view() ,name="profile"),
    path( "update/<int:pk>/", ManagerUserUpdateView.as_view() , name="update"),

    path( "manager/", include("app_no_user.urls")),
    path( "beneficios/", include("app_beneficios.urls")),
    path( "file/", include("app_manager_user.urls")),
    
    path( "cuota/", include("app_cuota.urls")),
    path( "consulta/", include("app_consulta.urls"))

]

handler404 = Custom404View.as_view()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
