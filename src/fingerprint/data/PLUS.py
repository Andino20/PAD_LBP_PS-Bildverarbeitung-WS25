import re
from pathlib import Path


def metadata(base_path):
    base_path = Path(base_path)
    real_path = base_path.joinpath("real")
    spoof_path = base_path.joinpath("spoof")

    pattern = r"(.+)_(PALMAR|DORSAL)_([0-9]+)_([0-9]+)_([0-9]+)_([0-9]+).png"
    data = {'real': [], 'spoof': []}
    for file in real_path.glob("**/*.png"):
        match = re.match(pattern, file.name)
        if match:
            data['real'].append({
                'scanner': match.group(1),
                'side': match.group(2),
                'subject': int(match.group(3)),
                'session': int(match.group(4)),
                'finger': int(match.group(5)),
                'imageId': int(match.group(6)),
                'path': str(file)
            })

    for file in spoof_path.glob("**/*.png"):
        match = re.match(pattern, file.name)
        if match:
            data['spoof'].append({
                'scanner': match.group(1),
                'side': match.group(2),
                'subject': int(match.group(3)),
                'session': int(match.group(4)),
                'finger': int(match.group(5)),
                'imageId': int(match.group(6)),
                'path': str(file)
            })
    return data
