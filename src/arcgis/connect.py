from arcgis.gis import GIS
import os

def connect_arcgis() -> GIS:
    """
    Secure ArcGIS connection using environment variables.
    """
    return GIS(
        url=os.getenv("ARCGIS_URL"),
        username=os.getenv("ARCGIS_USERNAME"),
        password=os.getenv("ARCGIS_PASSWORD")
    )
