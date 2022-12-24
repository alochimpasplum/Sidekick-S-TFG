grammar Python;

main_function: MAIN_FUNCTION ID
    sentence*;

sentence: var_decl | var_assign | var_print | str_print;

var_decl: TAB* VARIABLE_DECLARATIONS ID VARIABLE_TYPE;
var_assign: TAB* ID ASSIGN NUMBER;
var_print: TAB* PRINT ID;
str_print: TAB* PRINT VARIABLE_TYPE ID;

TAB : '<TAB>';
VARIABLE_DECLARATIONS : '<VAR_DECLARATION>';
VARIABLE_TYPE : '<INT>' | '<STRING>';
PRINT : '<PRINT>';
SCAN : '<SCAN>';
FUNCTION : '<FUNC>';
MAIN_FUNCTION : '<BASE_FUNC>';
IF : '<IF>';
IF_TRUE_START : '<IF_TRUE>';
IF_TRUE_END : '</IF_TRUE>';
IF_FALSE_START : '<IF_FALSE>';
IF_FALSE_END : '</IF_FALSE>';
END_CODE : '<END>';

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
NUMBER : [0-9]+;

WS : [ \t\n]+ -> skip;