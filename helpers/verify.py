import logging


class Verify:
    @staticmethod
    def equals(expected, actual, message_on_fail):
        """Method to check that actual information equals to expected information"""
        try:
            assert expected == actual, message_on_fail
        except AssertionError as err:
            err_type = err.__class__.__name__
            logging.error(f"{err_type}: {message_on_fail}")
            logging.debug(f"{expected} should be equal to {actual}")
            raise err
