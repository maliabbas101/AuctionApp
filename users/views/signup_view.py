from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib import messages
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

        messages.success(self.request, "Signup Successfull.")
        return redirect(self.get_success_url())








