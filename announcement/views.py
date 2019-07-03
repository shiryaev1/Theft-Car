from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
# from announcement.models import *
from announcement.forms import AnnouncementForm
from announcement.models import Announcement


def announcement_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        announcements = Announcement.objects.filter(
            mark__mark__icontains=search_query)
    else:
        announcements = Announcement.objects.all()
    user = request.user
    return render(request, 'announcement/announcement_list.html', locals())


# def user_page(request):
    # # if pk
    # user = request.user
    # announcements = Announcement.objects.filter(author_id=user.id)
    # # announcements = Announcement.objects.all()
    # return render(request, 'users/user_page.html', locals())


class AnnouncementCreate(View):

    def get(self, request):
        form = AnnouncementForm()
        return render(request, 'announcement/announcement.html',
                      context={'form': form})

    def post(self,request):
        bount_form = AnnouncementForm(request.POST)
        if bount_form.is_valid():
            bount_form.save(request.user)
            return redirect('use:view_profile')
        else:
            print(bount_form.errors)
        context = {'form': bount_form}
        return render(request,'announcement/announcement.html', context)
