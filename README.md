# pyretryx

Simple retry decorator for Python.

## Installation

```bash
pip install pyretryx
```

## Usage

```python
from pyretryx import retry

@retry(attempts=3)
def fetch():
    ...
```

## Async Usage

```python
from pyretryx import async_retry

@async_retry(attempts=5)
async def fetch():
    ...
```