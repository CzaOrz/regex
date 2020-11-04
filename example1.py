# coding: utf-8
import re
import loggus


def example1():
    text = "chen zi ang, ydc, yxc\r\n" \
           "匹配开头 匹配结尾\r\n" \
           "god say: you are a good man.\r\n" \
           "god say: you are a bad man.\r\n" \
           "now, what's god say?\r\n" \
           "hah~"

    loggus.WithFields({
        "ok": re.search("^chen", text, re.S).group(),
        "err": re.search("^匹配开头", text, re.S),
    }).info("^只能匹配目标字串的开头，其余部分则不进行匹配")

    loggus.WithFields({
        "ok": re.search("hah~$", text, re.S).group(),
        "err": re.search("chen$", text, re.S),
    }).info("$只能匹配目标字串的结尾，其余部分则不进行匹配")

    loggus.WithFields({
        "All": re.search("god say:(.*)", text, re.S).group(1),
        "OneLine": re.search("god say:(.*?)\r\n", text, re.S).group(1),
    }).info(".*表示延揽匹配，可以通过?来改为非贪婪")

    loggus.WithFields({
        "ok1": re.search("匹配([开头])", text, re.S).group(1),
        "ok2": re.search("匹配开([开头])", text, re.S).group(1),
        "ok3": re.search("chen ([a-z])", text, re.S).group(1),
        "ok4": re.search("匹([^开头])", text, re.S).group(1),
    }).info("[]表示可以匹配中括号内的任意一个, [^]则是不匹配")


if __name__ == '__main__':
    example1()
