import geopandas as gpd
import numpy as np

def add_spatial_features(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Build baseline spatial features for GeoAI.
    """
    gdf = gdf.copy()
    gdf["has_name"] = gdf["name"].notna().astype(int)
    gdf["has_address"] = gdf["full_address"].notna().astype(int)
    return gdf
