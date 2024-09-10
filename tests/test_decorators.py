from src.decorators import log


def test_log_console(capsys):
    """Тестирует работу декорированной функции с выводом в консоль"""

    @log()
    def test_func(x, y):
        return x + y

    test_func(2, 5)
    captured = capsys.readouterr()
    assert captured.out == "test_func работает\n"


def test_log_file():
    """Тестирует работу декорированной функции с выводом в файл"""

    @log(filename="mylog.txt")
    def test_sum(a, b):
        return a + b

    test_sum(4, 5)
    with open("mylog.txt", "r") as file:
        line_to_read = file.read()
    assert line_to_read == "Функция test_sum работает"


# def test_error(capsys):
#     '''Тестирует вызов исключения'''
#     @log()
#     def testing_error(x, y):
#         raise ValueError("Test error")
