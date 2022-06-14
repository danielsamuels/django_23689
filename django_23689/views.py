from django.http import JsonResponse
from django.utils import translation
from django.views.generic import View


class ExampleView(View):

    def get(self, *args, **kwargs):
        language_code = translation.get_language()
        # ^-- should be pt-BR, but is pt
        return JsonResponse({'language_code': language_code})
