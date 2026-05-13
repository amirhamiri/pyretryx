from pyretryx import retry


counter = 0


@retry(attempts=3)
def test_func():
    global counter
    counter += 1

    if counter < 3:
        raise ValueError()

    return True


def test_retry():
    assert test_func() is True