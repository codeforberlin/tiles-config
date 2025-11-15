import argparse

from gdal_tiles_api.config import load_config

parser = argparse.ArgumentParser()
parser.add_argument("--include", nargs="*")
parser.add_argument("--exclude", nargs="*")

args = parser.parse_args()

config = load_config()

lines = []
for map_settings in config.maps:
    if args.include and not any(
        str(map_settings.path).startswith(s) for s in args.include
    ):
        continue

    if args.exclude and any(str(map_settings.path).startswith(s) for s in args.exclude):
        continue

    lines.append(
        f"http://localhost:5000/cog/viewer?url={map_settings.get_dataset_path(config.tiles.path)}"
    )

string = "\n".join(lines)
print(string)
