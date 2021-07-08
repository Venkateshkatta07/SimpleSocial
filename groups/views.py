from _typeshed import Self

from django.core.checks import messages
from simplesocial.groups.models import GroupMember
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from groups.models import Group
from django.views import generic
from django.db import IntegrityError


class CreateGroup(generic.CreateView):
    fields=('name','description')
    model=Group

class SingleGroup(generic.DeleteView):
    model=Group

class ListGroups(generic.ListView):
    model=Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self, *args,**kwargs):
         return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group=get_object_or_404(Group,kwargs={'slug':Self.kwargs.get('slug')})

        try:
            GroupMember.objects.create(user=Self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,('Warning already a member!'))
        else:
            messages.success(self.request,('You are a member now!'))

        return super().get(request,*args,**kwargs)
        
class Leavegroup():
    pass
