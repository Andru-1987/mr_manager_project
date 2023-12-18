from django.utils.deprecation import MiddlewareMixin





class CorsMiddlewareMixin(MiddlewareMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.allowed_origins = [
            "http://localhost",  
            "https://*",
            "http://*",
            "https://*.app.github.dev",
            "http://localhost:80/*"
        ]


    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, DELETE"
        response["Access-Control-Allow-Headers"] = "*"
        return response