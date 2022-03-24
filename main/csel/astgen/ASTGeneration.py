from CSELVisitor import CSELVisitor
from CSELParser import CSELParser
from AST import *


class ASTGeneration(CSELVisitor):
    # program  : (declare)* EOF ;
    def visitProgram(self, ctx: CSELParser.ProgramContext):
        # return Program([VarDecl(Id(ctx.ID().getText()), [], NoneType(), None)])
        declList = []
        for x in ctx.declare():
            decl = self.visitDeclare(x)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return Program(declList)
    # declare: var_declare | const_declare | func_declare;/
    def visitDeclare(self,ctx:CSELParser.DeclareContext):
        return self.visitChildren(ctx)
    
    
    # var_declare: LET list_var (COMMA list_var)* SEMI;
    def visitVar_declare(self, ctx: CSELParser.Var_declareContext):
        arr = []
        for i in ctx.list_var():
            initVar = self.visitList_var(i)
            arr.append(VarDecl(initVar[0][0],initVar[0][1],initVar[1],initVar[2]))
        return arr
    # list_var: variable (COLON (NUMBER | STRING | BOOLEAN | JSON))? (EQUAL ex)? ;
    def visitList_var(self, ctx: CSELParser.List_varContext):
        if ctx.NUMBER(): typ=NumberType()
        elif ctx.STRING(): typ=StringType()
        elif ctx.BOOLEAN(): typ=BooleanType()
        elif ctx.JSON(): typ=JSONType()
        else: typ=NoneType()
        if ctx.ex(): return [self.visitVariable(ctx.variable()), typ, self.visitEx(ctx.ex())]
        return [self.visitVariable(ctx.variable()), typ, None]
    # variable: IDND (LSB INT (COMMA INT)* RSB)? ;
    def visitVariable(self, ctx: CSELParser.VariableContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.IDND().getText()),None]
        arr = [NumberLiteral(float(i.getText())) for i in ctx.INT()]
        return [Id(ctx.IDND().getText()), arr]
    
    
    # const_declare: CONSTANT list_const (COMMA list_const)* SEMI;
    def visitConst_declare(self, ctx: CSELParser.Const_declareContext):
        arr = []
        for i in ctx.list_const():
            initConst = self.visitList_const(i)
            arr.append(ConstDecl(initConst[0][0],initConst[0][1],initConst[1],initConst[2]))
        return arr
    # list_const: constant (COLON (NUMBER | STRING | BOOLEAN | JSON))? EQUAL ex ;
    def visitList_const(self, ctx: CSELParser.List_constContext):
        if ctx.NUMBER(): typ=NumberType()
        elif ctx.STRING(): typ=StringType()
        elif ctx.BOOLEAN(): typ=BooleanType()
        elif ctx.JSON(): typ=JSONType()
        else: typ=NoneType()
        return [self.visitConstant(ctx.constant()), typ, self.visitEx(ctx.ex())]
    # constant: IDD (LSB INT (COMMA INT)* RSB)?';
    def visitConstant(self, ctx: CSELParser.ConstantContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.IDD().getText()),None]
        arr = [NumberLiteral(float(i.getText())) for i in ctx.INT()]
        return [Id(ctx.IDD().getText()), arr]
    
    
    #func_declare: FUNCTION IDND LP params_list?  RP compound_stmt;
    def visitFunc_declare(self, ctx: CSELParser.Func_declareContext):
        compound = self.visitCompound_stmt(ctx.compound_stmt())
        paraList = self.visitParams_list(ctx.params_list()) if ctx.params_list() else []
        return [FuncDecl(Id(ctx.IDND().getText()), paraList, compound)]
    # params_list: variable_func (COMMA variable_func)*;
    def visitParams_list(self,ctx:CSELParser.Params_listContext):
        arr=[]
        for i in ctx.variable_func():
            temp=self.visitVariable_func(i)
            arr.append(VarDecl(temp[0],temp[1],NoneType(),None))
        return arr
    # variable_func: IDND (LSB (INT)? (COMMA INT?)* RSB)? ;
    def visitVariable_func(self,ctx:CSELParser.Variable_funcContext):
        if ctx.getChildCount() == 1:
            return [Id(ctx.IDND().getText()),None]
        if ctx.LSB() and (not ctx.INT()): 
            return [Id(ctx.IDND().getText()),[]]
        arr = [NumberLiteral(float(i.getText())) for i in ctx.INT()]
        return [Id(ctx.IDND().getText()), arr]

   
    # array: LSB (literal (COMMA literal)*)?' RSB ;
    def visitArray(self, ctx: CSELParser.ArrayContext):
        if ctx.getChildCount() == 2: return ArrayLiteral([])
        return ArrayLiteral([self.visitLiteral(x) for x in ctx.literal()])

    # json: LCB ((IDND COLON literal COMMA)* IDND COLON literal)? RCB;
    def visitJson(self, ctx: CSELParser.JsonContext):
        if ctx.getChildCount() == 2: return JSONLiteral([])
        arr=[]
        i=0
        for x in ctx.literal():
            arr.append((Id(ctx.IDND(i).getText()),self.visitLiteral(x)))
            i=i+1
        return JSONLiteral(arr)
    
    # literal: SUB? (INT|FLOAT) | BOOLEAN_LIT | STRING_LIT | array | json;
    def visitLiteral(self, ctx: CSELParser.LiteralContext):
        if ctx.INT(): return NumberLiteral(float(ctx.INT().getText())) 
        elif ctx.FLOAT(): return NumberLiteral(float(ctx.FLOAT().getText())) 
        elif ctx.BOOLEAN_LIT(): return BooleanLiteral(True) if ctx.BOOLEAN_LIT().getText() == "True" else BooleanLiteral(False)
        elif ctx.STRING_LIT(): return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.array(): return self.visitArray(ctx.array())
        else: return self.visitJson(ctx.json())
    
    # compound_stmt: LCB (declare_stmt)* RCB ;
    def visitCompound_stmt(self, ctx: CSELParser.Compound_stmtContext):
        declList = []
        for i in ctx.declare_stmt():
            decl = self.visitDeclare_stmt(i)
            if isinstance(decl, list):
                declList.extend(decl if decl else [])
            else:
                declList.append(decl)
        return declList

    # declare_stmt: var_declare | const_declare | stmt;
    def visitDeclare_stmt(self,ctx:CSELParser.Declare_stmtContext):
        return self.visitChildren(ctx)

    # stmt: assign_stmt|if_stmt|for_in|for_of|while_stmt|do_while_stmt|break_stmt|continue_stmt|call_stmt|return_stmt;
    def visitStmt(self, ctx: CSELParser.StmtContext):
        return self.visitChildren(ctx)

    # assign_stmt: (IDND | index_exp | key_exp ) EQUAL ex SEMI ;
    def visitAssign_stmt(self, ctx: CSELParser.Assign_stmtContext):
        if ctx.IDND():
            return Assign(Id(ctx.IDND().getText()), self.visitEx(ctx.ex()))
        elif ctx.index_exp():
            return Assign(self.visitIndex_exp(ctx.index_exp()), self.visitEx(ctx.ex()))
        return Assign(self.visitKey_exp(ctx.key_exp()), self.visitEx(ctx.ex()))

    # if_stmt: IF LP ex RP compound_stmt (ELIF LP ex RP compound_stmt)* (ELSE compound_stmt)? ';
    def visitIf_stmt(self, ctx: CSELParser.If_stmtContext):
        expr = ""
        arrStmt = []
        ifstmt = []
        for i in range(ctx.getChildCount()):
            if ctx.getChild(i) in ctx.ex():
                expr = self.visitEx(ctx.getChild(i))
            elif ctx.getChild(i) in ctx.compound_stmt():
                arrStmt.extend(self.visitCompound_stmt(ctx.getChild(i)))
            elif ctx.getChild(i) in ctx.ELIF() or ctx.getChild(i) == ctx.ELSE():
                ifstmt.append((expr, arrStmt))
                expr = ""
                arrStmt = []
        if ctx.ELSE():
            return If(ifstmt, arrStmt)
        ifstmt.append((expr, arrStmt))
        return If(ifstmt, [])
    
    # for_in: FOR IDND IN ex compound_stmt;
    def visitFor_in(self, ctx: CSELParser.For_inContext):
        idx1 = Id(ctx.getChild(1).getText())
        # if ctx.getChild(3) in ctx.IDND():
        #     expr = Id(ctx.getChild(3).getText())
        # else:
        expr = self.visitEx(ctx.ex())
        arrStmt = self.visitCompound_stmt(ctx.compound_stmt())
        return ForIn(idx1, expr, arrStmt)
    
    # for_of: FOR IDND OF ex compound_stmt ;
    def visitFor_of(self, ctx: CSELParser.For_inContext):
        idx1 = Id(ctx.getChild(1).getText())
        # if ctx.getChild(3) in ctx.IDND():
        #     expr = Id(ctx.getChild(3).getText())
        # else:
        expr = self.visitEx(ctx.ex())
        arrStmt = self.visitCompound_stmt(ctx.compound_stmt())
        return ForOf(idx1, expr, arrStmt)

    # while_stmt: WHILE LP ex RP compound_stmt ;
    def visitWhile_stmt(self, ctx: CSELParser.While_stmtContext):
        arrStmt = self.visitCompound_stmt(ctx.compound_stmt()) 
        expr = self.visitEx(ctx.ex())
        return While(expr, arrStmt)

    # break_stmt: BREAK SEMI ;
    def visitBreak_stmt(self, ctx: CSELParser.Break_stmtContext):
        return Break()

    # continue_stmt: CONTINUE SEMI ;
    def visitContinue_stmt(self, ctx: CSELParser.Continue_stmtContext):
        return Continue()

    # call_stmt: call_exp SEMI ;
    def visitCall_stmt(self, ctx: CSELParser.Call_stmtContext):
        callexp = self.visitCall_exp(ctx.call_exp())
        method = callexp.method
        param = callexp.param
        return CallStmt(method, param)

    # return_stmt: RETURN ex? SEMI ;
    def visitReturn_stmt(self, ctx: CSELParser.Return_stmtContext):
        return Return(self.visitEx(ctx.ex())) if ctx.ex() else Return(None)

    # call_exp: CALL LP IDND COMMA LSB exps_list?' RSB RP ;
    def visitCall_exp(self, ctx: CSELParser.Call_expContext):
        method = Id(ctx.IDND().getText())
        param = []
        if ctx.exps_list():
            param = self.visitExps_list(ctx.exps_list())
        return CallExpr(method, param)

    # exps_list: ex (COMMA ex)* ;
    def visitExps_list(self, ctx: CSELParser.Exps_listContext):
        return [self.visitEx(i) for i in ctx.ex()]

    # ex: exp (ADDDOT | EQUDOT) exp | exp ;
    def visitEx(self, ctx: CSELParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visitExp(ctx.exp(0))
        op = ctx.getChild(1).getText()
        left = self.visitExp(ctx.exp(0))
        right = self.visitExp(ctx.exp(1))
        return BinaryOp(op, left, right)

    # exp: exp1 (EQU | NQU | LT | GT | LTE | GTE ) exp1 | exp1 ;
    def visitExp(self, ctx: CSELParser.ExpContext):
        if ctx.getChildCount() == 1:
            return self.visitExp1(ctx.exp1(0))
        op = ctx.getChild(1).getText()
        left = self.visitExp1(ctx.exp1(0))
        right = self.visitExp1(ctx.exp1(1))
        return BinaryOp(op, left, right)

    # exp1: exp1 (AND | OR) exp2 | exp2;
    def visitExp1(self, ctx: CSELParser.Exp1Context):
        if ctx.getChildCount() == 1:
            return self.visitExp2(ctx.exp2())
        op = ctx.getChild(1).getText()
        left = self.visitExp1(ctx.exp1())
        right = self.visitExp2(ctx.exp2())
        return BinaryOp(op, left, right)
    
    # exp2: exp2 (ADD | SUB ) exp3 | exp3;
    def visitExp2(self, ctx: CSELParser.Exp2Context):
        if ctx.getChildCount() == 1:
            return self.visitExp3(ctx.exp3())
        op = ctx.getChild(1).getText()
        left = self.visitExp2(ctx.exp2())
        right = self.visitExp3(ctx.exp3())
        return BinaryOp(op, left, right)

    # exp3: exp3 (MUL | DIV | MOD) exp4 | exp4 ;
    def visitExp3(self, ctx: CSELParser.Exp3Context):
        if ctx.getChildCount() == 1:
            return self.visitExp4(ctx.exp4())
        op = ctx.getChild(1).getText()
        left = self.visitExp3(ctx.exp3())
        right = self.visitExp4(ctx.exp4())
        return BinaryOp(op, left, right)

    # exp4: FACT exp4 | exp5 ;
    def visitExp4(self, ctx: CSELParser.Exp4Context):
        if ctx.getChildCount() == 1:
            return self.visitExp5(ctx.exp5())
        op = '!'
        right = self.visitExp4(ctx.exp4())
        return UnaryOp(op, right)
    
    # exp5: SUB exp5 | exp6 ;
    def visitExp5(self, ctx: CSELParser.Exp5Context):
        if ctx.getChildCount() == 1:
            return self.visitExp6(ctx.exp6())
        op = ctx.getChild(0).getText()
        right = self.visitExp5(ctx.exp5())
        return UnaryOp(op, right)

    # exp6: exp7 (LSB ex (COMMA ex)* RSB)* | exp7 (LCB STRING_LIT RCB)*;
    def visitExp6(self, ctx: CSELParser.Exp6Context):
        if ctx.getChildCount() == 1:
            return self.visitExp7(ctx.exp7())
        if ctx.LSB():
            return ArrayAccess(self.visitExp7(ctx.exp7()), [self.visitEx(x) for x in ctx.ex()])
        if ctx.LCB():
            return JSONAccess(self.visitExp7(ctx.exp7()), [StringLiteral(x.getText()) for x in ctx.STRING_LIT()])

    # exp7: call_exp | operands ;
    def visitExp7(self, ctx: CSELParser.Exp7Context):
        return self.visitChildren(ctx)

    # operands:literal | IDND | IDD | call_exp | LP ex RP
    def visitOperands(self, ctx: CSELParser.OperandsContext):
        if ctx.IDD(): return Id(ctx.IDD().getText())
        if ctx.IDND(): return Id(ctx.IDND().getText())
        if ctx.literal(): return self.visitLiteral(ctx.literal())
        if ctx.call_exp(): return self.visitCall_exp(ctx.call_exp())
        return self.visitEx(ctx.ex())

    # index_exp: operands (LSB ex (COMMA ex)* RSB) ;
    def visitIndex_exp(self, ctx: CSELParser.Index_expContext):
        return ArrayAccess(self.visitOperands(ctx.operands()), [self.visitEx(x) for x in ctx.ex()])

    # key_exp:operands (LCB ex RCB)+;
    def visitKey_exp(self, ctx: CSELParser.Key_expContext):
        return JSONAccess(self.visitOperands(ctx.operands()), [self.visitEx(x) for x in ctx.ex()])

