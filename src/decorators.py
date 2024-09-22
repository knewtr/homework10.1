def log(filename=""):
    """Декоратор регистрирует данные выполнения функций"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w") as file:
                        file.write(f"Функция {func.__name__} работает")
                else:
                    print(f"{func.__name__} работает")
                return result
            except Exception as ex:
                if filename:
                    with open(filename, "w") as file:
                        file.write(
                            f"Ошибка в функции {func.__name__}: {ex.__class__.__name__}. Параметры: {args}, {kwargs}"
                        )
                else:
                    print(f"Ошибка в функции {func.__name__}: {ex.__class__.__name__}. Параметры: {args}, {kwargs}")

        return wrapper

    return decorator
