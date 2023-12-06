from django.shortcuts import render
from .forms import DataFileForm, MaualDatasForm
# Create your views here.


def index(request):
    return render(request, 'datas/index.html')


def ManualInput(request):
    if request.method == 'POST':
        form = MaualDatasForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'form': form}
    else:
        form = MaualDatasForm()
        context = {'form': form}
    return render(request, 'datas/ManualInput.html', context)
def Fileupload(request):
    if request.method == 'POST':
        form = DataFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {'form': form}
    else:
        form = DataFileForm()
        context = {'form': form}
    return render(request, 'datas/Fileupload.html', context)
