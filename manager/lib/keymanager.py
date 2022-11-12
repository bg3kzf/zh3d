#!/usr/bin/env python3
# coding: UTF-8
import sys
l11ll_opy_ = sys.version_info [0] == 2
l1l1l_opy_ = 2048
l1lll_opy_ = 7
def l111_opy_ (keyedStringLiteral):
    global l1l1_opy_
    stringNr = ord (keyedStringLiteral [-1])
    rotatedStringLiteral = keyedStringLiteral [:-1]
    rotationDistance = stringNr % len (rotatedStringLiteral)
    recodedStringLiteral = rotatedStringLiteral [:rotationDistance] + rotatedStringLiteral [rotationDistance:]
    if l11ll_opy_:
        stringLiteral = unicode () .join ([unichr (ord (char) - l1l1l_opy_ - (charIndex + stringNr) % l1lll_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    else:
        stringLiteral = str () .join ([chr (ord (char) - l1l1l_opy_ - (charIndex + stringNr) % l1lll_opy_) for charIndex, char in enumerate (recodedStringLiteral)])
    return eval (stringLiteral)
import os, sys, re
l1_opy_ = 40 + 1 + 9 + 4
l1ll1_opy_ = 0xFFFF
l11l1_opy_ = re.compile(l111_opy_ (u"ࠫࡤࡥࡖ࠴ࡆࡏࡣࡤࡡࡡ࠮ࡨࡄ࠱ࡋ࠶࠭࠺࡟ࡾ࠵࠵࠲࠱࠱ࡿࠪࠀ"))
def l1l_opy_(key):
    if len(key) != l1_opy_:
        return False
    sum = 0
    for i in range(len(key) - 4):
        sum = sum + ord(key[i])
    l11_opy_ = sum % l1ll1_opy_
    l1111_opy_ = int(key[len(key)-4 : ], 16)
    return l11_opy_ == l1111_opy_
def verify(key):
    return l1l_opy_(key)
def activate(path, key, l11l_opy_=True):
    if l11l_opy_ and not l1l_opy_(key):
        return False
    l1ll_opy_ = l111_opy_ (u"ࠬࡥ࡟ࡗ࠵ࡇࡐࡤࡥࠧࠁ") + key[0:10]
    lines = None
    with open(path, l111_opy_ (u"࠭ࡲࠨࠂ"),  encoding=l111_opy_ (u"ࠧࡶࡶࡩ࠱࠽࠭ࠃ")) as l1llll_opy_:
        lines = l1llll_opy_.readlines()
    with open(path, l111_opy_ (u"ࠨࡹࠪࠄ"),  encoding=l111_opy_ (u"ࠩࡸࡸ࡫࠳࠸ࠨࠅ")) as l1l11_opy_:
        for line in lines:
            l1l11_opy_.write(l11l1_opy_.sub(l1ll_opy_, line))
    return True
def deactivate(path):
    return activate(path, l111_opy_ (u"ࠪ࠴࠵࠶࠰࠱࠲࠳࠴࠵࠶ࠧࠆ"), False)
if __name__ == l111_opy_ (u"ࠫࡤࡥ࡭ࡢ࡫ࡱࡣࡤ࠭ࠇ"):
    l111l_opy_ = sys.argv
    if len(l111l_opy_) < 3:
        sys.exit(1)
    else:
        ll_opy_ = l111l_opy_[1]
        if ll_opy_ == l111_opy_ (u"ࠬࡼࡥࡳ࡫ࡩࡽࠬࠈ") and len(l111l_opy_) == 3:
            if verify(l111l_opy_[2]):
                print(l111_opy_ (u"࠭ࡏࡌࠩࠉ"))
                sys.exit(0)
            else:
                print(l111_opy_ (u"ࠧࡃࡃࡇࠫࠊ"))
                sys.exit(1)
        elif ll_opy_ == l111_opy_ (u"ࠨࡣࡦࡸ࡮ࡼࡡࡵࡧࠪࠋ") and len(l111l_opy_) == 4:
            activate(l111l_opy_[2], l111l_opy_[3])
            sys.exit(0)
        elif ll_opy_ == l111_opy_ (u"ࠩࡧࡩࡦࡩࡴࡪࡸࡤࡸࡪ࠭ࠌ") and len(l111l_opy_) == 3:
            deactivate(l111l_opy_[2])
            sys.exit(0)
        else:
            sys.exit(1)