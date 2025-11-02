import re
from pathlib import Path


def metadata(base_path):
    base_path = Path(base_path) / 'roi' / 'dev'
    real_path = base_path / 'real'
    spoof_path = base_path / 'spoof'

    pattern = r"([0-9]+)_([0-9]+)_([0-9]+)_([0-9]+)_([0-9]+).bmp"
    data = {'real': [], 'spoof': []}
    for file in real_path.glob("**/*.bmp"):
        match = re.match(pattern, file.name)
        if match:
            data['real'].append({
                'subject': int(match.group(1)),
                'finger': int(match.group(2)),
                'session': int(match.group(3)),
                'shot': int(match.group(4)),
                'light': int(match.group(5)),
                'path': str(file)
            })

    for file in spoof_path.glob("**/*.bmp"):
        match = re.match(pattern, file.name)
        if match:
            data['spoof'].append({
                'subject': int(match.group(1)),
                'finger': int(match.group(2)),
                'session': int(match.group(3)),
                'shot': int(match.group(4)),
                'light': int(match.group(5)),
                'path': str(file)
            })
    return data