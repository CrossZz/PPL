// MY ID:1812295
grammar CSEL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : (declare)* EOF ;
// GLOBAL VARIABLE
// var_const: var_declare | const_declare;

declare: var_declare | const_declare | func_declare;

var_declare: LET list_var (COMMA list_var)* SEMI;

const_declare: CONSTANT list_const (COMMA list_const)* SEMI;

list_const: constant (COLON (NUMBER | STRING | BOOLEAN | JSON))? EQUAL ex ;

func_declare: FUNCTION IDND LP params_list?  RP compound_stmt;

// prams_list: (IDND (LSB (INT)? (COMMA INT?)* RSB)? (COMMA IDND (LSB (INT)? (COMMA INT?)* RSB)?)*)? ;
params_list: variable_func (COMMA variable_func)*;

variable_func: IDND (LSB (INT)? (COMMA INT?)* RSB)? ;
// list_variable: variable (COMMA variable)* ;

list_var: variable (COLON (NUMBER | STRING | BOOLEAN | JSON))? (EQUAL ex)? ;

constant: IDD (LSB INT (COMMA INT)* RSB)?;

variable: IDND (LSB INT (COMMA INT)* RSB)? ;

compound_stmt: LCB (declare_stmt)* RCB ;

declare_stmt: var_declare | const_declare | stmt;

// STATEMENTS
stmt
    : assign_stmt
    | if_stmt
    | for_in
    | for_of
    | while_stmt
    | break_stmt
    | continue_stmt
    | call_stmt
    | return_stmt
    ;

assign_stmt: (IDND | index_exp | key_exp ) EQUAL ex SEMI ;

if_stmt: IF LP ex RP compound_stmt (ELIF LP ex RP compound_stmt)* (ELSE compound_stmt)? ;

for_in: FOR IDND IN ex compound_stmt;

for_of: FOR IDND OF ex compound_stmt ;

while_stmt: WHILE LP ex RP compound_stmt ;

break_stmt: BREAK SEMI ;

continue_stmt: CONTINUE SEMI ;

call_stmt: call_exp SEMI ;

return_stmt: RETURN ex? SEMI ;

call_exp: CALL LP IDND COMMA LSB exps_list? RSB RP ;



exps_list: ex (COMMA ex)* ;

ex: exp (ADDDOT | EQUDOT) exp | exp ;

exp: exp1 (EQU | NQU | LT | GT | LTE | GTE ) exp1 | exp1 ;

exp1: exp1 (AND | OR) exp2 | exp2;

exp2: exp2 (ADD | SUB ) exp3 | exp3;

exp3: exp3 (MUL | DIV | MOD) exp4 | exp4 ;

exp4: FACT exp4 | exp5 ;

exp5: SUB exp5 | exp6 ;

exp6: exp7 (LSB ex (COMMA ex)* RSB)* | exp7 (LCB STRING_LIT RCB)*;

exp7: call_exp | operands ;

operands
    : literal
    | IDND
    | IDD
    | call_exp
    | LP ex RP
    ;

index_exp: operands (LSB ex (COMMA ex)* RSB) ;

key_exp:operands (LCB ex RCB)+;

array: LSB (literal (COMMA literal)*)? RSB ;

//json
json: LCB ((IDND COLON literal COMMA)* IDND COLON literal)? RCB;
//literal
literal: SUB? (INT|FLOAT) | BOOLEAN_LIT | STRING_LIT | array | json;

//IDENTIFIERS
//ID WITH DOLLAR
IDD: DOLLAR (LOWER_CHAR | UPPER_CHAR | DIGIT | DASH)* ;
//ID NOT DOLLAR
IDND: LOWER_CHAR  (LOWER_CHAR | UPPER_CHAR | DIGIT | DASH)* ;

// LITERALS
// Number
// NUMBER_LIT: SUB? (INT|FLOAT);

INT: DIGIT+;

FLOAT: DIGIT+ (DECIMAL_PART? EXPONENT_PART | DECIMAL_PART EXPONENT_PART?) ;

// Boolean
BOOLEAN_LIT: (TRUE|FALSE);
//String
STRING_LIT: '"' (STR_CHAR)* '"'
    {
		s = str(self.text)
		self.text = s[1:-1]
	}
	;

// Break Continue If Elif Else
// While For Of In Function
// Let True False Call Return
// Number Boolean String JSON Array
// Constant

//KEYWORDS

BREAK: 'Break' ;
CONTINUE: 'Continue' ;
ELSE: 'Else' ;
ELIF: 'Elif' ;
FOR: 'For' ;
FUNCTION: 'Function' ;
IF: 'If' ;
RETURN: 'Return' ;
NUMBER:'Number';
WHILE: 'While' ;
CALL:'Call';
OF:'Of';
IN:'In';
LET:'Let';
fragment TRUE:'True';
fragment FALSE:'False';
BOOLEAN:'Boolean';
STRING:'String';
JSON:'JSON';
ARRAY:'Array';
CONSTANT:'Constant';

// OPERATORS

ADD: '+' ;
SUB: '-' ;
MUL: '*' ;
DIV: '/' ;
MOD: '%' ;
FACT: '!' ;
AND: '&&' ;
OR: '||' ;
EQU: '==' ;
NQU: '!=' ;
LT : '<' ;
GT : '>' ;
LTE: '<=' ;
GTE: '>=' ;
EQUAL: '=' ;
EQUDOT:'==.';
ADDDOT:'+.';

// SEPARATORS

LP: '(' ; 
RP: ')' ; 
LSB: '[' ; 
RSB: ']' ; 
COLON: ':' ; 
DOT: '.' ;
COMMA: ',' ; 
SEMI: ';' ; 
LCB: '{' ;
RCB: '}' ; 

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

COMMENT: '##' .*? '##' -> skip ; // skip comments

fragment DIGIT: [0-9] ;
fragment UPPER_CHAR: [A-Z] ;
fragment LOWER_CHAR: [a-z] ;
fragment DASH: '_' ;
fragment DOLLAR:'$';
fragment E: [eE] ;
fragment SIGN: [+-] ;
fragment DECIMAL_PART: DOT DIGIT* ;
fragment EXPONENT_PART: E SIGN? DIGIT+;
fragment STR_CHAR: ~[\n\r'\\"] | ESC_SEQ | '\'"' ;
fragment ESC_SEQ: '\\' [btnfr'\\] ;
fragment ESC_ILLEGAL: '\\' ~[btnfr'\\] | '\''~["];


UNCLOSE_STRING: '"'STR_CHAR* ( [\n\r] | EOF)
    {
		s = str(self.text)
		if s[-1] in ['\n', '\r']:
			raise UncloseString(s[1:-1])
		else:
			raise UncloseString(s[1:])
	}
	;

ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
    {
		s = str(self.text)
		raise IllegalEscape(s[1:])
	}
	;

UNTERMINATED_COMMENT: '##' .*? 
    {
        raise UnterminatedComment()
    }
    ;

ERROR_CHAR: .
    {
		raise ErrorToken(self.text)
	}
	;

