import pytest
from cyk_parser import (grammar)

# Pretty empty test file, but it thoroughly tests the 
# parse method from grammar class in cyk_parser.py

# usage:
# pytest -v

def test_parse():
    g_one = grammar('test_grammar_one.txt')
    # Corresponding grammar
    # S -> AB
    # A -> CD|CF
    # B -> c|EB
    # C -> a
    # D -> b
    # E -> c
    # F -> AD
    g_two = grammar('test_grammar_two.txt')
    # Corresponding grammar
    # S -> AB|BC
    # A -> BA|a
    # B -> CC|b
    # C -> AB|a
    g_three = grammar('test_grammar_three.txt')
    # Corresponding grammar
    # S -> XS|TY|AT|BT|ZR|a|b
    # F -> TY|AT|BT|a|b
    # T -> AT|BT|a|b
    # X -> TP
    # Y -> UF
    # Z -> LS
    # A -> a
    # B -> b
    # P -> x
    # U -> t
    # L -> l
    # R -> r
    # checking parser with test grammar one
    assert g_one.parse('abc') == True
    assert g_one.parse('bac') == False
    assert g_one.parse('aabcc') == False
    assert g_one.parse('abcc') == True
    assert g_one.parse('cabaab') == False
    assert g_one.parse('aaabbbcc') == True
    # checking parser with test grammar two
    assert g_two.parse('ab') == True
    assert g_two.parse('aaaaaaaaaab') == False
    assert g_two.parse('bbbbbbbbbbbbba') == False
    assert g_two.parse('babbabababa') == True
    assert g_two.parse('aaba') == True
    assert g_two.parse('baaba') == True
    # checking parser with test grammar three
    assert g_three.parse('bxataa') == True
    assert g_three.parse('bxataat') == False
    assert g_three.parse('lbxataar') == True
    assert g_three.parse('lbxataal') == False
    assert g_three.parse('axaabtbba') == True
    assert g_three.parse('laaaaaaaaaaxbbbbbbbbbbbbbbababbabar') == True