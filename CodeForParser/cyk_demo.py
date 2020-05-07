# usage: 
# python3 cyk_demo.py
from cyk_parser import grammar

# g_one = grammar('test_grammar_one.txt')
# Corresponding grammar
    # S -> AB
    # A -> CD|CF
    # B -> c|EB
    # C -> a
    # D -> b
    # E -> c
    # F -> AD
# g_one.parse('aaabbbcc')

# g_two = grammar('test_grammar_two.txt')
# Corresponding grammar
    # S -> AB|BC
    # A -> BA|a
    # B -> CC|b
    # C -> AB|a
# g_two.parse('baaba')

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
g_three.parse('laaaaaaaaaaxbbbbbbbbbbbbbbababbabar')
# g_four = grammar('test_grammar_from_class.txt')
# Corresponding grammar
# g_three.parse('')
print('Exiting progam')

