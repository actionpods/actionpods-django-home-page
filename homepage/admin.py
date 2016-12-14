from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import Introduction, NewsItem, Link

# Register your models here.
class IntroductionAdminForm(forms.ModelForm):
    #Set the editor to a WYSIWYG or Markdown
    #NOTE: Be sure to edit the template to reflect a change.
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Introduction
        fields = '__all__'

class IntroductionAdmin(admin.ModelAdmin):
    exclude = ['posted']
    form = IntroductionAdminForm

class NewsItemAdminForm(forms.ModelForm):
    #Set the editor to a WYSIWYG or Markdown
    #NOTE: Be sure to edit the template to reflect a change.
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Introduction
        fields = '__all__'

class NewsItemAdmin(admin.ModelAdmin):
    exclude = ['posted']
    form = NewsItemAdminForm
    prepopulated_fields = {
                           'slug': ('title',),
                           }


admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(Link)
