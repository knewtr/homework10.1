from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args):
       pass
        return wrapper
    return decorator

@log(filename='mylog.txt')
def log(filename):
    if filename:
