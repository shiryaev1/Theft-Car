from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
# from announcement.models import *
from announcement.forms import AnnouncementForm
from announcement.models import Announcement


def announcement_list(request):
    announcements = Announcement.objects.all()
    user = request.user
    return render(request, 'announcement/announcement_list.html', locals())


def user_page(request):
    return render(request, 'users/user_page.html')


class AnnouncementCreate(View):

    def get(self,request):
        form = AnnouncementForm()
        return render(request, 'announcement/announcement.html',
                      context={'form': form})

    def post(self,request):
        bount_form = AnnouncementForm(request.POST)
        if bount_form.is_valid():
            bount_form.save(request.user)
            return redirect('announcement:user-page')
        else:
            print(bount_form.errors)
        context = {'form': bount_form}
        return render(request,'announcement/announcement.html', context)
