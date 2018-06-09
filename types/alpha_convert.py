#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
ÌĿҪÇ£º
Äµõ½һ¸öܻì´ó´×ĸµÄַ�����ÄµÄÎñѸÃַûΪ½öÃ¡д×ĸ»òóÖ¸£¬ΪÁ¾¡¿ÉÜٵĸı䣺
È¹û´®°üó¸ÊСÓµÈÚ¡д×ĸÊ£¬Ô°ÑַûΪСд¡£
È¹ûµÄýÚ¡д×ĸÊ£¬Ô°ÑַûΪȫ´ó£

±È磺
solve('coDe')=="code"
solve("CODe")=="CODE"
"""



# ¶Ô¡дµÄ¡-1£¬´óÄ¡1£¬Ȼºóã¡£
# ´óÔȫ²¿´ó¬·ñò¿Сд
def check_charter(c):
    return -1 if c.islower() else 1

def slove(s):
    nums = list(map(check_charter, s))
    return s.upper() if sum(nums) > 0 else s.lower()

def slove_ace(s):
    upper = sum([c.isupper() for c in s])
    lower = sum([c.islower() for c in s])
    return [s.lower(), s.upper()][upper>lower]


if __name__ == "__main__":
    print slove("coDe")
    print slove("CODe")
    print slove_ace("coDe")
    print slove_ace("CODe")
