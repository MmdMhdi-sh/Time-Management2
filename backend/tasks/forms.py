from django import forms

from .models import Task

MAX_TASK_TITLE_LENGTH = 50

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'done', 'duration']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def cleaned_title(self):
        title = self.cleaned_data.get("title")
        if len(title) > MAX_TASK_TITLE_LENGTH:
            raise forms.ValidationError("This title is too long!")
        return title