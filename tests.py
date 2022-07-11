from shapely.geometry import Point, Polygon
from shapely_utils import *

def test_azimuth():
    """Test azimuth"""
    p1 = Point(0,0)
    p2 = Point(8,10)
    azimuth1 = abs(azimuth(p1, p2))
    print('Azimuth: ', azimuth1)
    assert azimuth1 == 38.65980825409009


def test_scale():
    """Test scale geometry"""

    polygon = Polygon([(2.2, 4.0), (7.2, -25.0), (9.0, -2.0)])
    scaled_polygon = scale_geom(polygon, 1.5)

    print( 'Input polygon: ', wkt.dumps(polygon))
    print( 'Scaled polygon: ',wkt.dumps(scaled_polygon))
    assert wkt.dumps(scaled_polygon) == 'POLYGON ((0.2333333333333343 9.8333333333333321, 7.7333333333333343 -33.6666666666666643, 10.4333333333333336 0.8333333333333330, 0.2333333333333343 9.8333333333333321))'
