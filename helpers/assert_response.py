VALID_EMAIL = {'status': 200,
               'email': 'email@example.com',
               'domain': 'example.com',
               'mx': True,
               'disposable': False,
               'alias': False,
               'did_you_mean': None}

INVALID_EMAIL_RESPONSE = {'error': 'The email address is invalid.', 'status': 400}

VALID_DOMAIN = {'status': 200,
                'domain': 'example.com',
                'mx': True,
                'disposable': False,
                'did_you_mean': None}

INVALID_DOMAIN_RESPONSE = {
    "status": 400,
    "error": "The domain is invalid."
}
