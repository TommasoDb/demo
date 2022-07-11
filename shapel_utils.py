from shapely.geometry import Point, Polygon
from shapely.geometry.base import BaseGeometry  # Base geometry class for validation purpose
from shapely import geos, wkb, wkt, affinity
import math


def azimuth(point1, point2):
    """Calculates the Azimuth between 2 points, (interval 0-180).

    :param: point1: First point in shapely format
    :type: Point
    :param: point2: Second point in shapely format
    :type: Point
    :rtype: float
    :return:
    """
    angle = math.atan2(point2.x - point1.x, point2.y - point1.y)
    return math.degrees(angle) if angle > 0 else math.degrees(angle) + 180


def scale_geom(geom, scale_factor):
    """Scales the input geometry preserving the middle point by moving first the geometry to 0,0 and moving it back after
    the scaling.

    :param: Shapely geometry (all types)
    :type: BaseGeometry
    :param: Scale factor, must be a number
    :type: float
    :rtype: BaseGeometry
    """

    x = geom.centroid.x
    y = geom.centroid.y
    result_geometry = geom
    result_geometry = affinity.translate(result_geometry, xoff=-1 * x, yoff=-1 * y, zoff=0.0)
    result_geometry = affinity.scale(result_geometry, xfact=scale_factor, yfact=scale_factor, zfact=1.0, origin=Point(0, 0))
    result_geometry = affinity.translate(result_geometry, xoff=x, yoff=y, zoff=0.0)
    return result_geometry


def shapely_to_wkt(geom):
    """Convert a Shapely geometry to WKT
    :rtype str
    """
    if issubclass(type(geom), BaseGeometry):
        return wkt.dumps(geom)
    else:
        return geom
