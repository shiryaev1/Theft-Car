from django import forms
from announcement.models import Announcement
from django.core.exceptions import ValidationError


class AnnouncementForm(forms.ModelForm):

    class Meta:
        model = Announcement
        fields = [
            'mark',
            'model',
            'year_of_issue',
            'color',
            'number',
            'date_theft',
            'description'
        ]

        # widgets = {
        #     'mark': forms.TextInput(attrs={'class': 'form-control'}),
        #     'model': forms.TextInput(attrs={'class': 'form-control'}),
        #     'year_of_issue': forms.TextInput(attrs={'class': 'form-control'}),
        #     'color': forms.TextInput(attrs={'class': 'form-control'}),
        #     'number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'date_theft': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.TextInput(attrs={'class': 'form-control'}),
        # }

    # def clean_slug(self):
    #     new_slug = self.cleaned_data['slug'].lower()
    #     if new_slug == 'create':
    #         raise ValidationError('Slug may not be "Create"')
    #     return new_slug

    def save(self, user):
        announcement = super(AnnouncementForm, self).save(commit=False)
        announcement.author = user

        announcement.save()
        return announcement
