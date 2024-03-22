from django.http import HttpResponse

from .utils import get_url_screenshot


# Create your views here.
def index(request):
    url = "https://play.pixels.xyz/pixels/share/3173"
    screenshot = get_url_screenshot(url)
    print(screenshot)
    return HttpResponse(screenshot, content_type="image/jpeg")
