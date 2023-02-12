import re


def has_cyrillic(text):
    return ''.join(re.findall('[а-я А-Я]', text))


class ReverseMiddleware:
    def __init__(self, get_response):
        self.count = 0
        self.get_response = get_response

    def __call__(self, request):
        self.count += 1
        response = self.get_response(request)

        if self.count % 10 != 0:
            return response

        for word in has_cyrillic(response.content.decode('utf-8')).split(' '):
            response.content = response.content.decode('utf-8').replace(
                word, word[::-1]
            )
        return response
