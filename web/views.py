from django.views import View
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Product
from .forms import GetInTouchForm
from .libs.telebot import telebot


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()

        return render(
            request,
            'main/products.html',
            {'products': products}
        )


class AboutUs(View):
    def get(self, request):
        return render(request, 'main/about.html')


class ContactPageView(View):
    template_name = 'main/contact.html'

    def get(self, request):
        form = GetInTouchForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            text = f"User: {obj}\nNumber: {obj.number}"
            resp = telebot.send_message(text)
            if resp.status_code == 200:
                messages.success(
                    request, 'Your message has been sent successfully. We will reply to you soon!') # noqa
                return redirect('contact-me')
            else:
                mess = "There was a problem sending the message. Please try again later." # noqa
                messages.error(request, mess)
        else:
            messages.error(request, 'Invalid form data. Please check the form and try again.') # noqa
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


class ProductDetailView(View):
    def get(self, request, id):
        product = Product.objects.get(id=id)

        return render(
            request,
            "main/shop-product.html",
            {"product": product}
        )
