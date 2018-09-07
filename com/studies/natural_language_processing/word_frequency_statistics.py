import argparse
from heapq import nlargest
from collections import defaultdict
from pyltp import SentenceSplitter
import jieba.analyse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath',help='File name of text to summarize')
    parser.add_argument('-l','--length',default=4,help='Number of sentences to return')
    args = parser.parse_args()
    return args

def cut_sentence(content):
    content.split(',')

def read_file(path):
    try:
        with open(path,'r',encoding="UTF-8") as file:
            return file.read()
    except IOError as e:
        print("Fatal Error: File ({}) could not be locaeted or is not readable.".format(path))

def sanitize_input(data):
    replace = {ord('\f'): ' ',ord('\t'): ' ',ord('\n'): ' ',ord('\r'): None}
    return data.translate(replace)

def tokenize_content(content):
    jieba.analyse.set_stop_words("D:/WorkSpace/data/Natural/test/stop_words.txt")
    tags = jieba.analyse.extract_tags(content,topK=10,withWeight=True)
    word_tokens_rank = dict()
    for tag in tags:
        word_tokens_rank[tag[0]] = tag[1]
    return[
        SentenceSplitter.split(content),word_tokens_rank
    ]

def score_tokens(words_tokens_rank,sentence_tokens):
    ranking = defaultdict(int)
    for i, sentence in enumerate(sentence_tokens):
        for word in jieba.cut(sentence.lower(),cut_all=False):
            if word in words_tokens_rank:
                ranking[i] += words_tokens_rank[word]
    return ranking

def summarize(ranks,sentences,length):
    if int(length) > len(sentences):
        print("Error, more sentences requestend than available. Use --l (--length) flag to adjust.")
        exit()
    indexes = nlargest(length,ranks,key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indexes)]
    return ' '.join(final_sentences)

def main():
    args = parse_arguments()
    # print(args)
    # filepath = "D:/WorkSpace/data/Natural/test/Precision-Strike-In-The-Us.txt"
    content = read_file(args.filepath)
    # content = read_file(filepath)
    content = sanitize_input(content)
    sentence_tokens, word_tokens_rank = tokenize_content(content)
    sentence_ranks = score_tokens(word_tokens_rank, sentence_tokens)
    return summarize(sentence_ranks, sentence_tokens, args.length)
    # return summarize(sentence_ranks, sentence_tokens, filepath)

if __name__ == "__main__":
    print(main())


"""
运行：
打开命令行，执行下面命令
python D:/WorkSpace/PyCharm/intelligent/com/studies/natural_language_processing/word_frequency_statistics.py

python D:/WorkSpace/PyCharm/intelligent/com/studies/natural_language_processing/word_frequency_statistics.py D:/WorkSpace/data/Natural/test/Precision-Strike-In-The-Us.txt

"""