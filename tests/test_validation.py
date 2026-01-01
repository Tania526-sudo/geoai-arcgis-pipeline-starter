import geopandas as gpd
from shapely.geometry import Point
from src.quality.validate_geodata import validate_geometry

def test_geometry_validation():
    gdf = gpd.GeoDataFrame(
        geometry=[Point(0, 0)],
        crs="EPSG:4326"
    )
    out = validate_geometry(gdf)
    assert out.geometry.is_valid.all()
