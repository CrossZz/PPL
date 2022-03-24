from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple
from AST import * 
from Visitor import *
from StaticError import *
from functools import *

class Type(ABC):
    __metaclass__ = ABCMeta
    pass
class Prim(Type):
    __metaclass__ = ABCMeta
    pass
class IntType(Prim):
    pass
# class FloatType(Prim):
#     pass
class NumberType(Prim):
    pass
class StringType(Prim):
    pass
class BoolType(Prim):
    pass
class VoidType(Type):
    pass
class Unknown(Type):
    pass
class JSONType(Type):
    pass

@dataclass
class ArrayType(Type):
    dimen:List[int]
    element_type: Type

@dataclass
class MType:
    intype:List[Type]
    restype:Type

@dataclass
class Symbol:
    name: str
    mtype:Type

class StaticChecker(BaseVisitor):
    # list_func_decl = []
    list_called = []
    list_func_name_and_param = []
    list_built_in_name = []
    list_called_exp = []
    list_arrcell_of_func = []
    

    def __init__(self,ast):
        self.ast = ast
        self.global_envi = [
Symbol("str2num",MType([StringType()],NumberType())),
Symbol("num2str",MType([NumberType()],StringType())),
Symbol("str2bool",MType([StringType()],BoolType())),
Symbol("bool2str",MType([BoolType()],StringType())),
Symbol("read",MType([],StringType())),
Symbol("print",MType([StringType()],VoidType())),
Symbol("printLn",MType([StringType()],VoidType()))
]                           

    def check(self):
        return self.visit(self.ast,self.global_envi)

    def visitProgram(self, ast, c):
    
        self.list_build_in_func_name = reduce(lambda acc, ele: acc + [ele.name], self.global_envi, [])
        func_names = reduce(lambda acc, ele: acc + [{"Name":ele.name.name, "numParam":len(ele.param)}] if isinstance(ele, FuncDecl) else [] , ast.decl, [])
        self.list_func_name_and_param = func_names
        c = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, acc)]], ast.decl, [[]])
        flags = list(filter(lambda x: x["ASTType"] == "FuncDecl", c[0]))
        if flags: 
            if not list(filter(lambda x: x["Name"] == "main", flags)):
                raise NoEntryPoint()
    
    def visitVarDecl(self, ast, c):
        vari = ast.variable.name
        dimen = ast.varDimen 
    
        if vari in self.list_build_in_func_name: raise Redeclared(Variable(),vari)
        if ast.varInit:
            init_val = self.visit(ast.varInit, c)
        else: init_val = None 

        flags = list(filter(lambda x: x["Name"] ==vari, c[0]))
        if flags: raise Redeclared(Variable(),vari)

        if dimen and init_val: return {"ASTType": "VarDecl", "Name":vari, "dimen" : dimen, "init_val" :  init_val, "Type": ArrayType(dimen,  init_val["Type"])}
        if dimen: return {"ASTType": "VarDecl", "Name":vari, "dimen" : dimen, "init_val" :  init_val, "Type": ArrayType(dimen, None)}
        if init_val:
            return {"ASTType": "VarDecl", "Name":vari, "dimen" : dimen, "init_val" : init_val, "Type": init_val["Type"]}
        return {"ASTType": "VarDecl", "Name":vari, "dimen" : dimen, "init_val" :  init_val, "Type": None}

    def visitConstDecl(self, ast, c):
        vari = ast.constant.name
        dimen = ast.constDimen 
    
        if vari in self.list_build_in_func_name: raise Redeclared(Constant(),vari)
        init_val = self.visit(ast.constInit, c) 

        flags = list(filter(lambda x: x["Name"] ==vari, c[0]))
        if flags: raise Redeclared(Constant(),vari)

        if dimen and init_val: return {"ASTType": "ConstDecl", "Name":vari, "dimen" : dimen, "init_val" :  init_val, "Type": ArrayType(dimen,  init_val["Type"])}
        # if dimen: return {"ASTType": "VarDecl", "Name":vari, "dimen" : dimen, "init_val" :  init_val, "Type": ArrayType(dimen, None)}
        # if init_val:
        return {"ASTType": "ConstDecl", "Name":vari, "dimen" : dimen, "init_val" : init_val, "Type": init_val["Type"]}
        # return {"ASTType": "ConstDecl", "Name":vari, "dimen" : dimen, "init_val" :  init_val, "Type": None}
    
    def visitFuncDecl(self, ast, c):
        func_name = ast.name.name
        if func_name in self.list_build_in_func_name: 
            raise Redeclared(Function(), func_name)
        same_name = list(filter(lambda x: x["Name"] == func_name, c[0]))
        if same_name: 
            raise Redeclared(Function(), ast.name.name)
        env_in_funcc = [[]]
        for e in ast.param:
            same_name_vari = list(filter(lambda x: x["Name"] == e.variable.name, env_in_funcc[0]))
            if same_name_vari: 
                raise Redeclared(Parameter(), e.variable.name)
            env_in_funcc[0] += [self.visit(e, env_in_funcc)]
        paramList = env_in_funcc[0]
        env_in_funcc = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, acc)]], ast.body[0], env_in_funcc)
        env_in_funcc += c
        return_type = VoidType  
        list_called = list(filter(lambda x:x["Name"] == func_name, self.list_called)) 
        if list_called: return_type = VoidType       
        
        for stmt in ast.body[1]:
            if isinstance(stmt, Return):
                return_type = None
                flag = list(filter(lambda x:x["Name"] == func_name, self.list_arrcell_of_func))
                if flag: return_type = flag[0]["Type"]
                
                cur_return = self.visit(stmt, env_in_funcc)
                
                if not return_type: 
                    return_type = cur_return["Type"]
                    if not return_type: raise TypeCannotBeInferred(stmt)
                elif return_type == VoidType: raise TypeMismatchInStatement(stmt)
            elif isinstance(stmt, CallStmt):
                self.visit(stmt, env_in_funcc)
                list_called =  list(filter(lambda x: x["Name"] == func_name, self.list_called))
                if list_called: 
                    for e1, e2 in zip(list_called,paramList): 
                        if e1["Type"] != e2["Type"]: raise TypeMismatchInStatement(stmt)
            elif isinstance(stmt, Assign):
                if isinstance(stmt.lhs, CallExpr):
                    list_called = list(filter(lambda x: x["Name"] == stmt.lhs.method.name and x["Type"] == VoidType, c[-1]))
                    if list_called: raise TypeMismatchInStatement(stmt)
                    self.visit(stmt, env_in_func)
                if isinstance(stmt.rhs, CallExpr):
                    list_called = list(filter(lambda x: x["Name"] == stmt.rhs.method.name and x["Type"] == VoidType, c[-1]))
                    if list_called: raise TypeMismatchInStatement(stmt)
                    self.visit(stmt, env_in_funcc)
                self.visit(stmt, env_in_funcc)
            else: self.visit(stmt, env_in_funcc) 
        return {"ASTType": "FuncDecl", "Name": func_name, "paramList": paramList, "Type": return_type}
    
                
    

    def visitAssign(self, ast, c):
        
        lhs = self.visit(ast.lhs, c)
        if isinstance(ast.lhs, Id) and lhs == None: raise Undeclared(Identifier(), ast.lhs.name)
        
        rhs = self.visit(ast.rhs, c)
        if isinstance(ast.rhs, Id) and rhs == None: raise Undeclared(Identifier(), ast.rhs.name)
    

        if isinstance(lhs, TypeCannotBeInferred): raise TypeCannotBeInferred(ast)
        if isinstance(rhs, TypeCannotBeInferred): raise TypeCannotBeInferred(ast)

        if not isinstance(ast.lhs, ArrayAccess) and not isinstance(ast.rhs, ArrayAccess):
            if lhs["Type"] == VoidType: raise TypeMismatchInStatement(ast)
            if lhs["Type"] == None and rhs["Type"] == None: 
                raise TypeCannotBeInferred(ast)
            if lhs["Type"] == None: lhs["Type"] = rhs["Type"]
            if rhs["Type"] == None: rhs["Type"] = lhs["Type"]
            if lhs["Type"] != rhs["Type"]: 
                raise TypeMismatchInStatement(ast)

        if isinstance(ast.lhs, ArrayAccess) and isinstance(ast.rhs, ArrayAccess):
            id = ast.rhs.arr
            if isinstance(id, CallExpr):
                if not rhs["Name"]["dimen"]: 
                    raise TypeCannotBeInferred(ast)
                id = id.method

            if not rhs["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: rhs["Ele_Type"] = flag[0]["Type"].element_type

            id = ast.lhs.arr
            if isinstance(id, CallExpr): 
                if not lhs["Name"]["dimen"]: 
                    raise TypeCannotBeInferred(ast)
                id = id.method

            if not lhs["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: lhs["Ele_Type"] = flag[0]["Type"].element_type

    
            if not lhs["Ele_Type"] and not rhs["Ele_Type"]: 
                raise TypeCannotBeInferred(ast)
            if not lhs["Ele_Type"]: lhs["Ele_Type"] = rhs["Ele_Type"]
            if not rhs["Ele_Type"]: rhs["Ele_Type"] = lhs["Ele_Type"]
            if rhs["Ele_Type"] != lhs["Ele_Type"]: 
                raise TypeMismatchInStatement(ast)
            
            id = ast.lhs.arr
            if isinstance(id, CallExpr): id = id.method
            flag = self.visit(id, c)
            if flag: flag["Type"].element_type = lhs["Ele_Type"]
            else:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: flag[0]["Type"].element_type = lhs["Ele_Type"]

            id = ast.rhs.arr
            if isinstance(id, CallExpr): id = id.method
            flag = self.visit(id, c)
            if flag: flag["Type"].element_type = rhs["Ele_Type"]
            else:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: flag["Type"][0].element_type = rhs["Ele_Type"]
    

        elif isinstance(ast.rhs, ArrayAccess):
            id = ast.rhs.arr
            if isinstance(id, CallExpr): 
                if not rhs["Name"]["dimen"]: raise TypeCannotBeInferred(ast)
                id = id.method

            if not rhs["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: rhs["Ele_Type"] = flag[0]["Type"].element_type

            if not rhs["Ele_Type"] and not lhs["Type"]: 
                raise TypeCannotBeInferred(ast)
            if not rhs["Ele_Type"]: rhs["Ele_Type"] = lhs["Type"]
            if not lhs["Type"]: lhs["Type"] = rhs["Ele_Type"]
            if rhs["Ele_Type"] != lhs["Type"]: 
                raise TypeMismatchInStatement(ast) 

            flag = self.visit(id, c)
            if flag: flag["Type"].element_type = rhs["Ele_Type"]
            else:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: flag[0]["Type"].element_type = rhs["Ele_Type"]

        elif isinstance(ast.lhs, ArrayAccess):
            id = ast.lhs.arr
            if isinstance(id, CallExpr): 
                if not lhs["Name"]["dimen"]: 
                    raise TypeCannotBeInferred(ast)
                id = id.method
            if not lhs["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: lhs["Ele_Type"] = flag[0]["Type"].element_type
            
            if not lhs["Ele_Type"] and not rhs["Type"]: 
                raise TypeCannotBeInferred(ast)
            if not lhs["Ele_Type"]: lhs["Ele_Type"] = rhs["Type"]
            if not rhs["Type"]: rhs["Type"] = lhs["Ele_Type"]
            if lhs["Ele_Type"] != rhs["Type"]: 
                raise TypeMismatchInStatement(ast) 
            flag = self.visit(id, c)
            if flag: flag["Type"].element_type = lhs["Ele_Type"]
            else:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))[0]
                if flag: flag["Type"].element_type = lhs["Ele_Type"]

    def visitArrayAccess(self, ast, c):
        arr = self.visit(ast.arr, c)
        flag = None
        if isinstance(ast.arr, Id): flag = self.visit(ast.arr, c)
        else: flag = self.visit(ast.arr.method, c)
        if flag and not isinstance(flag["Type"], ArrayType): 
            raise TypeMismatchInExpression(ast)  
        if isinstance(arr, TypeCannotBeInferred): 
            return TypeCannotBeInferred(ast)
        if not arr and isinstance(ast.arr, Id): 
            raise Undeclared(Identifier(), ast.arr.name)
        idx = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, c)]], ast.idx, [[]])
        if list(filter(lambda x: isinstance(x, TypeCannotBeInferred), idx[0])): 
            return TypeCannotBeInferred(ast)
        flags = list(filter(lambda x: x["Type"] == IntType, idx[0]))
        if arr["Type"]:
            if not isinstance(arr["Type"],ArrayType): 
                raise TypeMismatchInExpression(ast)
        else: arr["Type"] = ArrayType([],None)
        if arr["dimen"] and len(arr["dimen"]) != len(idx[0]): 
            raise TypeMismatchInExpression(ast)
        if len(flags) != len(idx[0]): 
            raise TypeMismatchInExpression(ast)
        ele_type = None
        array_type = None
        for lst in c:
            flag = list(filter(lambda x: x["Name"] == arr["Name"], lst))
            if flag:
                if flag[0]["Type"]: ele_type = flag[0]["Type"].element_type
                array_type = flag[0]["Type"]
        if isinstance(ast.arr, CallExpr):
            array_type = arr["Type"]
            flag = list(filter(lambda x: x["Name"] == arr["Name"], self.list_arrcell_of_func))
            if not flag: self.list_arrcell_of_func.append(arr)
        return {"ASTType":"ArrayAccess", "Name":arr, "idx":idx[0], "Type":array_type, "Ele_Type": ele_type}

    def visitJSONAccess(self,ast,c):
        arr = self.visit(ast.json, c)
        flag = None
        if isinstance(ast.json, Id): flag = self.visit(ast.json, c)
        else: flag = self.visit(ast.json.method, c)
        if flag and not isinstance(flag["Type"], JSONType): 
            raise TypeMismatchInExpression(ast)  
        if isinstance(json, TypeCannotBeInferred): 
            return TypeCannotBeInferred(ast)
        if not arr and isinstance(ast.json, Id): 
            raise Undeclared(Identifier(), ast.json.name)
        idx = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, c)]], ast.idx, [[]])
        if list(filter(lambda x: isinstance(x, TypeCannotBeInferred), idx[0])): 
            return TypeCannotBeInferred(ast)
        flags = list(filter(lambda x: x["Type"] == StringType, idx[0]))
        if json["Type"]:
            if not isinstance(json["Type"],JSONType): 
                raise TypeMismatchInExpression(ast)
        else: json["Type"] = ArrayType([],None)
        if json["dimen"] and len(json["dimen"]) != len(idx[0]): 
            raise TypeMismatchInExpression(ast)
        if len(flags) != len(idx[0]): 
            raise TypeMismatchInExpression(ast)
        ele_type = None
        array_type = None
        for lst in c:
            flag = list(filter(lambda x: x["Name"] == json["Name"], lst))
            if flag:
                if flag[0]["Type"]: ele_type = flag[0]["Type"].element_type
                array_type = flag[0]["Type"]
        if isinstance(ast.json, CallExpr):
            array_type = json["Type"]
            flag = list(filter(lambda x: x["Name"] == json["Name"], self.list_arrcell_of_func))
            if not flag: self.list_arrcell_of_func.append(json)
        return {"ASTType":"JSONAccess", "Name":json, "idx":idx[0], "Type":json_type, "Ele_Type": ele_type}

    def visitCallStmt(self, ast, c):
        method = ast.method.name
        tmp = self.visit(ast.method, c)
        if tmp and tmp["ASTType"] != "FuncDecl": raise TypeMismatchInStatement(ast)
        for e in ast.param:
            if isinstance(e, Id): 
                if not self.visit(e, c): raise Undeclared(Identifier(), e.name)
        paramList = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, c)]], ast.param, [[]])
        
        void_type_lst = list(filter(lambda x: x["Name"] == method and x["Type"] != VoidType, c[-1]))
        if void_type_lst: raise TypeMismatchInStatement(ast)

        if method in self.list_build_in_func_name:
            current_func = list(filter(lambda x:x.name == method, self.global_envi))[0]
            current_param_list = current_func.mtype.intype
            if len(current_param_list) != len(paramList): 
                raise TypeMismatchInStatement(ast)
            if current_func.mtype.restype != VoidType: 
                raise TypeMismatchInStatement(ast)
            for e1, e2 in zip(current_param_list, paramList[0]):
                if isinstance(e1, IntType): return_type = IntType
                # if isinstance(e1,FloatType): return_type = FloatType
                if isinstance(e1,StringType): return_type = StringType
                if isinstance(e1,BoolType): return_type = BoolType
                if isinstance(e1,VoidType): return_type = VoidType
                if return_type != e2["Type"]: 
                    raise TypeMismatchInStatement(ast)
                return

        flags = list(filter(lambda x: x["Name"] == method, self.list_func_name_and_param))
        if not flags: raise Undeclared(Function(), method)
        if flags[0]["numParam"] != len(paramList[0]): 
            raise TypeMismatchInStatement(ast)


        flag = list(filter(lambda x: isinstance(x, TypeCannotBeInferred), paramList[0]))
        if flag: 
            raise TypeCannotBeInferred(ast)

        flag = list(filter(lambda x: x["Type"] == None, paramList[0]))
        if flag: 
            raise TypeCannotBeInferred(ast)

        cur = {"ASTType":"CallStmt", "Name": ast.method.name ,"paramList": paramList[0], "Type":VoidType}
        if not list(filter(lambda x:x["Name"] == method, self.list_called)): 
            self.list_called.append(cur)
            inferred_param_list = list(filter(lambda x:x["Name"] == method, self.list_called))[0]["paramList"]
            for e1, e2 in zip(paramList[0], inferred_param_list):
                e2["Type"] = e1["Type"]
            
        else:
            inferred_param_list = list(filter(lambda x:x["Name"] == method, self.list_called))[0]["paramList"]
            for e1, e2 in zip(paramList[0], inferred_param_list):
                if e1["Type"] != e2["Type"]:
                    raise TypeMismatchInStatement(ast)
                    

    def visitReturn(self, ast, c):

        if ast.expr:
            expr = self.visit(ast.expr, c)
            if isinstance(expr, TypeCannotBeInferred): 
                raise TypeCannotBeInferred(ast)
            return {"ASTType":"Return", "Type":expr["Type"]}
        else: 
            return {"ASTType":"Return", "Type":VoidType}

    def visitCallExpr(self, ast, c):
        method = ast.method.name
        for e in ast.param:
            if isinstance(e, Id): 
                if not self.visit(e, c): 
                    raise Undeclared(Identifier(), e.name)
        paramList = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, c)]], ast.param, [[]])
        flag = list(filter(lambda x: x["Name"] == method and x["Type"] == VoidType, c[-1]))
        if flag: raise TypeMismatchInExpression(ast)

        return_type = None

        if method in self.list_build_in_func_name:
            current_func = list(filter(lambda x:x.name == method, self.global_envi))[0]
            
            current_param_list = current_func.mtype.intype # param list of built in func
            if len(current_param_list) != len(paramList): 
                raise TypeMismatchInExpression(ast)
            if current_func.mtype.restype == VoidType: 
                raise TypeMismatchInExpression(ast) # return type of buitll in func
            for e1, e2 in zip(current_param_list, paramList[0]):
                if isinstance(e1, NumberType): return_type = NumberType
                # if isinstance(e1,FloatType): return_type = FloatType
                if isinstance(e1,BoolType): return_type = BoolType
                if isinstance(e1,StringType): return_type = StringType
                if isinstance(e1,VoidType): return_type = VoidType
                if return_type != e2["Type"]: 
                    raise TypeMismatchInExpression(ast)
            return {"ASTType":"CallExpr", "Name": ast.method.name, "dimen":[] ,"paramList": paramList[0], "Type":return_type}
        
        flags = list(filter(lambda x: x["Name"] == method, self.list_func_name_and_param))
        if not flags: raise Undeclared(Function(), method) # empty list
        if flags[0]["numParam"] != len(paramList[0]): 
            raise TypeMismatchInExpression(ast)

        flag = list(filter(lambda x: isinstance(x, TypeCannotBeInferred), paramList[0]))
        if flag: 
            return TypeCannotBeInferred(ast)

        flag = list(filter(lambda x: x["Type"] == None, paramList[0]))
        if flag: 
            return TypeCannotBeInferred(ast)

    
        flag = list(filter(lambda x: x["Name"] == method, c[-1]))
        dimen = []
        if flag:    
            return_type = flag[0]["Type"]
            if isinstance(flag[0]["Type"], ArrayType): dimen = flag[0]["Type"].dimen
        cur = {"ASTType":"CallExpr", "Name": ast.method.name, "dimen":dimen ,"paramList": paramList[0], "Type":return_type}
        
        if not list(filter(lambda x:x["Name"] == method, self.list_called_exp)): # lan dau goi, trong list_called chưa có 
            self.list_called.append(cur)
        elif list(filter(lambda x:x["Name"] == method, c[-1])):
            declared_param_list = list(filter(lambda x:x["Name"] == method, c[-1]))[0]["paramList"]
            
            for e1, e2 in zip(paramList[0], declared_param_list):
                if e1["Type"] != e2["Type"]:
                    raise TypeMismatchInExpression(ast)
        else:
            inferred_param_list = list(filter(lambda x:x["Name"] == method, self.list_called))[0]["paramList"]
            for e1, e2 in zip(paramList[0], inferred_param_list):
                if e1["Type"] != e2["Type"]:
                    raise TypeMismatchInExpression(ast)
        return cur

    def visitIf(self, ast, c):
        # print(viisted if stmt)
        expr = self.visit(ast.ifthenStmt[0][0], c)
        if isinstance(expr, TypeCannotBeInferred): 
            raise TypeCannotBeInferred(ast)

        if isinstance(ast.ifthenStmt[0][0], ArrayAccess):
            id = ast.ifthenStmt[0][0].arr
            if isinstance(id, CallExpr): 
                if not expr["Name"]["dimen"]: 
                    raise TypeCannotBeInferred(ast)
                id = id.method

            if not expr["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: expr["Ele_Type"] = flag[0]["Type"].element_type

            if not expr["Ele_Type"]: 
                expr["Ele_Type"] = BoolType
                if isinstance(id, CallExpr): 
                    expr["Name"]["Type"].element_type = BoolType

            flag = self.visit(id, c)
            if flag: flag["Type"].element_type = expr["Ele_Type"]
            else:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: flag[0]["Type"].element_type = expr["Ele_Type"]
            # print("expr = ", expr)
        else:
            if not expr["Type"]: expr["Type"] = BoolType
            if expr["Type"] != BoolType: 
                raise TypeMismatchInStatement(ast)

        env_in_if = [[]]
        env_in_if = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, acc)]], ast.ifthenStmt[0][1], env_in_if)
        env_in_if += c
        reduce(lambda acc, ele: self.visit(ele, env_in_if), ast.ifthenStmt[0][2], [])
        
        # else stmt
        env_in_else = [[]]
        env_in_if = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, acc)]], ast.elseStmt[0], env_in_if)
        env_in_else += c
        reduce(lambda acc, ele: self.visit(ele, env_in_if), ast.elseStmt[1], [])

    def visitForIn(self, ast, c):
        idx1 = self.visit(ast.idx1, c)
        expr1 = self.visit(ast.expr, c)
        if isinstance(expr1, TypeCannotBeInferred): 
            raise TypeCannotBeInferred(ast)

        if not idx1: 
            raise Undeclared(Identifier(), ast.idx1.name)
        if not idx1["Type"]: idx1["Type"] = NumberType
        if not expr1["Type"]: expr1["Type"] = NumberType
        if idx1["Type"] != NumberType or expr1["Type"] != NumberType: 
            raise TypeMismatchInStatement(ast)

        # loop
        envInForIn = [[]]
        envInForIn = reduce(lambda acc, ele: [acc[0] + [self.visit(ele,acc)]], ast.loop[0], envInForIn)
        envInForIn += c
        reduce(lambda acc, ele: self.visit(ele, envInForIn), ast.loop[1], envInForIn)
    
    def visitForOf(self, ast, c):
        idx1 = self.visit(ast.idx1, c)
        expr1 = self.visit(ast.expr, c)
        if isinstance(expr1, TypeCannotBeInferred): 
            raise TypeCannotBeInferred(ast)

        if not idx1: 
            raise Undeclared(Identifier(), ast.idx1.name)
        if not idx1["Type"]: idx1["Type"] = SringType
        if not expr1["Type"]: expr1["Type"] = JSONType
        if idx1["Type"] != StringType or expr1["Type"] != JSONType: 
            raise TypeMismatchInStatement(ast)

        # loop
        envInForOf = [[]]
        envInForOf = reduce(lambda acc, ele: [acc[0] + [self.visit(ele,acc)]], ast.loop[0], envInForOf)
        envInForOf += c
        reduce(lambda acc, ele: self.visit(ele, envInForIn), ast.loop[1], envInForOf)

    
    def visitWhile(self, ast, c):
        exp = self.visit(ast.exp, c)
        if isinstance(exp, TypeCannotBeInferred): 
            raise TypeCannotBeInferred(ast)
        if not exp["Type"]: exp["Type"] = BoolType
        if exp["Type"] != BoolType: 
            raise TypeMismatchInStatement(ast)

        envInWhile = [[]]
        envInWhile = reduce(lambda acc, ele: [acc[0] + [self.visit(ele, acc)]], ast.sl[0], envInWhile)
        envInWhile += c
        reduce(lambda acc, ele: self.visit(ele,envInWhile), ast.sl[1], [])

    
    def visitBreak(self, ast, c): pass

    def visitContinue(self, ast, c): pass

    def visitBinaryOp(self, ast, c):
    
        op = ast.op
        
        left = self.visit(ast.left, c)
        if isinstance(ast.left, Id) and left == None: 
            raise Undeclared(Identifier(), ast.left.name)
    
        right = self.visit(ast.right, c)
        if isinstance(ast.right, Id) and right == None: 
            raise Undeclared(Identifier(), ast.right.name)
        
        if isinstance(left, TypeCannotBeInferred): 
            return TypeCannotBeInferred(ast)
        if isinstance(right, TypeCannotBeInferred): 
            return TypeCannotBeInferred(ast)

        if isinstance(ast.left, ArrayAccess):
            id = ast.left.arr
            if isinstance(id, CallExpr): 
                if not left["Name"]["dimen"]: 
                    return TypeCannotBeInferred(ast)
                id = id.method

            if not left["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: left["Ele_Type"] = flag[0]["Type"].element_type

        if isinstance(ast.right, ArrayAccess):
            id = ast.right.arr
            if isinstance(id, CallExpr): 
                if not right["Name"]["dimen"]: 
                    return TypeCannotBeInferred(ast)
                id = id.method

            if not right["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: right["Ele_Type"] = flag[0]["Type"].element_type

        if op in ['+.']:

            left_index = "Type"
            right_index = "Type"
            if isinstance(ast.left, ArrayAccess): left_index = "Ele_Type"
            if isinstance(ast.right, ArrayAccess): right_index = "Ele_Type"
            if left[left_index] == None and right[right_index] == None:
                left[left_index] = StringType
                right[right_index] = StringType
            if left[left_index] == None: left[left_index] = right[right_index]
            if right[right_index] == None: right[right_index] = left[left_index]
            if right[right_index] != left[left_index]: 
                raise TypeMismatchInExpression(ast)
            if left[left_index] != StringType: 
                raise TypeMismatchInExpression(ast)
            return {"ASTType":"BinOp", "Type": StringType}
    
        if op in ['+', '-', '*', '/', '%']:

            left_index = "Type"
            right_index = "Type"
            if isinstance(ast.left, ArrayAccess): left_index = "Ele_Type"
            if isinstance(ast.right, ArrayAccess): right_index = "Ele_Type"
            if left[left_index] == None and right[right_index] == None:
                left[left_index] = NumberType
                right[right_index] = NumberType
            if left[left_index] == None: left[left_index] = right[right_index]
            if right[right_index] == None: right[right_index] = left[left_index]
            if right[right_index] != left[left_index]: 
                raise TypeMismatchInExpression(ast)
            if left[left_index] != NumberType: 
                raise TypeMismatchInExpression(ast)
            return {"ASTType":"BinOp", "Type": NumberType}
        # if op in ['+.', '-.', '*.', '\\.']:
        #     left_index = "Type"
        #     right_index = "Type"
        #     if left[left_index] == None and right[right_index] == None:
        #         left[left_index] = FloatType
        #         right[right_index] = FloatType
        #     if left[left_index] == None: left[left_index] = right[right_index]
        #     if right[right_index] == None: right[right_index] = left[left_index]
        #     if right[right_index] != left[left_index]: 
        #         raise TypeMismatchInExpression(ast)
        #     if left[left_index] != FloatType: 
        #         raise TypeMismatchInExpression(ast)
        #     return {"ASTType":"BinOp", "Type": FloatType}
        if op in ["&&", "||"]: 
            left_index = "Type"
            right_index = "Type"
            if left[left_index] == None and right[right_index] == None:
                left[left_index] = BoolType
                right[right_index] = BoolType
            if left[left_index] == None: left[left_index] = right[right_index]
            if right[right_index] == None: right[right_index] = left[left_index]
            if right[right_index] != left[left_index]: 
                raise TypeMismatchInExpression(ast)
            if left[left_index] != BoolType: 
                raise TypeMismatchInExpression(ast)
            return {"ASTType":"BinOp", "Type": BoolType}
        if op in ["==", "!=", "<", ">", "<=", ">="]:
            left_index = "Type"
            right_index = "Type" 
            if left[left_index] == None and right[right_index] == None:
                left[left_index] = NumberType
                right[right_index] = NumberType
            if left[left_index] == None: left[left_index] = right[right_index]
            if right[right_index] == None: right[right_index] = left[left_index]
            if right[right_index] != left[left_index]: 
                raise TypeMismatchInExpression(ast)
            if left[left_index] != NumberType: 
                raise TypeMismatchInExpression(ast)
            return {"ASTType":"BinOp", "Type": BoolType}
        
        if op in ["==.", "!=", "<", ">", "<=", ">="]:
            left_index = "Type"
            right_index = "Type" 
            if left[left_index] == None and right[right_index] == None:
                left[left_index] = StringType
                right[right_index] = StringType
            if left[left_index] == None: left[left_index] = right[right_index]
            if right[right_index] == None: right[right_index] = left[left_index]
            if right[right_index] != left[left_index]: 
                raise TypeMismatchInExpression(ast)
            if left[left_index] != StringType: 
                raise TypeMismatchInExpression(ast)
            return {"ASTType":"BinOp", "Type": BoolType}
        
        # if op in ["<.", ">.", "<=.", ">=.", "=/="]: 
        #     left_index = "Type"
        #     right_index = "Type"
        #     if left[left_index] == None and right[right_index] == None:
        #         left[left_index] = FloatType
        #         right[right_index] = FloatType
        #     if left[left_index] == None: left[left_index] = right[right_index]
        #     if right[right_index] == None: right[right_index] = left[left_index]
        #     if right[right_index] != left[left_index]: 
        #         raise TypeMismatchInExpression(ast)
        #     if left[left_index] != FloatType: 
        #         raise TypeMismatchInExpression(ast)
        #     return {"ASTType":"BinOp", "Type": BoolType}

    def visitUnaryOp(self, ast, c):
        op = ast.op
        body = self.visit(ast.body, c)
        if isinstance(ast.body, Id) and body == None: 
            raise Undeclared(Identifier(), ast.body.name)

        if isinstance(body, TypeCannotBeInferred): 
            return TypeCannotBeInferred(ast)

        if isinstance(ast.body, ArrayAccess):
            id = ast.body.arr
            if isinstance(id, CallExpr): 
                if not body["Name"]["dimen"]: 
                    return TypeCannotBeInferred(ast)
                id = id.method

            if not body["Ele_Type"]:
                flag = list(filter(lambda x:x["Name"] == id.name, self.list_arrcell_of_func))
                if flag: body["Ele_Type"] = flag[0]["Type"].element_type

        if op in ["-"]:
            if body["Type"] == None: body["Type"] = IntType
            if body["Type"] != IntType: raise TypeMismatchInExpression(ast)
            return {"ASTType":"UnaryOp", "Type":IntType}

        # if op in ["-."]:
        #     if body["Type"] == None: body["Type"] = FloatType
        #     if body["Type"] != FloatType: raise TypeMismatchInExpression(ast)
        #     return {"ASTType":"UnaryOp", "Type":FloatType}

        if op in ["!"]:
            if body["Type"] == None: body["Type"] = BoolType
            if body["Type"] != BoolType: raise TypeMismatchInExpression(ast)
            return {"ASTType":"UnaryOp", "Type":BoolType}
    def visitId(self, ast, c):
        for lst in c:
            flags = list(filter(lambda x: x["Name"] == ast.name, lst))
            if flags: return flags[0] 
        return None

    def visitIntLiteral(self, ast, c):
        return {"ASTType": "Literal", "Type": IntType}
    
    def visitNumberLiteral(self, ast, c):
        return {"ASTType": "Literal", "Type": NumberType}

    # def visitFloatLiteral(self, ast, c):
    #     return {"ASTType": "Literal", "Type": FloatType}

    def visitBooleanLiteral(self, ast, c):
        return {"ASTType": "Literal", "Type": BoolType}

    def visitArrayLiteral(self, ast, c):
        ele_type = None
        if ast.value: ele_type = self.visit(ast.value[0], c)["Type"]
        return {"ASTType": "Literal", "Type": ArrayType(ast.value, ele_type)}

    def visitStringLiteral(self, ast, c):
        return {"ASTType": "Literal", "Type": StringType}
    
    def visitJSONLiteral(self, ast, c):
        return {"ASTType": "Literal", "Type": JSONType}
