from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'Balkonich/main.html')

def insulation(request):
    return render(request, 'Balkonich/insulation.html')

def electrical_installation(request):
    return render(request, 'Balkonich/electrical_installation.html')

def interior_decoration(request):
    return render(request, 'Balkonich/interior_decoration.html')

def slopes(request):
    return render(request, 'Balkonich/slopes.html')

def armored_film(request):
    return render(request, 'Balkonich/armored_film.html')