from django import forms

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'content': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'content': 'Write your note here:'
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError("Title must be at least 3 characters long")
        if 'Django' not in title:
            raise forms.ValidationError("Title must contain the word 'Django'")
        return title