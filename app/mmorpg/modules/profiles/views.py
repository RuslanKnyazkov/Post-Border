from django.shortcuts import render
from django.views.generic import DetailView
from .models import UserProfile

class ProfileView(DetailView):
    template_name = 'profile.html'
    model = UserProfile
    context_object_name = 'profile'
