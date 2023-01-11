from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver
from ..forms import AuctionUserCreationForm
from django.shortcuts import redirect


class SignUpView(CreateView):
    form_class = AuctionUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        self.object = form.save()
        self.object.groups.set(self.request.POST.get('groups'))
        self.object.save()
        return redirect(self.get_success_url())








