from abc import ABC

import requests
import logging

from ValidatorPizzaAPI.config import config
from ValidatorPizzaAPI.routes.user_routes import UserRoutes


class ServiceAPIValidatorPizza(ABC):
    def __init__(self):
        self.url = config.base_url
        self._session = requests.session()

    def _get(self, route: UserRoutes, **kwargs):
        """Return GET request"""
        logging.debug("Return GET request")
        return self._session.get(self.url + route.value, **kwargs)

    def _post(self, route: UserRoutes, body: dict, **kwargs):
        """Return POST request"""
        logging.debug("Return POST request")
        return self._session.post(self.url + route.value, json=body, **kwargs)

