class IMM(object):
    def __init__(self,dic_path):
        self.dictionary = set()
        self.maximum = 0
        print("hello!!!!")
        with open(dic_path,'r',encoding='utf8') as f:
            for line in f:
                #去除字符串中的空格，转换字符
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                if len(line) > self.maximum:
                    self.maximum = len(line)

    def cut(self,text):
        result = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maximum,0,-1):
                if index - size < 0:
                    continue
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        return result[::-1]
#
def main():
    print("hi!!!!!!!!")
    text = "南京市长江大桥"
    tokenizer = IMM('D:/WorkSpace/PyCharm/intelligent/com/datas/imm_dic.utf8')
    print(tokenizer.cut(text))



# if __name__ == "__main__":
# m = main()


# class IMM(object):
#     def __init__(self, dic_path):
#         self.dictionary = set()
#         self.maximum = 0
#         # 读取词典
#         with open(dic_path, 'r', encoding='utf8') as f:
#             for line in f:
#                 line = line.strip()
#                 if not line:
#                     continue
#                 self.dictionary.add(line)
#                 if len(line) > self.maximum:
#                     self.maximum = len(line)
#
#     def cut(self, text):
#         result = []
#         index = len(text)
#         while index > 0:
#             word = None
#             for size in range(self.maximum, 0, -1):
#                 if index - size < 0:
#                     continue
#                 piece = text[(index - size):index]
#                 if piece in self.dictionary:
#                     word = piece
#                     result.append(word)
#                     index -= size
#                     break
#             if word is None:
#                 index -= 1
#         return result[::-1]
#
#
# def main():
#     text = "南京市长江大桥"
#
#     # tokenizer = IMM('./data/imm_dic.utf8')
#     tokenizer = IMM('D:/WorkSpace/PyCharm/intelligent/com/datas/words.utf8')
#     print(tokenizer.cut(text))

main()