from django.forms import ModelForm

from .models import Poll,SimplePoll

class CreatePollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three', 'option_four']    # noqa: E501

class CreatePollFormSimple(ModelForm):
    class Meta:
        model = SimplePoll
        fields = ['question', 'option_yes', 'option_no']        