from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import redirect
# from announcement.models import *
from announcement.forms import PostForm


class PostCreate(View):
    def get(self,request):
        form = PostForm()
        return render(request, 'announcement/announcement.html',
                      context={'form': form})

    def post(self,request):
        bount_form = PostForm(request.POST)
        if bount_form.is_valid():
            bount_form.save()
            return redirect('post:post_create_url')
        else:
            print(bount_form.errors)
        context = {'form': bount_form}
        return render(request,'announcement/announcement.html', context)
