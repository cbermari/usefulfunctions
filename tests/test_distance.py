# tests/test_distance.py
from usefulfunctions.distance import haversine
import numpy as np

def test_haversine_output_type():
    #testing distance le Wagon to UVa
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 41.6626268,-4.7099289
    assert type(haversine(lon1, lat1, lon2, lat2)) == float

def test_haversine_output_value():
    #testing distance le Wagon to UVa
    lat1, lon1 = 48.865070, 2.380009
    lat2, lon2 = 41.6626268,-4.7099289
    np.testing.assert_allclose(1070.336581924166,
                               haversine(lon1, lat1, lon2, lat2), rtol=1e-1)
