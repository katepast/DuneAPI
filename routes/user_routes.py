from enum import Enum


class UserRoutes(Enum):
    INVALID_EMAIL_URL = "/email/em.com"
    VALID_EMAIL_URL = "/email/email@example.com"

    VALID_DOMAIN_URL = "/domain/example.com"
    INVALID_DOMAIN_URL = "/domain/test_data"
