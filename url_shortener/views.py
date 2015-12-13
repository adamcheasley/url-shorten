from django.http import HttpResponse
from django.http import HttpResponseNotFound


def home(request):
    return HttpResponse("welcome")


def resolve(request, shortcode=None):
    shortcode = request.resolver_match.args[0]
    if shortcode is None:
        return HttpResponseNotFound("<h1>Not found</h1>")

    # look up the real url
    return HttpResponse("hello world")


def create_short_url(request):
    return HttpResponse("create URL here")
