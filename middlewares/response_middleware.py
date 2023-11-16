class CustomResponseMiddleware:  # Middleware para modificar las respuestas de la API
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 200:
            data = response.data if hasattr(response, 'data') else {}
            response.data = {'ok': True, 'results': data}
        else:
            response.data = {'ok': False, 'message': response.data['detail']}

        return response
