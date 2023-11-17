from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Construye la estructura deseada para la respuesta
        response_data = {
            'ok': True,
            'results': data
        }

        # Si hay errores, modifica la estructura para reflejar el error
        if renderer_context and 'response' in renderer_context:
            response = renderer_context['response']
            if not response.status_code // 100 == 2:  # Cualquier código de estado 2xx se considera éxito
                response_data['ok'] = False
                response_data['error'] = data.get(
                    'detail', 'Unknown error')
                response_data["results"] = None

        return super().render(response_data, accepted_media_type, renderer_context)
