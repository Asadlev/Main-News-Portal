class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    # код, выполняемый до формирования ответа (или другого middleware)
        response = self.get_response(request)
    # код, выполняемый после формирования запроса (или нижнего слоя)
        if request.mobile:
            prefix = 'mobile/'
        else:
            prefix = 'fill/'
        response.template_name = prefix + response.template_name

        return response

