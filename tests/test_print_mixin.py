from src.print_mixin import PrintMixin
import builtins


class TemporaryClass(PrintMixin):
    """Временный класс для проверки миксин"""

    def __init__(self, *args, **kwargs):
        self.name = "Test"
        self.description = "Description"
        self.price = 35
        self.quantity = 500
        super().__init__()


def test_print_mixin():
    obj = TemporaryClass()
    assert repr(obj) == "TemporaryClass(Test, Description, 35, 500)"


def test_print_mixin_print(monkeypatch):
    printed = []

    def fake_print(value):
        printed.append(value)

        monkeypatch.setattr(builtins,"print", fake_print)

        TemporaryClass()
        assert printed == ["TemporaryClass(Test, Description, 10, 5)"]
