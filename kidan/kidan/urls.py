from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_kidan.urls')),
    #add path to frontend
    path('', include('frontend.urls'))
]
