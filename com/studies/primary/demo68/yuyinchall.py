
yuyinutils = __import__("yuyinutils")
get_wavs_lables = yuyinutils.get_wavs_lables

wav_path = ""
label_file = ""

wav_files, labels = get_wavs_lables(wav_path, label_file)
print(wav_files[0],labels[0])
print("wav: ", len(wav_files), "label: ", len(labels))

from collections import Counter
from .yuyinutils import *

