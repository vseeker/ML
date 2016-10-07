# encoding=utf8
''' get the english which of the the biggest match-rate which calculate by the Levenshtein library '''


import Levenshtein as lvn
from django.utils.translation import ugettext_lazy as _

translate_list = [_("Bad request"),
                  _("Unauthorized"),
                  _("Forbidden"),
                  _("Not found"),
                  _("Method Not Allowed"),
                  _("Method Not Acceptable"),
                  _("Proxy Authentication Required"),
                  _("Request Timeout"),
                  _("Conflict"),
                  _("Gone"),
                  _("Length Required"),
                  _("Over limit"),
                  _("Security group rule already exists. Rule id is 04f1e406-d4d0-4766-9378-77bd7ed9e650."),
                  ]
x = "good morning"
'''
tmp = _("Over limit", "Length Required", x).__dict__.get('_proxy____args', None)
print tmp, type(tmp), type(tmp[0])
# ('Over limit', 'Length Required', 'good morning') <type 'tuple'> <type 'str'>
print type(_("Over limit", "Length Required", x))
# <class 'django.utils.functional.__proxy__'>
'''

def get_english(your_string=None, search_list=None):
    if not your_string or not search_list:
        print "please input your_string or search_list"
        return 0
    the_rate_of_most_match = 0.0
    for index, el in enumerate(search_list):
        match_rate = lvn.ratio(your_string, el)
        if match_rate > the_rate_of_most_match:
            the_rate_of_most_match = match_rate
            the_index_of_most_match = index
        print el, match_rate, the_index_of_most_match
    # return search_list[the_index_of_most_match]
    print "result", search_list[the_index_of_most_match]

# get_english(your_string=u"Security group rule already exists. Rule id is %(id)s.", search_list=translate_list)


def get_the_best_match_item(your_string=None, search_list=None):
    if not your_string or not search_list:
        print "please input your_string or search_list to be matched with !"
        return 0
    the_rate_of_most_match = 0.0
    for index, el in enumerate(search_list):
        # print your_string, type(your_string)
        # print el, type(el)
        match_rate = lvn.ratio(your_string, el)
        if match_rate > the_rate_of_most_match:
            the_rate_of_most_match = match_rate
            the_index_of_most_match = index
        # print el, match_rate, the_index_of_most_match
    # return search_list[the_index_of_most_match]
    print "the best_match ******--> :", search_list[the_index_of_most_match]
    return search_list[the_index_of_most_match]
