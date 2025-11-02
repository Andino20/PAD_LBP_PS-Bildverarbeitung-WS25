from fingerprint.data import PLUS, IDIAP, SCUT
from skimage.feature import local_binary_pattern
from skimage import io
from functools import reduce

data = PLUS.metadata('../data/Data_FV_Spoofing_WS2025_26/PLUS')
# data = IDIAP.metadata('../data/Data_FV_Spoofing_WS2025_26/IDIAP')
# data = SCUT.metadata('../data/Data_FV_Spoofing_WS2025_26/SCUT')

spoofs = {(f['subject'], f['finger']) for f in data['spoof']}
real_paths = [f['path'] for f in data['real'] if (f['subject'], f['finger']) in spoofs]

def hist(lbp):
    hist = [0] * 256
    for v in lbp.ravel():
        hist[int(v)] += 1
    return [x / lbp.size for x in hist]

for p in real_paths:
    image = io.imread(p)
    lbp = local_binary_pattern(image, P=8, R=1)
    print(hist(lbp))