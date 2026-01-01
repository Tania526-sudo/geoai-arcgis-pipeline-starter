from dataclasses import dataclass

@dataclass
class PipelineConfig:
    bbox = (30.38, 50.40, 30.62, 50.52)
    crs_wgs84 = "EPSG:4326"
    crs_projected = "EPSG:3857"

    raw_dir = "data/00_raw"
    clean_dir = "data/01_clean"
    qaqc_dir = "data/02_qaqc"

    arcgis_url = "https://www.arcgis.com"
