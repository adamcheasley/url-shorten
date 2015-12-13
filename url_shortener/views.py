from django.http import HttpResponse


def resolve(request, shortcode):
    # look up the real url
    return HttpResponse("hello world")
