from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from logs.models import Logs


def addlogmsg(user, instance, message):
    """
    :param request:
    :return:
    """
    add_log_msg = Logs(user=user, instance=instance, message=message)
    add_log_msg.save()


def showlogs(request):
    """
    :param request:
    :return:
    """

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index'))

    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('index'))

    logs = Logs.objects.all()

    return render(request, 'showlogs.html', locals())
