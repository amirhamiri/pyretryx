import time
import functools


def retry(
    attempts=3,
    delay=1,
    backoff=1,
    exceptions=(Exception,),
    logger=False,
):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay

            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)

                except exceptions as e:
                    if attempt == attempts:
                        raise

                    if logger:
                        print(
                            f"[pyretryx] Attempt "
                            f"{attempt} failed: {e}"
                        )

                    time.sleep(current_delay)
                    current_delay *= backoff

        return wrapper

    return decorator