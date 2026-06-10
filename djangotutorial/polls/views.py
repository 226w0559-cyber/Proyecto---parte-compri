from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def vista1(request):
    return HttpResponse("Disfrutando de un fin de semana jugando videojuegos con amigos <h1>Rafael Castro</h1>..")

def vista2(request):
    return HttpResponse("Caminando por la tarde mientras escucho mi música favorita en los audífonos <h1>Rafael Castro</h1>..")

def vista3(request):
    return HttpResponse("Tengo varias metas en mente para este año en la programación <h1>Rafael Castro</h1>..")

def vista4(request):
    return HttpResponse("Recordando las mejores anécdotas y risas durante los proyectos en equipo <h1>Rafael Castro</h1>..")

def vista5(request):
    return HttpResponse("Cada línea de código es un paso más cerca de dominar el desarrollo web <h1>Rafael Castro</h1>..")

def vista6(request):
    return HttpResponse("Momentos clave en las clases, retos superados, café y aprendizaje constante <h1>Rafael Castro</h1>..")

def vista7(request):
    return HttpResponse("El verdadero reto no es escribir el código, sino entender la lógica detrás de él <h1>Rafael Castro</h1>..")

def vista8(request):
    return HttpResponse("Analizando nuevas ideas para implementar funciones útiles en la aplicación <h1>Rafael Castro</h1>..")

def vista9(request):
    return HttpResponse("Configurando servidores y desplegando proyectos en la nube con éxito <h1>Rafael Castro</h1>..")

def vista10(request):
    return HttpResponse("Y con esto concluimos la configuración de las vistas de la aplicación <h1>Rafael Castro</h1>..")