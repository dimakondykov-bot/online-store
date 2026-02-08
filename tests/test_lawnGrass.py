import pytest

from src.lawnGrass import LawnGrass


def test_lawngrass_init():
    """Проверяем, что объект LawnGrass правильно инициализируется."""
    grass = LawnGrass(
        name="GreenField",
        description="Premium lawn grass",
        price=1500,
        quantity=10,
        country="Netherlands",
        germination_period=14,
        color="green",
    )

    assert grass.name == "GreenField"
    assert grass.description == "Premium lawn grass"
    assert grass.quantity == 10
    assert grass.country == "Netherlands"
    assert grass.germination_period == 14
    assert grass.color == "green"
    # __price приватный — проверим косвенно в тесте сложения


def test_lawngrass_add_same_type():
    """Проверяем корректность сложения двух объектов LawnGrass."""
    grass1 = LawnGrass(
        name="Трава 1",
        description="Test 1",
        price=1300,
        quantity=3,
        country="США",
        germination_period=7,
        color="зёленая",
    )

    grass2 = LawnGrass(
        name="Трава 2",
        description="Test 2",
        price=900,
        quantity=2,
        country="Канада",
        germination_period=5,
        color="тёмно зелёная",
    )

    result = grass1 + grass2

    assert result == 5700


def test_lawngrass_add_different_type_raises_type_error():
    """Проверяем, что при сложении с объектом другого типа выбрасывается TypeError."""
    grass = LawnGrass(
        name="Трава",
        description="Test",
        price=850,
        quantity=1,
        country="Бразилия",
        germination_period=6,
        color="Светло зелёная",
    )

    class Other:
        pass

    with pytest.raises(TypeError):
        _ = grass + Other()
