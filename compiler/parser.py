import ply.yacc as yacc
from .lexer import tokens  # Note the dot for relative import

symbol_table = {}

def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_statement_assign(p):
    'statement : ID ASSIGN expression'
    symbol_table[p[1]] = p[3]
    print(f"{p[1]} = {p[3]}")
    p[0] = ('assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = ('expr', p[1])

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if type(p[1]) != type(p[3]):
        print("Semantic Error: Type mismatch")
        p[0] = 0
    else:
        if p[2] == '+': result = p[1] + p[3]
        elif p[2] == '-': result = p[1] - p[3]
        elif p[2] == '*': result = p[1] * p[3]
        elif p[2] == '/': result = p[1] / p[3]
        p[0] = result

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_id(p):
    'expression : ID'
    if p[1] not in symbol_table:
        print(f"Semantic Error: '{p[1]}' not declared")
        p[0] = 0
    else:
        p[0] = symbol_table[p[1]]

def p_error(p):
    if p:
        print(f"Syntax Error at '{p.value}'")
    else:
        print("Syntax Error at EOF")

parser = yacc.yacc()
