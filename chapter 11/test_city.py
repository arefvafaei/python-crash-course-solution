# --------------------- 11-1
# --------- FAILED ---------
# from city_function import city_country
# def test_city_country():
#     city = city_country("santiago","chile")
#     assert city == "santiago, chile - population 5000000"
# --------- SUCCESS ---------
from city_function import city_country
def test_city_country():
    city = city_country("santiago","chile",5000000)
    assert city == "santiago, chile - population 5000000"
