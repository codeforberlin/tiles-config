import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument('PATH')
parser.add_argument('HISTOMAP_PATH')

args = parser.parse_args()

lines = []
for file_path in Path(args.PATH).glob('*.tif'):
    lines += [
        '[[maps]]',
        f'name = "HistoMap Kartenblatt {file_path.stem}"',
        f'path = "{Path(args.HISTOMAP_PATH) / file_path.stem}"',
        f'dataset = "{Path(args.HISTOMAP_PATH) / file_path.name}"',
        'attribution.text = "Senatsverwaltung für Stadtentwicklung, Bauen und Wohnen Berlin / Landesarchiv Berlin / Histomap Berlin"',
        'attribution.href = "https://histomapberlin.de"',
        ''
    ]

string = '\n'.join(lines)
print(string)
