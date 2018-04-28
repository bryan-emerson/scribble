from urllib.parse import parse_qs

class SimpleUnderscoreMethod:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.method == 'POST':
            post_data = parse_qs(request.body)
            method = post_data[b'_method'][0].decode('UTF-8')
            request.method = method
            print('*' * 80 + '\n', response, request.method, '\n' + '*' * 80)
        return response
