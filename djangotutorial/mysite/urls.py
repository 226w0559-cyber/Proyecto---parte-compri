from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView  # Agrega esta importación


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('', RedirectView.as_view(url='polls/rafael1/', permanent=True)), # Redirige la raíz a rafael1