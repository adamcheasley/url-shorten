from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import URLCreationForm
from .models import URLMap


def home(request):
    return HttpResponse("welcome")


def resolve(request, shortcode=None):
    shortcode = request.resolver_match.args[0]
    if shortcode is None:
        return HttpResponseNotFound("<h1>Not found</h1>")

    # look up the real url
    url = URLMap.objects.filter(shortcode=shortcode)
    if not url:
        return HttpResponseNotFound("<h1>Not found</h1>")

    return HttpResponseRedirect(url[0].original_url)


def create_short_url(request):
    if request.method == "POST":
        form = URLCreationForm(request.POST)
        form.is_valid()
        new = URLMap(original_url=form.cleaned_data.get('url'))
        new.save()
        base_url = request.build_absolute_uri().replace(
            request.get_full_path(), '')
        shorturl = "{}/resolve/{}".format(
            base_url, new.shortcode)
        return render(request,
                      'shorturl_created.html',
                      {'shorturl': shorturl})
    else:
        form = URLCreationForm()

    return render(request, 'url_creation.html', {'form': form})
