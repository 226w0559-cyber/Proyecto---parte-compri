from django.contrib import admin
from django.urls import include, path # Asegúrate de importar 'include'

urlpatterns = [
    path('polls/', include('polls.urls')), # Esta línea conecta tu app
    path('admin/', admin.site.urls),
]