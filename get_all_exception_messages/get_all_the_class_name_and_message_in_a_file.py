# coding=utf-8
import os
import linecache


# list = GetFileList('D:\\workspace\\PyDemo\\fas', [])

def get():
    # 提取出path.txt文件所有文件的类名以及message，存到all_class.txt
    with open('all_class.txt', 'w+') as cf:
        with open("path.txt") as f:
            for e in f:
                with open(e[:-1]) as fp:
                    ln_count = 0
                    for ln in fp:
                        ln_count += 1
                        if 'class' in ln and ln.rfind('class') == 0:
                            # cf.writelines(ln.split(' ')[1].split('(')[0]+'\n')
                            cf.writelines(ln.split(' ')[1])
                        if ln.rfind('message') == 4:
                            # if ln.rfind(')')
                            cf.writelines(ln + '\n')


def get_all_message_in_the_file(file_name="your_file"):
    with open('all_class_complete.txt', 'a+') as cf:
        with open(file_name) as f:
            ln_count = 0
            for ln in f:
                ln_count += 1
                if len(ln) > 2:
                    if 'class' in ln and ln.rfind('class') == 0:
                        cf.writelines(ln)
                        continue
                        # cf.writelines(ln.split(' ')[1].split('(')[0]+'\n')
                        # cf.writelines(ln.split(' ')[1])
                    # print ln.rfind('message')
                    if ln.rfind('message') == 4:
                        # print ln.rfind('('), ln.rfind(')')
                        if ln.rfind('(') != -1 and ln.rfind(')') != -1 and ln.rfind('"') and (ln.rfind(')') > ln.rfind('"')):  # 带括号的message只占一行，直接拿出
                            cf.writelines(ln + '\n')
                            continue
                        if ln.rfind('"') != -1 and ln.rfind('"') != -1 and ln.rfind('(') == -1:  # 不带括号直接拿出，这种情况只考虑一行的情况
                            cf.writelines(ln + '\n')
                            continue

                        if ln.rfind('(') != -1 and ln.rfind(')') == -1:  # 当前行只有左括号，即下面还有注释
                            # 则剩下只有两种情况，最后一行含有右括号（当然也有双引号），非最后一行只含" "
                            # 所以拿到所有的注释
                            ln = ln.strip(' ')[:-1]  # 去掉换行符
                            for i in xrange(1, 7):  # 假设message的信息最多有7行
                                message = linecache.getline(file_name, ln_count + i)[:-1]
                                # print 'message', message, ln_count
                                if message.rfind('"') != -1 and message.rfind(')') != -1 and(message.rfind('"') < message.rfind(')')):  # 最后一行
                                    ln = ln + message.strip(' ')
                                    break
                                else:
                                    # print linecache.getline(file_name, ln_count+i)
                                    ln = ln + message.strip(' ')[:-1]
                                    continue
                                    # print ln
                                    # ln += linecache.getlines(file_name, ln_count + i)
                            # ln_count += i
                            cf.writelines(ln + '\n')
                            continue






# get_all_message_in_the_file('class_exception.txt')


with open("path.txt") as f:
    for e in f:
        get_all_message_in_the_file(e[:-1])


# def read_file_in_unicode()
