from django.http import HttpResponse

from broadcast.models import Serie
from broadcast.settings import AVAILABLE_SERIES

# Create your views here.

def cast(request):
    """
   :type request: django.core.handlers.wsgi.WSGIRequest
   :rtype: HttpResponse
   """
    message = "Working fine dude."
    return HttpResponse(message)

def listing(request):
    """
    :type request: django.core.handlers.wsgi.WSGIRequest
    :rtype: HttpResponse
    """
    ep_list = []
    for serie in AVAILABLE_SERIES:
        episodes = Serie.objects.filter(serie=serie).order_by('episode')
        serie_name_div = '<div>Série: {}</div>'.format(episodes[0].serie)
        episodes = list('<li>épisode {}: {}</li>'.format(e.episode, e.iframe_link) for e in episodes)
        episodes.insert(0, serie_name_div)
        ep_list.extend(episodes)
    return HttpResponse(ep_list)