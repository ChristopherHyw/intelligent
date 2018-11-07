
def get_content(path):
    with open(path,'r',encoding='utf8',errors='ignore') as f:
        content = ''
        for l in f:
            l = l.strip()
            content += l
        return content

def get_TF(words, topK = 10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w,0) + 1
    return sorted(tf_dic.items(),key=lambda x: x[1],reverse=True)[:topK]

def stop_words(path):
    with open(path,encoding='utf8') as f:
        return [l.strip() for l in f]

def main():
    import glob
    import random
    import jieba

    files = glob.glob('D:/WorkSpace/PyCharm/intelligent/com/datas/wordcount.txt')
    corpus = [get_content(x) for x in files]

    sample_inx = random.randint(0,len(corpus))
    # split_words = list(jieba.cut(corpus[sample_inx]))
    split_words = [x for x in jieba.cut(corpus[sample_inx]) if x not in stop_words('D:/WorkSpace/PyCharm/intelligent/com/datas/stop_words.utf8')]
    # print('样本')
    # print('样本')
    print('topK：'+str(get_TF(split_words,topK=5)))

main()