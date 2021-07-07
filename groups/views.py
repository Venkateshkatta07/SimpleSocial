from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from groups.models import Group
from django.views import generic


class CreateGroup(generic.CreateView):
    fields=('name','description')
    model=Group

class SingleGroup(generic.DeleteView):
    model=Group

class ListGroups(generic.ListView):
    model=Group