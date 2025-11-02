
from fingerprint.data import PLUS, IDIAP, SCUT

data = PLUS.metadata('../data/Data_FV_Spoofing_WS2025_26/PLUS')
#data = IDIAP.metadata('../data/Data_FV_Spoofing_WS2025_26/IDIAP')
#data = SCUT.metadata('../data/Data_FV_Spoofing_WS2025_26/SCUT')
print(data['spoof'])