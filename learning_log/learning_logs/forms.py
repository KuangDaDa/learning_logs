from django.forms import ModelForm
from learning_logs.models import Topic,Entry


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        label = {'text': ''}


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}

