from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


# !Create router instance
router = DefaultRouter()

urlpatterns = [
    path('',views.CreateUserView.as_view()),
    path('forgot-password',views.PasswordRecoveryView.as_view()),
    #* Authentication Views
    path('api/token',TokenObtainPairView.as_view(),name='token_obtain_view'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh_view')
]
router.register('users',views.UserFullControlView,basename="full_user_access")

# ! add router urls to our url patterns
urlpatterns+= router.urls