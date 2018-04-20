
yuyinutils = __import__("yuyinutils")
get_wavs_lables = yuyinutils.get_wavs_lables

wav_path = ""
label_file = ""

wav_files, labels = get_wavs_lables(wav_path, label_file)
print(wav_files[0],labels[0])
print("wav: ", len(wav_files), "label: ", len(labels))

from collections import Counter
from .yuyinutils import *

all_words = []
for label in labels:
    all_words += [word for word in label]
counter = Counter(all_words)
words = sorted(counter)
words_size = len(words)
word_num_map = dict(zip(words,range(words_size)))

print('字体大小：', words_size)

n_input = 26
n_context = 9
sparse_tuple_to_texts_ch = yuyinutils.sparse_tuple_to_texts_ch
ndarray_to_text_ch = yuyinutils.ndarray_to_text_ch
get_audio_and_transcritych = yuyinutils.tet_audio_and_transcriptch
pad_sequences = yuyinutils.pad_sequences
sparse_tuple_from = yuyinutils.sparse_tuple_from
batch_size = 8

def next_batch(labels,start_idx=0,batch_size=1,wav_files=wav_files):
    filesize = len(labels)
    end_idx = min(filesize, start_idx + batch_size)
    idx_list = range(start_idx, end_idx)
    txt_labels = [labels[i] for i in idx_list]
    wav_files = [wav_files[i] for i in idx_list]
    (source, audio_len, target, transcript_len) = get_audio_and_transcriptch(None,txt_labels)


