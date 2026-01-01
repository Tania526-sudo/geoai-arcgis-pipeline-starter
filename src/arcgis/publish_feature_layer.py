import geopandas as gpd

def publish_feature_layer(gis, gdf: gpd.GeoDataFrame, title: str):
    """
    Publish GeoDataFrame as Hosted Feature Layer.
    """
    item = gis.content.import_data(gdf)
    item.update(item_properties={"title": title})
    return item
