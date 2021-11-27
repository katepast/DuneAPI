from ValidatorPizzaAPI.helpers.service_api_validator_pizza import ServiceAPIValidatorPizza
from ValidatorPizzaAPI.routes.user_routes import UserRoutes


class UserServiceAPI(ServiceAPIValidatorPizza):

    def get_response_by_valid_email(self):
        return self._get(UserRoutes.VALID_EMAIL_URL)

    def get_response_by_invalid_email(self):
        return self._get(UserRoutes.INVALID_EMAIL_URL)

    def get_response_by_valid_domain(self):
        return self._get(UserRoutes.VALID_DOMAIN_URL)

    def get_response_by_invalid_domain(self):
        return self._get(UserRoutes.INVALID_DOMAIN_URL)

