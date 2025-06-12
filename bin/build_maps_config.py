import json

from gdal_tiles_api.config import load_config

config = load_config()

data = {
    'brand': {
        'text': 'maps.berlin.codefor.de',
        'href': 'https:/maps.berlin.codefor.de'
    },
    'view': {
        'center': [52.51, 13.37628],
        'zoom': 12
    },
    'maps': []
}

for map_settings in config.maps:
    if 'href' in map_settings.attribution:
        attribution = '<a href="{href}" _target="blank">{text}</a>'.format(**map_settings.attribution)
    else:
        attribution = map_settings.attribution.get('text', '')

    data['maps'].append({
        'name': map_settings.name,
        'url': map_settings.get_url(host=config.tiles.host),
        'options': {
            'attribution': attribution,
            'minZoom': 5,
            'maxZoom': 20
        }
    })

string = json.dumps(data, indent=2, ensure_ascii=False)
print(string)
