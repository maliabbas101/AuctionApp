from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages

from ..forms import AuctionUserCreationForm

class SignUpView(CreateView):
    form_class = AuctionUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def post( self, request ,*args, **kwargs):
        messages.success(request, "Account created successfully.")
        return super().post(request, *args, **kwargs)








