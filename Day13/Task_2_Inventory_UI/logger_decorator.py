from datetime import datetime
from functools import wraps

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        with open("logs.txt", "a") as f:
            f.write(f"[{datetime.now()}] {func.__name__} executed\n")

        return result
    return wrapper