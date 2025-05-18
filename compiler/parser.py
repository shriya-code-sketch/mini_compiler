import ply.yacc as yacc
from .lexer import tokens

# Symbol table to store variable values
symbol_table = {}

def p_program(p):
    'program : statement_list'
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement_assign(p):
    'statement : ID ASSIGN expression'
    symbol_table[p[1]] = p[3]
    print(f"{p[1]} = {p[3]}")
    p[0] = ('assign', p[1], p[3])

def p_statement_expr(p):
    'statement : expression'
    p[0] = ('expr', p[1])

def p_statement_if(p):
    'statement : IF expression statement'
    if p[2]:
        parser.parse(p[3])

def p_statement_if_else(p):
    'statement : IF expression statement ELSE statement'
    if p[2]:
        parser.parse(p[3])
    else:
        parser.parse(p[5])

def p_statement_while(p):
    'statement : WHILE expression statement'
    while p[2]:
        parser.parse(p[3])

# Switch-Case implementation
def p_statement_switch(p):
    '''statement : SWITCH expression LBRACE case_list RBRACE'''
    switch_value = p[2]
    cases = p[4]
    if switch_value in cases:
        parser.parse(cases[switch_value])
    elif "default" in cases:
        parser.parse(cases["default"])

def p_case_list(p):
    '''case_list : case
                 | case_list case'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = {**p[1], **p[2]}

def p_case(p):
    '''case : CASE expression COLON statement
            | DEFAULT COLON statement'''
    if len(p) == 5:
        p[0] = {p[2]: p[4]}
    else:
        p[0] = {"default": p[3]}

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression LT expression
                  | expression GT expression
                  | expression EQ expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '==':
        p[0] = p[1] == p[3]

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


