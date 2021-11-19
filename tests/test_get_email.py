import pytest

from ValidatorPizzaAPI import config
from ValidatorPizzaAPI.helpers.http_methods import get
from ValidatorPizzaAPI.helpers.logging import logger
from ValidatorPizzaAPI.helpers.verify import Verify
from ValidatorPizzaAPI.helpers.assert_response import *


@pytest.mark.debug
def test_get_response_by_valid_email():
    """Get response from valid email"""

    email_value = VALID_EMAIL.get('email')
    response = get(url=config.valid_email.format(email_value))
    json_resp = response.json()

    logger.info("Verify that status code returns 200 for GET request with valid email")
    Verify.equals(200, response.status_code, "Status code does not equal to 200")

    logger.info(f"Verify that specified user with email '{email_value}' is created")
    Verify.equals(email_value, json_resp['email'], f"User '{email_value}' is not created")

    logger.info(f"Verify that full response '{VALID_EMAIL}' corresponds to received '{json_resp}'")
    Verify.equals(VALID_EMAIL, json_resp, f"Data does not correspond to '{VALID_EMAIL}'")


@pytest.mark.debug
def test_get_response_by_invalid_email():
    """Get response from invalid email"""

    response = get(url=config.invalid_email_url)
    json_resp = response.json()

    logger.info("Verify that status code returns 400 for GET request with invalid email")
    Verify.equals(400, response.status_code, "Status code does not equal to 400 for GET request with invalid email")

    logger.info(f"Verify that response '{INVALID_EMAIL_RESPONSE}' corresponds to received '{json_resp}'")
    Verify.equals(INVALID_EMAIL_RESPONSE, json_resp, f"Response does not correspond to '{INVALID_EMAIL_RESPONSE}'")


@pytest.mark.debug
def test_get_response_by_valid_domain():
    """Get response from valid domain email"""

    domain_value = VALID_EMAIL.get('domain')
    response = get(url=config.valid_domain_url.format(domain_value))
    json_resp = response.json()

    logger.info(f"Verify that status code returns 200 for GET request of specified domain value '{domain_value}'")
    Verify.equals(200, response.status_code, "Status code does not equal to 200")

    logger.info(f"Verify that specified user with domain '{domain_value}' is received")
    Verify.equals(domain_value, json_resp['domain'], f"Domain value '{domain_value}' is not received")

    logger.info(f"Verify that full domain response '{VALID_DOMAIN}' corresponds to received '{json_resp}'")
    Verify.equals(VALID_DOMAIN, json_resp, f"Full domain does not correspond to '{VALID_DOMAIN}'")


@pytest.mark.debug
def test_get_response_by_invalid_domain():
    """Get response from invalid domain"""

    response = get(url=config.invalid_domain_url)
    json_resp = response.json()

    logger.info("Verify that status code returns 400 for GET request with invalid domain")
    Verify.equals(400, response.status_code, "Status code does not equal to 400 for GET request with invalid domain")

    logger.info(f"Verify that response '{INVALID_DOMAIN_RESPONSE}' corresponds to received '{json_resp}'")
    Verify.equals(INVALID_DOMAIN_RESPONSE, json_resp, f"Data does not correspond to '{INVALID_DOMAIN_RESPONSE}'")
