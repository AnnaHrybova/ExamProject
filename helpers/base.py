import logging
import time

from selenium.common.exceptions import WebDriverException, TimeoutException


def wait_until_ok(timeout, period=0.5):
    """Retry function with parameters"""

    def act_decorator(target_func):
        logger = logging.getLogger(__name__)

        def wrapper(*args, **kwargs):
            must_end = time.time() + timeout
            while True:
                try:
                    return target_func(*args, **kwargs)
                except (WebDriverException, AssertionError, TimeoutException) as error:
                    error_name = error if str(error) else error.__class__.__name__
                    logger.debug("Catch '%s'. Left %s seconds", error_name, (must_end - time.time()))
                    if time.time() >= must_end:
                        logger.warning("Waiting timed out after %s", timeout)
                        raise error
                    time.sleep(period)

        return wrapper

    return act_decorator