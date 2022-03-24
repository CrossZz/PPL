import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


class CheckSuite(unittest.TestCase):    
    def test_497(self):
        input="""
        Let a;
        Function main(){
          Call(foo,[a]);
        }
        Function foo(){

        }
        """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,497))
    def test_498(self):
        input="""
        Let a: Number;
        Let x[a,3]: Number;
        Function main(b[3,3,3]){
            x=b;
        }
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,498))
    def test_499(self):
        input="""
        Let a: Number;
        Let b;
        Let x[a,b]: Number;
        Function main(b[3,3,3]){
            x=b;
        }
        """
        expect = str(TypeCannotBeInferred(VarDecl(Id("x"),[Id("a"),Id("b")],NumberType(),None)))
        self.assertTrue(TestChecker.test(input,expect,499))
    def test_409(self):
        input="""
        Let a: Number;
        Function main() {
            For x In a {

            }
        }
        """
        expect = str(TypeMismatchInStatement(ForIn(Id("x"),Id("a"),[])))
        self.assertTrue(TestChecker.test(input,expect,409))
    def test_439(self):
        input="""
        Let a[2,3]: Number;
        Function main() {
            Constant $b = [[1,2,3],[1,2,3]];
            For x In a {
                x = $b;
            }
        }
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),Id("$b"))))
        self.assertTrue(TestChecker.test(input,expect,439))
    def test_440(self):
        input="""
        Let a: Number, b =3;
        Let c[a,b]: Number;
        Function main() {
            For x In c {
                For y In x {
                    y = True;
                }
            }
        }
        """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,440))
    def test_448(self):
        input="""
        Let a: Number;
        Function main() {
           For x Of a {

           }
        }
        """
        expect = str(TypeMismatchInStatement(ForOf(Id("x"),Id("a"),[])))
        self.assertTrue(TestChecker.test(input,expect,448))
    def test_449(self):
        input="""
        Let a: JSON;
        Function main() {
            For x Of a {
                x= 6;
                x= True;
                x= n;
            }
        }
        """
        expect = str(Undeclared(Identifier(),"n"))
        self.assertTrue(TestChecker.test(input,expect,449))
    def test_450(self):
        input="""
        Let a: JSON;
        Function main() {
            For x Of a {
                x = a{"m"} + True ;
            }
        }
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+",JSONAccess(Id("a"),[StringLiteral("m")]),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,450))
    def test_452(self):
        input="""
        Let a: JSON;
        Function main() {
            For x Of a {
                x = a{"m"} +. 1 ;
            }
        }
        """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",JSONAccess(Id("a"),[StringLiteral("m")]),NumberLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,452))
    def test_461(self):
        input="""
        Let a: JSON;
        Function main() {
            If (a{"m"}>True) {
                
            }
        }
        """
        expect = str(TypeMismatchInExpression(BinaryOp(">",JSONAccess(Id("a"),[StringLiteral("m")]),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,461))
    def test_468(self):
        input="""
        Let a: JSON;
        Function main() {
            a{"n"} = 1+3;
            Let a: Number;
            a{"n"} =0;
        }
        """
        expect = str(TypeMismatchInExpression(JSONAccess(Id("a"),[StringLiteral("n")])))
        self.assertTrue(TestChecker.test(input,expect,468))
    def test_494(self):
        input="""
        Let x;
        Function main(x){

        }
        Let y;
        Function a(){
            x=1;
        }
        Let y;
        """
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_495(self):
        input="""
        Let x;
        Function main(x){

        }
        Let y;
        Function a(){
            Let o;
            x=1;
            Let o;
        }
        """
        expect = str(Redeclared(Variable(),"o"))
        self.assertTrue(TestChecker.test(input,expect,495))
    def test_496(self):
        input="""
        Let x;
        Function main(x){

        }
        Let y;
        Function a(){
            Let o;
            x=1;
            x=2;
            x="s";
        }
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),StringLiteral("s"))))
        self.assertTrue(TestChecker.test(input,expect,496))
    def test_401(self):
        input = """
            
            """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input,expect,401))
    def test_402(self):
        input = """
                Let main;
                Function main(){
                    
                }  

            """
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,402))
    def test_403(self):
        input = """
                Function main(x){
                    x=1;
                    x= "String";
                }
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),StringLiteral("String"))))
        self.assertTrue(TestChecker.test(input,expect,403))
    def test_404(self):
        input = """
                Function foo(x){
                    Return 1;
                }
                Function main(){
                    Let x, y = 0.5;
                    x = 1 + Call(foo,[1]);
                    y = Call(foo,["S"]) - 1;
                }
            """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[StringLiteral("S")])))
        self.assertTrue(TestChecker.test(input,expect,404))
    def test_405(self):
        input = """
                Function foo(x){

                }
                Function main(){
                   Let x, y = 0.5;
                    Call(foo,[x]);
                }
            """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,405))
    def test_406(self):
        input = """
        Function foo(){

        }
        Function main(main){
            Let foo;
            foo = foo + Call(main,[]);
            Return 1;
        }
        
                   """
        expect = str(Undeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,406))
    def test_407(self):
        input = """
            Function main(x,y){
                x = 1; 
                Call(main,["v", 0]); 
            } 
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[StringLiteral("v"),NumberLiteral(0.0)])))
        self.assertTrue(TestChecker.test(input,expect,407))
    def test_408(self):
        input = """
            Function foo(x,y){

            } 
            Function main(x,y){
                Call(foo,[1,2]);  
                Call(foo,[1.0,True]); 
            }
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[NumberLiteral(1.0),BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input,expect,408))
        
    def test_410(self):
        input = """
            Function main(x){
                Let y = True; 
                x = 1.0; 
                Call(main,[y]);
            }      
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,410))
        
    def test_411(self):
        input = """
            Function main(x){
                Let y = True; 
                Call(main,[y]); 
                x = 1.0;
            } 
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),NumberLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,411))
        
    def test_412(self):
        input = """Function main(){
                Call(print,[Call(read,[4])]);
        } 
        """
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[NumberLiteral(4.0)])))
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        input = Program([FuncDecl(Id("main"),[],[CallStmt(Id("print"),[CallExpr(Id("read"),[NumberLiteral(4.0)])])])])
        expect = str(TypeMismatchInExpression(CallExpr(Id("read"),[NumberLiteral(4.0)])))
        self.assertTrue(TestChecker.test(input,expect,413))
        
    def test_414(self):
        input = """Function main(){ 
                        Call(printLn,[]);
                    }  
                  """
        expect = str(TypeMismatchInStatement(CallStmt(Id("printLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,414))
        
    def test_415(self):
        input = Program([FuncDecl(Id("main"),[],[CallStmt(Id("printLn"),[])])])
        expect = str(TypeMismatchInStatement(CallStmt(Id("printLn"),[])))
        self.assertTrue(TestChecker.test(input,expect,415))
        
    def test_416(self):
        input = Program([FuncDecl(Id("main"),[],[CallStmt(Id("foo"),[])])])
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,416))
        
    def test_417(self):
        input = """
                Function main(x,y,z,t,k){
                    y= x + y / z * t;
                    x= k % t;
                    y= x == z;
                }

            """
        expect = str(TypeMismatchInStatement(Assign(Id("y"),BinaryOp("==",Id("x"),Id("z")))))
        self.assertTrue(TestChecker.test(input,expect,417))
        
    def test_418(self):
        input = """ 
            Function main(global_var){
                global_var = 25+6-2.5%True/100 ; 
            } 
        """
        expect = str(TypeMismatchInExpression(BinaryOp("%",NumberLiteral(2.5),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,418))
        
    def test_419(self):
        input = """
                Let a[1,2]= [[1,2]];
                Function main(x){
                    a[1,2] = x;
                    x[1] = 1;
                }
            """
        expect = str(TypeMismatchInExpression(ArrayAccess(Id("x"),[NumberLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input,expect,419))
        
    def test_420(self):
        input = """                
                Function main(){
                    Let a[5]= [1,2,3,4,5];
                    Let b[5];
                    a=b;
                    a[5]=b;
                }
            """
        expect = str(TypeMismatchInStatement(Assign(ArrayAccess(Id("a"),[NumberLiteral(5.0)]),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,420))
    def test_421(self):
        input = """
                Function main(){
                    Let a[5]= [1,2,3,4,5];
                    Let b[5];
                    b= [True,True,True,True,True];
                    a=b;
                }
            """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test_422(self):
        input = """               
                Function main() {
                    Let a[5]= [1,2,3,4,5];
                    Let b[2,4]= [[1,2,3,4],[1,2,3,4]];
                    a=b;
                }
            """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,422))
        
    def test_423(self):
        input = """             
                Function main(){
                    Let a[5]= [1,2,3,4,5];
                    Let b[5];
                    Let c;
                    c = b[5] +. 1;
                }
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",ArrayAccess(Id("b"),[NumberLiteral(5.0)]),NumberLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,423))
        
    def test_424(self):
        input = """                
                Function main(){
                    Let a[5],b[5];
                    a=b;
                }
            """
        expect = str(TypeCannotBeInferred(Assign(Id("a"),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,424))
        
    def test_425(self):
        input = """                
                Let x[5]=[1,2];
                Let x=1;
                Function main() {

                }            
        """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,425))
        
    def test_426(self):
        input = """
                Let x;
                Function main(){
                    Let x;
                    Let main;
                    Let x[5]=[1,2,3,4,5];
                }
            """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,426))
        
    def test_427(self):
        input = """
                Function main(){ 
                }
                Function main(x){ 
                }
            """
        expect = str(Redeclared(Function(),"main"))
        self.assertTrue(TestChecker.test(input,expect,427))
        
    def test_428(self):
        input = """
                Function main(x){ 
                    Let x;
                }
            """
        expect = str(Redeclared(Variable(),"x"))
        self.assertTrue(TestChecker.test(input,expect,428))
        
    def test_429(self):
        input = """
                Function main(x,x){ 
                }
            """
        expect = str(Redeclared(Parameter(),"x"))
        self.assertTrue(TestChecker.test(input,expect,429))
        
    def test_430(self):
        input = """
                Let x;
                Function main(x){
                    x=foo;
                }
            """
        expect = str(Undeclared(Identifier(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_431(self):
        input = """               
                Function main(){
                    Call(foo,[]);
                }
            """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_432(self):
        input = """
                Function foo(x){

                }
                Function main(x,y,a){
                    y = a + Call(foo,[x]);
                }

                
            """
        expect = str(TypeCannotBeInferred(Assign(Id("y"),BinaryOp("+",Id("a"),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,432))
        
    def test_433(self):
        input = """
                Function main(){
                    Let x,y;
                    x=y;
                }
            """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,433))
        
    def test_434(self):
        input = """
                Function foo(x){

                }
                Function main(){
                    Let x;
                    If (Call(foo,[x])){
                        x=1;
                    }
                }
                
            """
        expect = str(TypeCannotBeInferred(If([(CallExpr(Id("foo"),[Id("x")]),[Assign(Id("x"),NumberLiteral(1.0))])],[])))
        self.assertTrue(TestChecker.test(input,expect,434))
        
    def test_435(self):
        input = """
                Function foo(x,y){
                    
                }
                Function main(){
                    Let x=1,y;
                    Call(foo,[x,y]);
                }
            """
        expect = str(TypeCannotBeInferred(CallStmt(Id("foo"),[Id("x"),Id("y")])))
        self.assertTrue(TestChecker.test(input,expect,435))
        
    def test_436(self):
        input = """
                Function foo(x){ 

                }
                Function main(){
                    Let x;
                    x = 1 + Call(foo,[x]);
                }               
                

            """
        expect = str(TypeCannotBeInferred(Assign(Id("x"),BinaryOp("+",NumberLiteral(1.0),CallExpr(Id("foo"),[Id("x")])))))
        self.assertTrue(TestChecker.test(input,expect,436))
        
    def test_437(self):
        input = """
            Function main(){ 
                Let x;
                If (x) {
                    Let y;
                }
                y=1;
            }
            """
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,437))
        
    def test_438(self):
        input = """
                Function main(){
                    Let x;
                    If (x){
                        x=1;
                    }
                    Else{
                        Let y,z;
                        y = x;
                    }
                }
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),NumberLiteral(1.0))))
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_441(self):
        input = """
                Function foo(x){

                }
                Function main(){
                    Let x;
                    While (Call(foo,[x])){
                        x=1;
                    }
                }
                
            """
        expect = str(TypeCannotBeInferred(While(CallExpr(Id("foo"),[Id("x")]),[Assign(Id("x"),NumberLiteral(1.0))])))
        self.assertTrue(TestChecker.test(input,expect,441))
        
    def test_442(self):
        input = """ 
        Let a = True, d = "string";
        ##this  is comment##
        Function main(a[123], b , x){ 
            Let y;
            While (True){
                Let y; 
                y = y + 1;
                Call(main,[a,y,d]);
            }
        }
        """
        expect = str(TypeCannotBeInferred(CallStmt(Id("main"),[Id("a"),Id("y"),Id("d")])))
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_443(self):
        input = """  
                Function foo(x){

                }              
                Function main(x){
                    x= 1+ Call(foo,[1]);
                    Call(foo,[1]);
                }
                
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[NumberLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input,expect,443))
        
    def test_444(self):
        input = """
                Function foo(x){

                }
                Function main(x){
                    Call(foo,[1]);
                    x= 1 + Call(foo,[1]);
                }
                
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+",NumberLiteral(1.0),CallExpr(Id("foo"),[NumberLiteral(1.0)]))))
        self.assertTrue(TestChecker.test(input,expect,444))
        
    def test_445(self):
        input = """
                Function foo(x){

                }
                Function main(){
                    Let x,y;
                    x= y + Call(foo,[1,2]);
                }
            """
        expect = str(TypeMismatchInExpression(CallExpr(Id("foo"),[NumberLiteral(1.0),NumberLiteral(2.0)])))
        self.assertTrue(TestChecker.test(input,expect,445))
        
    def test_446(self):
        input = """Function main(a){
            While (a ==. "s"){
                While (a<100){
                    a=a-30;
                }
            }
        }
        """
        expect = str(TypeMismatchInExpression(BinaryOp("<",Id("a"),NumberLiteral(100.0))))
        self.assertTrue(TestChecker.test(input,expect,446))
        
    def test_447(self):
        input = """
                Function main(){
                    Let x=1;
                    If (x){

                    }
                }
            """
        expect = str(TypeMismatchInStatement(If([(Id("x"),[])],[])))
        self.assertTrue(TestChecker.test(input,expect,447))

    def test_451(self):
        input = """
                Function main(){
                    Let x=1,y;
                    While (x){

                    }
                }
            """
        expect = str(TypeMismatchInStatement(While(Id("x"),[])))
        self.assertTrue(TestChecker.test(input,expect,451))
        
        
    def test_453(self):
        input = """
                Function foo(){

                }
                Function main(){
                    Let x;
                    Call(foo,[]);
                    Call(foo,[]) = x+1;
                }
            """
        expect = str(TypeMismatchInStatement(Assign(CallExpr(Id("foo"),[]),BinaryOp("+",Id("x"),NumberLiteral(1.0)))))
        self.assertTrue(TestChecker.test(input,expect,453))
        
    def test_454(self):
        input = """
                Function foo(){

                }
                Function main(){
                    Let x;
                    Call(foo,[]);
                    x = Call(foo,[]);
                }
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,454))
        
    def test_455(self):
        input = """
                Function foo(){
                    Return 1;
                }
                Function main(){
                    Call(foo,[]);
                }
                
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[])))
        self.assertTrue(TestChecker.test(input,expect,455))
        
    def test_456(self):
        input = """
                Function foo(){
                    Return 1.5;
                }
                Function main(){
                    Let x;
                    x = "1" +. Call(foo,[]);
                }
                
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",StringLiteral("1"),CallExpr(Id("foo"),[]))))
        self.assertTrue(TestChecker.test(input,expect,456))
        
    def test_457(self):
        input = """                
                Function main(){
                    Let x;
                    If (x) {
                        Return "s";
                    }
                    Else {
                        Return 1.5;
                    }
                }
            """
        expect = str(TypeMismatchInStatement(Return(NumberLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,457))
        
    def test_458(self):
        input = """
         Function foo(x1,x2){
            Return;
        }
        Function main(){
            Let x;
            Call(foo,[1,2]);
            x = Call(foo,[5,99]);
            Return 0;
        }
       
        """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),CallExpr(Id("foo"),[NumberLiteral(5.0),NumberLiteral(99.0)]))))
        self.assertTrue(TestChecker.test(input,expect,458))
        
    def test_459(self):
        input = """
                Function main(){
                    Let x;
                    Return x;
                }
            """
        expect = str(TypeCannotBeInferred(Return(Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,459))
        
    def test_460(self):
        input = """
                Function main(){
                    Let a[1,2];
                    a[1+1,"s"] = 1;
                }
            """
        expect = str(TypeMismatchInExpression(ArrayAccess(Id("a"),[BinaryOp("+",NumberLiteral(1.0),NumberLiteral(1.0)),StringLiteral("s")])))
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_462(self):
        input = """
                Function foo(n){
                    Let x[1,2]=[[1,2]] ;
                    Return x;
                }
                Function main(){
                    Let x;
                    Call(foo,[x])[x+3,True]=1;
                }
            """
        expect = str(TypeMismatchInExpression(ArrayAccess(CallExpr(Id("foo"),[Id("x")]),[BinaryOp("+",Id("x"),NumberLiteral(3.0)),BooleanLiteral(True)])))
        self.assertTrue(TestChecker.test(input,expect,462))
        
    def test_463(self):
        input = """
                
                Let x;
                Function fact(n){
                    If (n == 0){
                        Return 1;
                    }
                    Else{
                        Return n * Call(fact,[n - 1]);
                    }
                }
                Function main(){
                    x = 10;
                    Call(fact,[x]);
                }
            """
        expect = str(TypeMismatchInStatement(CallStmt(Id("fact"),[Id("x")])))
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_464(self):
        input = """
                Function foo(a[5], b){
                    Let i;
                    While (i < 5){
                        a[i] = b + 1.0;
                        i = i + 1;
                    }
                    i= True;
                }
                Function main(){

                }
            """
        expect = str(TypeMismatchInStatement(Assign(Id("i"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,464))
        
    def test_465(self):
        input = """
                Function main(){
                    Let a[5]=[1,2,3,4,5];
                    Let b[2,3]=[[1,2,3],[4,5,6]];
                    a[3 + Call(foo,[2])] = a[b[2,3]] + 4.0;
                }
            """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,465))
        
    def test_466(self):
        input = """
                Function foo(x,y){
                    Call(foo,[2 + x, 4. / y]);
                    Call(foo,[x,y]);
                }
                Function main(){
                    Call(foo,[3,"S"]);
                }         
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[NumberLiteral(3.0),StringLiteral("S")])))
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_467(self):
        input = """
                Function main(){
                    If (True){

                    }
                    Elif (True){
                        Let a[1],b;
                        a[1]=b;
                    }
                        
                }
            """
        expect = str(TypeCannotBeInferred(Assign(ArrayAccess(Id("a"),[NumberLiteral(1.0)]),Id("b"))))
        self.assertTrue(TestChecker.test(input,expect,467))
        
    def test_469(self):
        input = """
                Let a[3]:String =["Mot","2","Three"];
                Function main(){
                    a[1] = a[1] + a[2];
                }
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+",ArrayAccess(Id("a"),[NumberLiteral(1.0)]),ArrayAccess(Id("a"),[NumberLiteral(2.0)]))))
        self.assertTrue(TestChecker.test(input,expect,469))
        
    def test_470(self):
        input = """
                Function main(){
                    Let a,b,c,d;
                    a = a + b || c - d;
                }
            """
        expect = str(TypeMismatchInExpression(BinaryOp("||",BinaryOp("+",Id("a"),Id("b")),BinaryOp("-",Id("c"),Id("d")))))
        self.assertTrue(TestChecker.test(input,expect,470))
    def test_471(self):
        input = """
            Function main(){
                Let sum: Number = 0, a = 1;
                While (a < 10){
                    Let b, cal = 1;
                    While (b < 10){
                        cal = cal * b;
                        b = b + 1;
                    }
                    sum = sum + prod;
                    a = a + 1;
                }
            }
            """
        expect = str(Undeclared(Identifier(),"prod"))
        self.assertTrue(TestChecker.test(input,expect,471))
        
    def test_472(self):
        input = """
            Function main(){
                Let a=1,x; 
                a= Call(foo,[x]); 
            }             
            """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,472))
        
    def test_473(self):
        input = """
                Function main(){
                    Let x;
                    If (True){
                        x = 3;
                    }
                    Else {
                        x = True;
                    }
                }
            """
        expect = str(TypeMismatchInStatement(Assign(Id("x"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,473))
        
    def test_474(self):
        input = """
                Let x =1;
                Function main(y){
                    x = y + Call(main,["s"]) ;
                }
            """
        expect = str(TypeMismatchInExpression(CallExpr(Id("main"),[StringLiteral("s")])))
        self.assertTrue(TestChecker.test(input,expect,474))
        
    def test_475(self):
        input = """
        Let x =1;
        Function main(y){
            x = Call(main,["s"]) + y;
        }
         """
        expect = str(TypeMismatchInExpression(BinaryOp("+",CallExpr(Id("main"),[StringLiteral("s")]),Id("y"))))
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_476(self):
        input = """
                Function main(x){
                    Let y;
                    While (y){
                        x=True;
                        Call(main,[0.5]);
                    } 
                }
                """
        expect = str(TypeMismatchInStatement(CallStmt(Id("main"),[NumberLiteral(0.5)])))
        self.assertTrue(TestChecker.test(input,expect,476))
        
    def test_477(self):
        input = """
                Function main(x, a, b, c){
                    If(x == ((False||True) && (a > b + c))){
                        a = b - c;
                    }
                    Else{
                        a = b + c;
                        x = True;
                    }
                        
                }
            """
        expect = str(TypeMismatchInExpression(BinaryOp("==",Id("x"),BinaryOp("&&",BinaryOp("||",BooleanLiteral(False),BooleanLiteral(True)),BinaryOp(">",Id("a"),BinaryOp("+",Id("b"),Id("c")))))))
        self.assertTrue(TestChecker.test(input,expect,477))
        
    def test_478(self):
        input = """
                Let abc[2,3,4];
                Function foo(x[2]){
                     x[1] = 1;
                    abc[1] = 2.;
                }
                Let nm;
                Function main(){
                    Let z[2,3,4] = [1.,2.];
                    Let w[2] = [3.,4.];
                    Let x;
                    abc = z;
                    Call(foo,[x]);
                }
                """
        expect = str(TypeMismatchInExpression(ArrayAccess(Id("abc"),[NumberLiteral(1.0)])))
        self.assertTrue(TestChecker.test(input,expect,478))
    def test_479(self):
        input = """
                Let abc[5];
                Function foo(x[2]){
                    x[1] = 1;
                    abc[1] = 2;
                }
                Function main(){
                    Let z[2] = [1,2];
                    Let w[2] = [True,False];
                    Let x;
                    abc[1] = 1;
                    Call(foo,[z]);
                    Call(foo,[w]);
                }
               """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[Id("w")])))
        self.assertTrue(TestChecker.test(input,expect,479))
        
    def test_480(self):
        input = """
                Let abc[5];
                Function foo(x[2]){
                    x[1] = 1;
                    abc[1] = True;
                }
                Function main(){
                    Let z[2] = [1,2];
                    Let w[2] = [3,4];
                    Let x;
                    abc[1] = 1.5; 
                }
                """
        expect = str(TypeMismatchInStatement(Assign(ArrayAccess(Id("abc"),[NumberLiteral(1.0)]),NumberLiteral(1.5))))
        self.assertTrue(TestChecker.test(input,expect,480))
        
    def test_481(self):
        input = """
                Function foo(x[2]){

                }
               
                Function main(){
                    Let z[2] = [1,2];
                    Let w[2] = [3,4];
                    Let x;
                    Call(foo,[z]);
                    Call(foo,[w[2]]);
                }
                 """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"),[ArrayAccess(Id("w"),[NumberLiteral(2.0)])])))
        self.assertTrue(TestChecker.test(input,expect,481))
        
    def test_482(self):
        input = """
                    Function main(x){
                        y= x + Call(main,[0.5]);
                    }
                    """
        expect = str(Undeclared(Identifier(),"y"))
        self.assertTrue(TestChecker.test(input,expect,482))
        
    def test_483(self):
        input = """
                Function main(){
                    If (True){
                        Let a;
                        Let x;
                        Let y;
                        x = 1;
                        y = 2;
                        z = 3;
                    }
                } 
            """
        expect = str(Undeclared(Identifier(),"z"))
        self.assertTrue(TestChecker.test(input,expect,483))

        
    def test_485(self):
        input = """
        Function main(){
            Let x[5];
            If (True){
                While (True){
                    Return x;
                }
            }
        }
        """
        expect = str(TypeCannotBeInferred(Return(Id("x"))))
        self.assertTrue(TestChecker.test(input,expect,485))
        
    def test_486(self):
        input = """
        Function main(n){
            Let x;
            While (x>1){
                If (x==1){
                    Return;
                }
            }
            Return True;
        } 
        """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,486))
    def test_500(self):
        input = """
        Function main(n){
            Let x;
            While (x>1){
                If (x==1){
                    Return;
                }
            }
            Return True;
        } 
        """
        expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,500))
    def test_487(self):
        input = """
        Function main(n){
            Let a;
            While(a!=3){
                Let b;
                While(b!=4){

                }
            }                
            a=True;
        } 
        """
        expect = str(TypeMismatchInStatement(Assign(Id("a"),BooleanLiteral(True))))
        self.assertTrue(TestChecker.test(input,expect,487))
        
    def test_488(self):
        input = """
        Function main(x,y){
            While (True){
                Return Call(main,[x,y]);
            }
        } 
            """
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id("main"),[Id("x"),Id("y")]))))
        self.assertTrue(TestChecker.test(input,expect,488))
        
    def test_489(self):
        input = """
        Let a;
        Function main(n){
            While (True){
                Return a+3;
            }
            Return a +. "s";
        } 
            """
        expect = str(TypeMismatchInExpression(BinaryOp("+.",Id("a"),StringLiteral("s"))))
        self.assertTrue(TestChecker.test(input,expect,489))
        
    def test_490(self):
        input = """
        Function main(x,y){
            Return Call(main,[x +3,y + 10.2]);
        } 
            """
        expect = str(TypeCannotBeInferred(Return(CallExpr(Id("main"),[BinaryOp("+",Id("x"),NumberLiteral(3.0)),BinaryOp("+",Id("y"),NumberLiteral(10.2))]))))
        self.assertTrue(TestChecker.test(input,expect,490))
    
    def test_491(self):
        input = """
                Function main(a,b,c) {
                    a= (a==b)!= c +3;
                }
            """
        expect = str(TypeMismatchInExpression(BinaryOp("!=",BinaryOp("==",Id("a"),Id("b")),BinaryOp("+",Id("c"),NumberLiteral(3.0)))))
        self.assertTrue(TestChecker.test(input,expect,491))
    def test_492(self):
        input = """
            Function main(n){
                If (n == 0){
                    If (n!=0){
                        If (n!=0){
                             a=5;
                        }       
                    }
                }
            } 
            """
        expect = str(Undeclared(Identifier(),"a"))
        self.assertTrue(TestChecker.test(input,expect,492))
        
    def test_493(self):
        input = """
        Let x;
        Function foo(){
            x = 2;
        }
        Function main(x[5]){
            x = [1.,2.,3.,4.,5.];
        }   
        
        """
        expect = str()
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_484(self):
        input = """
            Function main(){
                Let a=1,x; 
                a= Call(foo,[x]); 
            } 
            """
        expect = str(Undeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input,expect,484))


