import re
from pathlib import Path

def metadata(base_path):
    base_path = Path(base_path).joinpath('cropped').joinpath('dev')
    real_path = base_path.joinpath("real")
    spoof_path = base_path.joinpath("spoof")

    pattern = r"([0-9]+)_(L|R)_([0-9]+).png"
    data = {'real': [], 'spoof': []}
    for file in real_path.glob("**/*.png"):
        match = re.match(pattern, file.name)
        if match:
            data['real'].append({
                'subject': int(match.group(1)),
                'side': match.group(2),
                'session': int(match.group(3)),
                'path': str(file)
            })

    for file in spoof_path.glob("**/*.png"):
        match = re.match(pattern, file.name)
        if match:
            data['spoof'].append({
                'subject': int(match.group(1)),
                'side': match.group(2),
                'session': int(match.group(3)),
                'path': str(file)
            })
    return data