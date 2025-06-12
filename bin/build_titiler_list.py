from gdal_tiles_api.config import load_config

config = load_config()

lines = []
for map_settings in config.maps:
    lines.append(
        f"http://localhost:5000/cog/viewer?url={map_settings.get_dataset_path(config.tiles.path)}"
    )

string = '\n'.join(lines)
print(string)
