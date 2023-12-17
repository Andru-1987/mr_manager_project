from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static


from .views import LandingPage , Custom404View


from app_aigasra_user.views import AigasraUserCreateView
from app_aigasra_user.views import AigasraUserLoginView
from app_aigasra_user.views import AigasraUserProfileView
from app_aigasra_user.views import AigasraUserUpdateView





urlpatterns = [
    path( "admin/", admin.site.urls),
    path( "", LandingPage.as_view(), name="index"),

    path( "logout/", LogoutView.as_view(), name="logout"),
    
    path( "login/", AigasraUserLoginView.as_view(), name="login"),
    path( "register/", AigasraUserCreateView.as_view(), name="register"),
    path( "profile/", AigasraUserProfileView.as_view() ,name="profile"),
    path( "update/<int:pk>/", AigasraUserUpdateView.as_view() , name="update"),

    path( "aigasra/", include("app_no_user.urls")),
    path( "beneficios/", include("app_beneficios.urls")),
    path( "file/", include("app_aigasra_user.urls")),
    
    path( "cuota/", include("app_cuota.urls")),
    path( "consulta/", include("app_consulta.urls"))

]

handler404 = Custom404View.as_view()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

