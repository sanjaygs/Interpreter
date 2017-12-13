import TokenType
from Tokenizer import Tokenizer
from token import Token


class Calculator:

    def __init__(self):
        self.currentTokenPosition = 0
        self.tokens = list()

    def GetToken(self,offset):
        if self.currentTokenPosition + offset >= len(self.tokens):
            return Token("", TokenType.EOF)
        return self.tokens[self.currentTokenPosition+offset]

    def CurrentToken(self):
        return self.GetToken(0)

    def EatToken(self, offset):
        self.currentTokenPosition = self.currentTokenPosition + offset

    def MatchAndEat(self, type):
        token = self.CurrentToken()
        if not self.CurrentToken().type == type:
            print("Saw "+token.type + "but" +type + "expected")
            exit(0)
        self.EatToken(1)
        return token

    def Add(self):
        self.MatchAndEat(TokenType.ADD)
        return self.Term()

    def Subtract(self):
        self.MatchAndEat(TokenType.SUBTRACT)
        return self.Term()

    def Multiply(self):
        self.MatchAndEat(TokenType.MULTIPLY)
        return self.Factor()

    def Divide(self):
        self.MatchAndEat(TokenType.DIVIDE)
        return self.Factor()

    def Factor(self):
        result = 0
        if self.CurrentToken().type == TokenType.LEFT_PAREN:
            self.MatchAndEat(TokenType.LEFT_PAREN)
            result = self.ArithmeticExpression()
            self.MatchAndEat(TokenType.RIGHT_PAREN)
        elif self.CurrentToken().type == TokenType.NUMBER:
            result = int(self.CurrentToken().text)
            self.MatchAndEat(TokenType.NUMBER)
        return result

    # recursive descent parsing
    def Term(self):
        result = self.Factor()
        while (self.CurrentToken().type == TokenType.MULTIPLY) or (self.CurrentToken().type == TokenType.DIVIDE):
            if self.CurrentToken().type == TokenType.MULTIPLY:
                result *= self.Multiply()
            elif self.CurrentToken().type == TokenType.DIVIDE:
                result /= self.Divide()
        return result

    def ArithmeticExpression(self):
        result = self.Term()
        while (self.CurrentToken().type == TokenType.ADD) or (self.CurrentToken().type == TokenType.SUBTRACT):
            if self.CurrentToken().type == TokenType.ADD:
                result += self.Add()
            elif self.CurrentToken().type == TokenType.SUBTRACT:
                result -= self.Subtract()
        return result

    def PrettyPrint(self, tokens):
        numberCount = 0
        opCount = 0
        for token in tokens:
            if token.type == TokenType.NUMBER:
                print("Number...." + token.text)
                numberCount += 1
            else:
                print("Operator..." + token.type)
                opCount += 1
        print("You have got ",numberCount," different numbers and ",opCount," operators.")


def main():
    expression = input("Enter the expression: ")
    expression += " "
    calc = Calculator()
    toke = Tokenizer()
    print("Expression: " + expression)
    print("-----------")
    calc.tokens = toke.Tokenize(expression)
    calc.PrettyPrint(calc.tokens)
    print("-----------")
    print("Expression Result: ",calc.ArithmeticExpression())

if __name__ == "__main__":
    main()
