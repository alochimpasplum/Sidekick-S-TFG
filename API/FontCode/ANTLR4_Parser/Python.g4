grammar Python;

prog: (function | var | math_op | conditional)+ EOF
    ;

function: main_function         # Function_A
        | built_function        # Function_B
        | custom_function       # Function_C
        ;

expr: ID        # Variable
    | NUMBER    # Number
    ;

main_function: MAIN_FUNCTION;
custom_function: FUNCTION expr;
built_function: print           # Built_print
              | scan            # Built_scan
              ;

var : var_decl      # Var_A
    | var_assign    # Var_B
    ;

var_decl: VARIABLE_DECLARATIONS expr VARIABLE_TYPE;
var_assign: expr ASSIGN expr;

math_op: expr ASSIGN expr (PLUS | MINUS | MULT | DIV) expr      # Math_Operation
       ;

conditional: CONDITIONAL_START condition conditional_branches CONDITIONAL_END;

conditional_branches: conditional_branch+;

condition: expr                                             # Switch_Case
         | expr (GT | LET | GEQ | LEQ | EQ | NEQ) expr      # If
         ;

conditional_branch: CONDITION_BRANCH_START expr conditional_lines CONDITION_BRANCH_END;

conditional_lines: (function | var | math_op)* ;

print: PRINT expr;
scan: SCAN expr;

TAB : '<TAB>' -> skip;
VARIABLE_DECLARATIONS : '<VAR_DECLARATION>';
VARIABLE_TYPE : '<INT>' | '<STRING>';
PRINT : '<PRINT>';
SCAN : '<SCAN>';
FUNCTION : '<FUNC>';
MAIN_FUNCTION : '<BASE_FUNC>';
CONDITIONAL_START : '<CONDITIONAL>';
CONDITIONAL_END : '</CONDITIONAL>';
CONDITION_BRANCH_START : '<CONDITION>';
CONDITION_BRANCH_END : '</CONDITION>';
END_CODE : '<END>' -> skip;

PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/';

AND : '&&';
OR : '||';
NOT : '!';

GT : '>';
LET : '<';
GEQ : '>=';
LEQ : '<=';
EQ : '==';
NEQ : '!=';

ASSIGN : '=';

ID : [a-zA-Z_][a-zA-Z0-9_]*;
// todo: agregar strings
NUMBER : [0-9]+;

WS : [ \t\n]+ -> skip;