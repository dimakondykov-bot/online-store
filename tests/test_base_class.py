import pytest
from src.base_product import BaseProduct



def test_base_product_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct()


def test_child_without_new_product_fails():
    class BadChild(BaseProduct):
        pass

    with pytest.raises(TypeError):
        BadChild()


def test_child_with_new_product_ok():
    class GoodChild(BaseProduct):
        @classmethod
        def new_product(cls, *args, **kwargs):
            return "ok"

    obj = GoodChild()
    assert obj.new_product() == "ok"
