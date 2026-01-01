import geopandas as gpd

def validate_geometry(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Validate and repair geometries.
    """
    gdf = gdf.copy()
    gdf["flag_invalid_geom"] = ~gdf.geometry.is_valid
    gdf.loc[gdf["flag_invalid_geom"], "geometry"] = (
        gdf.loc[gdf["flag_invalid_geom"], "geometry"].buffer(0)
    )
    return gdf
