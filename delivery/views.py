from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout
from django.urls import reverse
from delivery.forms import AgentForm, PickForm, ProdForm, ProductOwner
from delivery.service import Services
from django.contrib import messages



class FirstPage(View):
    def get(self, request):
        data = {}
        return render(request, "first-page.html",data)


class Index(View):
    def get(self, request):
        data = {
            "form":AgentForm()
        }
        return render(request, "index.html", data)
    
    def post(self, request):
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
        


class PickPoint(View):
    def get(self, request):
        data = {
            "form":PickForm()
        }
        return render(request, "pick.html", data)
    
    def post(self, request):
        form = PickForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))
        else:
            data = {
                "form":form
            }
            return render(request, "pick.html", data)
    


class Deliver(View):
    def get(self, request):
        data = {
            "form":ProdForm()
        }
        return render(request, "arrived.html", data)
    
    def post(self, request):
        form = ProdForm(request.POST)
        sms = Services()
        if form.is_valid():
            form.save()
            numbers = [form.cleaned_data["contact"]]
            message = f"Dear {form.cleaned_data['name']}, your package {form.cleaned_data['product_name']} has arrived and is ready for pickup at agent SAmple Agent"
            sms.send_message(numbers=numbers, message=message)
            messages.success(request, message)
            return redirect(reverse("all-available"))


class Available(View):
    def get(self, request):
        data = {
            "all": ProductOwner.objects.all().order_by("-id")
        }
        return render(request, "all.html", data)
    

class PickUp(View):
    def get(self, request, id):
        owner = ProductOwner.objects.get(id=id)
        owner.status = True
        owner.save()
        sms = Services()
        number = [owner.contact]
        messages = f"Dear {owner.name}, your package {owner.product_name} has been picked up successfully"
        sms.send_message(numbers=number, message=messages)
        return redirect(reverse("all-available"))
