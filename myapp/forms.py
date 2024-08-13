from django import forms

class create_new_task(forms.Form):
    title = forms.CharField(label="Task Title",  max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="description task", widget=forms.Textarea(attrs={
        'class':'input'
    }))


class create_new_project(forms.Form):
    name = forms.CharField(label="Project Name",  max_length=200, widget=forms.TextInput(attrs={
        'class':'input'
    }))

