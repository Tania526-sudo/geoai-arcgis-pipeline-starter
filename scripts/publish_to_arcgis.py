from src.arcgis.connect import connect_arcgis
from src.arcgis.publish_feature_layer import publish_feature_layer

def main():
    gis = connect_arcgis()
    print("Connected to ArcGIS:", gis.properties.portalName)

if __name__ == "__main__":
    main()
