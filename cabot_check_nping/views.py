from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

from cabot.cabotapp.models import StatusCheck
from cabot.cabotapp.views import (CheckCreateView, CheckUpdateView,
                                  StatusCheckForm, base_widgets)

from .models import NPINGStatusCheck


class NPINGStatusCheckForm(StatusCheckForm):
    symmetrical_fields = ('service_set', 'instance_set')

    class Meta:
        model = NPINGStatusCheck
        fields = (
            'name',
            'host',
            'nping_cmd_line_switches',
            'count',
            'frequency',
            'active',
            'importance',
            'debounce',
        )

        widgets = dict(**base_widgets)
        widgets.update({
            'host': forms.TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'service.arachnys.com',
            }),
            'nping_cmd_line_switches': forms.TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'service.arachnys.com',
            })
        })


class NPINGCheckCreateView(CheckCreateView):
    model = NPINGStatusCheck
    form_class = NPINGStatusCheckForm


class NPINGCheckUpdateView(CheckUpdateView):
    model = NPINGStatusCheck
    form_class = NPINGStatusCheckForm


def duplicate_check(request, pk):
    pc = StatusCheck.objects.get(pk=pk)
    npk = pc.duplicate()
    return HttpResponseRedirect(reverse('update-nping-check', kwargs={'pk': npk}))
