import TokenType
import TokenizeState
from token import Token


class Tokenizer:

    def IsOp(self, chr):
        return (chr == '+') or (chr == '-') or (chr == '*') or \
               (chr == '/')

    def FindOpType(self, firstOperator):
        type = TokenType.UNKNOWN
        if firstOperator == '+':
            type = TokenType.ADD
        elif firstOperator == '-':
            type = TokenType.SUBTRACT
        elif firstOperator == '*':
            type = TokenType.MULTIPLY
        elif firstOperator == '/':
            type = TokenType.DIVIDE
        return type

    def IsParen(self, chr):
        return (chr == '(') or (chr == ')')

    def FindParenType(self, chr):
        type = TokenType.UNKNOWN
        if chr == '(':
            type = TokenType.LEFT_PAREN
        elif chr == ')':
            type = TokenType.RIGHT_PAREN
        return type

    # The passed expression is checked to get tokens in Tokenize
    def Tokenize(self, source):
        tokens = list()
        token = ''
        state = TokenizeState.DEFAULT

        index = 0

        while index < len(source):
            chr = source[index]
            if state == TokenizeState.DEFAULT:
                opType = self.FindOpType(chr)
                if self.IsOp(chr):
                    tokens.append(Token(str(chr), opType))
                elif self.IsParen(chr):
                    parenType = self.FindParenType(chr)
                    tokens.append(Token(str(chr), parenType))
                elif chr.isdigit():
                    token = token + chr
                    state = TokenizeState.NUMBER

            # Handles multi-digit numbers
            elif state == TokenizeState.NUMBER:
                if chr.isdigit():
                    token = token + chr
                else:
                    tokens.append(Token(token, TokenizeState.NUMBER))
                    token = ""
                    state = TokenizeState.DEFAULT
                    index -= 1

            index += 1

        return tokens

