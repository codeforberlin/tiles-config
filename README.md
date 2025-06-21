tiles.codedefor.de
==================

This repo hold the server config for [tiles.codedefor.de](https://tiles.codefor.de), which
uses the [GDAL-Tiles-API](https://github.com/codeforberlin/gdal-tiles-api) to serve
[tiles](https://wiki.openstreetmap.org/wiki/Tiles) to different maps, e.g.:

* https://luftbilder.berlin.codefor.de/
* https://maps.berlin.codefor.de/
* https://www.blnmap.de/

This repo replaces https://github.com/codeforberlin/tilestache-config.

The config for https://mapproxy.codefor.de/ is maintained separately in https://github.com/codeforberlin/mapproxy-config.

The configuration format is described [here](https://github.com/codeforberlin/gdal-tiles-api?tab=readme-ov-file#usage)
and there entries for the different maps split into `.toml` files in `config.d`.

The `bin` drectory holds several helper scripts to create derived configuration files:

* `bin/build_maps_config.py` creates a config JSON file for
  https://github.com/codeforberlin/luftbilder.berlin.codefor.de or
  https://github.com/codeforberlin/maps.berlin.codefor.de
* `bin/build_titiler_list.py` creates a flat list to be used with [TiTiler](https://developmentseed.org/titiler/)
* `bin/build_histomap_config.py` was used to create `config.d/10-histomap.toml` from the directory containing the images.
