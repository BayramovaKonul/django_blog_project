from typing import Any
from django.shortcuts import redirect
from django.urls import reverse
import logging

logger = logging.getLogger('base')

# to prevent authenticated users to go to login and register again
class PreventAuthenticatedUsers:
    def __init__(self, get_response):
        self.get_response = get_response
    

    def __call__(self, request) -> Any:
        
        logger.info(f"Request method: {request.method}, Request path: {request.path}")

        unallowed_urls = [reverse('login'), reverse('register')]
        if request.user.is_authenticated and request.path in unallowed_urls:
            logger.warning(f"User: {request.user.id} tried to go to unallowed urls.")
            return redirect('about')
        response = self.get_response(request)
        logger.info(f"Response status code: {response.status_code}")
        return response