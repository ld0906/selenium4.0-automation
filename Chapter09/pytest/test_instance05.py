import pytest

class Refill_Oil:
    def __init__(self,oil_litre):
            self.oil_litre = oil_litre


class Car(Refill_Oil):
    def get_oil_litre(self):
        return self.oil_litre



@pytest.fixture
def get_oil_litre_for_cars():
    return [Car(11),Car(12),Car(20)]



def test_oil_litres(get_oil_litre_for_cars):
    car_list = get_oil_litre_for_cars
    for car in car_list:

        assert car.get_oil_litre() > 10