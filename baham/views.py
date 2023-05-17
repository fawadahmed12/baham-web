from django.shortcuts import render,reverse
from django.template import loader
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from baham.models import VehicleModel
from baham.enum_types import VehicleType

# Create your views here
def view_home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))
def view_about(request):
    template = loader.get_template("about.html")
    return HttpResponse(template.render({}, request))
def view_contact(request):
    template = loader.get_template("contact.html")
    return HttpResponse(template.render({}, request))

def view_vehicles(request):
    template = loader.get_template("vehicles.html")
    veh = VehicleModel.objects.all().order_by('vendor')
    context = {
        "vehicle_data": veh
    }
    return HttpResponse(template.render(context, request))

def view_addvehicle(request):
    template = loader.get_template("addvehicle.html")
    VEHICLE_TYPE_CHOICES = [(choice.value, choice.name) for choice in VehicleType]
    context = {
        "types": VEHICLE_TYPE_CHOICES
    }
    print("##############################")
    print(context)
    return HttpResponse(template.render(context, request))

def save_vehicle(request):
    _vendor = request.POST.get('vendor')
    _model = request.POST.get('model')
    _type = request.POST.get('type')
    _capacity = request.POST.get('capacity')

    # // validation

    newcar = VehicleModel.objects.create(vendor=_vendor, model=_model, type=_type, capacity=_capacity)
    newcar.save()

    return HttpResponseRedirect(reverse('vehicles'))

def updatevehicle(request):
    _vendor = request.POST.get('vendor')
    _model = request.POST.get('model')
    _type = request.POST.get('type')
    _capacity = request.POST.get('capacity')
    newcar = VehicleModel.objects.create(vendor=_vendor, model=_model, type=_type, capacity=_capacity)
    newcar.save()


def voided(request,id):
    obj= VehicleModel.objects.get(uuid=id)
    obj.void()
    return HttpResponseRedirect(reverse('vehicles'))

def unvoided(request,id):
    obj= VehicleModel.objects.get(uuid=id)
    obj.unvoid()
    return HttpResponseRedirect(reverse('vehicles'))


