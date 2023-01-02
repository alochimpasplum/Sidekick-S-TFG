import Constants
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonParser import PythonParser
from FontCode.ANTLR4_Parser.Antlr4_Files.PythonVisitor import PythonVisitor
from FontCode.ANTLR4_Parser.Expressions.Number import Number
from FontCode.ANTLR4_Parser.Expressions.Variable import Variable
from FontCode.ANTLR4_Parser.Expressions.Expression import Expression
from FontCode.ANTLR4_Parser.Expressions.Function import Function
from FontCode.ANTLR4_Parser.Expressions.MainFunction import MainFunction
from FontCode.ANTLR4_Parser.Expressions.CustomFunction import CustomFunction
from FontCode.ANTLR4_Parser.Expressions.BuiltFunction import BuiltFunction
from FontCode.ANTLR4_Parser.Expressions.Var import Var
from FontCode.ANTLR4_Parser.Expressions.VariableDeclaration import VariableDeclaration
from FontCode.ANTLR4_Parser.Expressions.VariableAssign import VariableAssign
from FontCode.ANTLR4_Parser.Expressions.Print import Print
from FontCode.ANTLR4_Parser.Expressions.MathOperation import MathOperation
from FontCode.ANTLR4_Parser.Expressions.Scan import Scan
from FontCode.ANTLR4_Parser.Expressions.Conditional import Conditional
from FontCode.ANTLR4_Parser.Expressions.ConditionalBranches import ConditionalBranches
from FontCode.ANTLR4_Parser.Expressions.ConditionalBranch import ConditionalBranch
from FontCode.ANTLR4_Parser.Expressions.ConditionalLines import ConditionalLines
from FontCode.ANTLR4_Parser.Expressions.If import If
from FontCode.ANTLR4_Parser.Expressions.SwitchCase import SwitchCase
from FontCode.ANTLR4_Parser.Expressions.MathOperationSimplified import MathOperationSimplified


class AntlrToExpression(PythonVisitor):

    def visitScan(self, ctx: PythonParser.ScanContext):
        storing_var: Expression = self.visit((ctx.getChild(1)))
        return Scan(storing_var)

    def visitFunction(self, ctx: PythonParser.FunctionContext):
        child: Expression = self.visit(ctx.getChild(0))
        return Function(child)

    def visitMath_Operation(self, ctx: PythonParser.Math_OperationContext):
        assign: Expression = self.visit(ctx.getChild(0))
        left: Expression = self.visit(ctx.getChild(2))
        right: Expression = self.visit(ctx.getChild(4))
        operation: str = ctx.getChild(3).getText()
        return MathOperation(operation, assign, left, right)

    def visitConditional(self, ctx: PythonParser.ConditionalContext):
        condition: Expression = self.visit(ctx.getChild(1))
        branches: Expression = self.visit(ctx.getChild(2))
        return Conditional(condition, branches)

    def visitVariable(self, ctx: PythonParser.VariableContext):
        name: str = ctx.getChild(0).getText()
        return Variable(name)

    def visitConditional_branch(self, ctx: PythonParser.Conditional_branchContext):
        condition: Expression = self.visit(ctx.getChild(1))
        conditional_lines: Expression = self.visit(ctx.getChild(2))
        return ConditionalBranch(condition, conditional_lines)

    def visitConditional_branches(self, ctx: PythonParser.Conditional_branchesContext):
        branches: [Expression] = []

        for i in range(0, ctx.getChildCount()):
            branches.append(self.visit(ctx.getChild(i)))

        return ConditionalBranches(branches)

    def visitConditional_lines(self, ctx: PythonParser.Conditional_linesContext):
        lines: [Expression] = []

        for i in range(0, ctx.getChildCount()):
            lines.append(self.visit(ctx.getChild(i)))

        return ConditionalLines(lines)

    def visitIf(self, ctx: PythonParser.IfContext):
        left: Expression = self.visit(ctx.getChild(0))
        right: Expression = self.visit(ctx.getChild(2))
        condition: str = ctx.getChild(1).getText()
        return If(left, right, condition)

    def visitNumber(self, ctx: PythonParser.NumberContext):
        num: str = ctx.getChild(0).getText()
        return Number(int(num))

    def visitMain_function(self, ctx: PythonParser.Main_functionContext):
        name: str = ctx.getChild(0).getText()
        return MainFunction(name)

    def visitCustom_function(self, ctx: PythonParser.Custom_functionContext):
        child: Expression = self.visit(ctx.getChild(1))
        return CustomFunction(child)

    def visitMath_Operation_Simplified(self, ctx: PythonParser.Math_Operation_SimplifiedContext):
        left: Expression = self.visit(ctx.getChild(0))
        right: Expression = self.visit(ctx.getChild(3))
        operation: str = ctx.getChild(1).getText()
        return MathOperationSimplified(left, right, operation)

    def visitBuilt_function(self, ctx: PythonParser.Built_functionContext):
        child: Expression = self.visit(ctx.getChild(1))
        return BuiltFunction(child)

    def visitVar(self, ctx: PythonParser.VarContext):
        child: Expression = self.visit(ctx.getChild(1))
        return Var(child)

    def visitVar_decl(self, ctx: PythonParser.Var_declContext):
        child: Expression = self.visit(ctx.getChild(1))
        var_type: str = ctx.getChild(2).getText()
        return VariableDeclaration(child, var_type)

    def visitVar_assign(self, ctx: PythonParser.Var_assignContext):
        left: Expression = self.visit(ctx.getChild(0))
        right: Expression = self.visit(ctx.getChild(2))
        return VariableAssign(left, right)

    def visitPrint(self, ctx: PythonParser.PrintContext):
        child: Expression = self.visit(ctx.getChild(1))
        return Print(child)

    def visitSwitch_Case(self, ctx: PythonParser.Switch_CaseContext):
        condition: Expression = self.visit(ctx.getChild(0))
        return SwitchCase(condition)
