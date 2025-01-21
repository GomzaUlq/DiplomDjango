from django.shortcuts import render
from states.models import State


def state(request):
    states = State.objects.all()
    return render(request, 'states/state.html', {'states': states})


def state_detail(request, id):
    state_view = State.objects.get(id=id)
    return render(request, 'states/state_detail.html', {'state': state_view})
