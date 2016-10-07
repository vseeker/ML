# encoding=utf8
import re
import get_the_best_match as gbm
import str2unicode_dict as sd
t = u'无法删除 路由lkjlkpkpkk"An unknown exception occurred." jwefokwljof123 "12321434"id:29384'
z = u'无法删除路由"An unknown exception occurred."'
c = u'Security group rule already exists. Rule id: is 04f1e406-d4d0-4766-9378-77bd7ed9e650. aaa. '
d = u'为网络‘21’创建子网“192.168.11.0／24”失败，Invalid input for operation: Requested subnet with ' \
    u'cidr:192.168.11.0/24 for network: 04f1e406-d4d0-4766-9378-77bd7ed9e650db overlaps with another subnet.  '
chn = re.compile(ur'[\,\u4e00-\u9fa5]*')  # 仅中文
non_chn = re.compile(ur'[^\，\u4e00-\u9fa5]*')  # 非中文
number = re.compile(ur'[\s0-9_-]*')  # 仅数字
english = re.compile(ur'[\sA-Za-z_-]*')  # 仅英文
english_contained = re.compile(ur'[\sA-Za-z]+')  # 必须包含英文,+至少含有一个英文字符
#  print t,type(t)
#  m = re.match(ur'^[0-9A-Za-z\u4e00-\u9fa5_.-]+$', u'张兵兵')
m = re.findall(ur'[\u4e00-\u9fa5]+', t)
#  m = re.search(ur'^[\u4e00-\u9fa5]+$', u'无法删除路由')
#  m = re.match(ur"^[\u4e00-\u9fa5_a-zA-Z0-9]+$", t)


english2chinese_dict = {u"An unknown exception occurred": u"发生未知错误",
                        u'id:': u'序列号:',
                        }


def get_str_with_regex(strings=None, regex=None):
    if not strings or not regex:
        print "you don't give strings or regex, please check it "
    str_matched_regex = [el for el in regex.findall(strings) if len(el) > 1]
    # print str_matched_regex
    return str_matched_regex if str_matched_regex else None


def translate(strings=None, translate_dic=english2chinese_dict):
    """
    将输入的可能需要翻译的strings进行翻译,并返回翻译后并且拼装好的unicode字符串
    :param strings: 输入串
    :param translate_dic:匹配模版:英文 ->{"hello (.*)":_(你好 %s)}
    :return: 拼装好的unicode串
    """
    #  逐层判断是否需要进行翻译
    if not strings:
        print 'the string is null'
        return
    list_str_need_to_be_translated= get_str_need_to_be_translated(strings)
    if not list_str_need_to_be_translated:
        print 'the string do not need  to be translate'
        return
    regex_list = [item for item in translate_dic.iterkeys()]
    print 'regex_list', regex_list
    for el in list_str_need_to_be_translated:
        # 在字典中找到匹配率最高的那个键值,然后进行利用该键值模版参数提取,最后利用该键对应的值和参数进行格式化翻译
        best_match = gbm.get_the_best_match_item(el, regex_list)  # 找到最为匹配的那一个(依据的是字符串的匹配度,粗匹配)
        match_result = re.match(best_match, el)  # 利用re精匹配并且得到参数列表
        print match_result.groups()

    return strings



def get_str_need_to_be_translated(strings=None):
    """
    首先将strings进行非中文字串的提取,然后进行包含英文的字串的提取(该字串即是需要翻译的字串)
    :param strings: 输入的需要部分翻译的字串
    :return: 需要翻译的那部分组成的list
    """
    non_chn = re.compile(ur'[^\，\u4e00-\u9fa5]*')  # 非中文
    english_contained = re.compile(ur'[\sA-Za-z]+')  # 必须包含英文,+至少含有一个英文字符0
    list_sub_str_of_non_chn = get_str_with_regex(strings=strings, regex=non_chn)
    list_sub_str_of_english_contained = []
    for el in list_sub_str_of_non_chn:
        if english_contained.match(el):
            list_sub_str_of_english_contained.append(el)
            # print el
    # print list_sub_str_of_english_contained
    return list_sub_str_of_english_contained if len(list_sub_str_of_english_contained) else None


# print get_str_with_regex(d, non_chn)
# for el in get_str_with_regex(d, non_chn):
#     print get_str_with_regex(el, english_contained)

# print get_str_need_to_be_translated(d)

# print translate(z, english2chinese_dict)

translate(strings=d, translate_dic=sd.dict_regex_and_str)
