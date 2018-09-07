import re

# text_string = '文本最重要的来源无疑是网络。\
# 我们要把网络中的文本获取成一个文本数据库。\
# 利用爬虫爬抓取到网络中的信息。\
# 爬取的策略有广度爬取和深度爬取。\
# 根据用户需求，爬虫可以有主题爬虫和通用爬虫之分。'

# regex = '爬虫'
# regex = '文本'
# regex = '爬.'
# regex = '^文本'
# regex = '网络$'
#
# p_string = text_string.split('。')
#
# for line in p_string:
#     if re.search(regex,line) is not None:
#         print(line)

# text_string = ['[重要的]今年第七号台风23日登陆广东东部沿海地区',
#                '上海发布车库销售监管通知：违规者暂停网签资格',
#                '[紧要的]中国对印度连发强硬信息印度急切需要结束对峙']
#
# regex = '^\[[重紧]..\]'
#
# for line in text_string:
#     if re.search(regex,line) is not None:
#         print(line)

# if re.search("\\\\","I have one nee\dle") is not None:
# if re.search(r"\\","I have one nee\dle") is not None:
#     print("match it")
# else:
#     print("no match")

# strings = ['War of 1812','There are 5280 feet to a mile',
#            'Happy New Year 2016!']
# year_strings = []
# for string in strings:
#     if re.search('[1-2][0-9]{3}',string):
#         year_strings.append(string)
#     print(year_strings)

# lists = re.findall("[a-z]","abc1234")
# print(lists)

years_string = '2016 was a good year, but 2017 will be better!'
years = re.findall('[2][0-9]{3}',years_string)
print(years)