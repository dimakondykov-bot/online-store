import pytest
from src.smartphone import Smartphone


def test_smartphone_init():
    """Проверяем, что смартфон правильно инициализируется."""
    smartphone = Smartphone(
        name="samsung",
        description="смартфон",
        price=78500,
        quantity=3,
        efficiency="snapdragon 8 gen 3",
        model="samsung s24 plus",
        memory=256,
        color="Чёрный"
    )
    assert smartphone.name == "samsung"
    assert smartphone.description == "смартфон"
    assert smartphone.price == 78500
    assert smartphone.quantity == 3
    assert smartphone.efficiency == "snapdragon 8 gen 3"
    assert smartphone.model == "samsung s24 plus"
    assert smartphone.memory == 256
    assert smartphone.color == "Чёрный"


def tets_smartphone_add_same_class():
    """Проверяем сложение двух смартфонов одного класса."""
    smartphone1 = Smartphone(
        name="Phone 1",
        description="Test 1",
        price=15000, quantity=5,
        efficiency=80,
        model="A1",
        memory=256,
        color="white",
    )

    smartphone2 = Smartphone(
        name="Phone 2",
        description="Test 2",
        price=23000, quantity=2,
        efficiency=95,
        model="A1",
        memory=512,
        color="green",
    )

    resalt = smartphone1 + smartphone2
    assert resalt == 121000


def test_smartphone_add_different_type_raises_type_error():
    """Проверяем, что при сложении с другим типом выбрасывается TypeError."""
    phone = Smartphone(
        name="Phone",
        description="Test",
        price=100,
        quantity=1,
        efficiency=80,
        model="X",
        memory=64,
        color="blue",
    )

    class Other:
        pass

    with pytest.raises(TypeError):
        _ = phone + Other()
