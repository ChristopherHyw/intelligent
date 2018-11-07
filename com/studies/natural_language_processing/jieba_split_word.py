import jieba

sent = '自然语言处理是计算机科学领域与人工智能领域中的一个重要方向。\
它研究能实现人与计算机之间用自然语言进行有效通信的各种理论和方法。\
自然语言处理是一门融语言学、计算机科学、数学于一体的科学。'

# seg_list = jieba.cut(sent,cut_all=True)
# print('全模式',' '.join(seg_list))
#
# seg_list = jieba.cut(sent,cut_all=False)
# print('精确模式',' '.join(seg_list))
#
# seg_list = jieba.cut(sent)
# print('默认模式',' '.join(seg_list))
#
# seg_list = jieba.cut_for_search(sent)
# print('搜索模式',' '.join(seg_list))


