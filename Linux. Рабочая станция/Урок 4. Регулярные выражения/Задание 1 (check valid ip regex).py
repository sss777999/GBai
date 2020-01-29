# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"((25[0-5]|2[0-5]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-5]\d|[01]?\d\d?)"

test_str = ("192.168.1.1\n"
            "225.1000.15.1\n"
            "255.254.10.1\n"
            "192.200.256.10\n"
            "26.224.1.255\n"
            "25.220.\n")

matches = re.finditer(regex, test_str, re.MULTILINE)
"""для вывода только full match в этом случае"""
for i in matches:
    print(i.group())

"""
for matchNum, match in enumerate(matches, start=1):

    print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                        end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                        end=match.end(groupNum),
                                                                        group=match.group(groupNum)))

Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.


Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
"""
