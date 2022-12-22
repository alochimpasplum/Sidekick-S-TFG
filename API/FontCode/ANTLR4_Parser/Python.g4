grammar Python;

TAB : '<TAB>';
VARIABLE_DECLARATIONS : '<VAR_DECLARATION>';
VARIABLE : '<VAR>';
PRINT : '<PRINT>';
SCAN : '<SCAN>';
FUNCTION : '<FUNC>';
MAIN_FUNCTION : '<BASE_FUNC>';
MATH_OPERATION : '<MATH>';
IF : '<IF>';
IF_TRUE_START : '<IF_TRUE>';
IF_TRUE_END : '</IF_TRUE>';
IF_FALSE_START : '<IF_FALSE>';
IF_FALSE_END : '</IF_FALSE>';
END_CODE : '<END>';

PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : '/' | 'div';

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

WS : [ ]+ -> skip;