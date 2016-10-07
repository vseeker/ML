# coding=utf-8
import os


def get_messages():
    with open('messages_complete.txt', 'w+') as mf:
        with open('all_class_complete.txt') as cf:
            for ln in cf:
                if ln.rfind("=") > 0:
                    messages = "kk"
                    messages = ln[ln.rfind("=")+1:]
                    # if messages.rfind("("):
                        # messages = messages[messages.rfind("("):-1]
                    # print type(messages)
                    # break
                    if len(messages) > 1:
                        mf.writelines(messages)





def get_final_messages():
    with open('final_messages_complete.txt', 'w+') as ff:
        with open('messages_complete.txt') as mf:
            for ln in mf:
                if len(ln) > 2:
                    # print ln[2]
                    ln = ln[1:-1]
                    if ln[1] == '(':
                        ln = ln[2:-1]
                        # print ln
                    if len(ln)>2:
                        ff.writelines(ln+'\n')



# get_messages()
#
get_final_messages()

