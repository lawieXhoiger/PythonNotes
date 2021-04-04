# 下面所有的解析步骤可能需要花点时间弄明白，但是它们原理都是查找输入并试
# 着去匹配语法规则。第一个输入令牌是 NUM，因此替换首先会匹配那个部分。一旦匹
# 配成功，就会进入下一个令牌 +，以此类推。当已经确定不能匹配下一个令牌的时候，
# 右边的部分 (比如 { (*/) factor }* ) 就会被清理掉。在一个成功的解析中，整个右
# 边部分会完全展开来匹配输入令牌流。

# 有了前面的知识背景，下面我们举一个简单示例来展示如何构建一个递归下降表
# 达式求值程序：

import re
import collections
NUM = "(?P<NUM>\d+)"
PLUS = "(?P<PLUS>\+)"
MINUS = "(?P<MINUS>\-)"
TIMES = "(?P<TIMES>\*)"
DIVIDE = "(?P<DIVIDE>/)"
LPAREN = "(?P<LPAREN>\()"
RPAREN = "(?P<RPAREN>\))"
WS = "?<WS>\s+"

master_pat = re.compile('|'.join([NUM,PLUS,
                                  MINUS,TIMES,DIVIDE,LPAREN,RPAREN]))
# Tokenizer 分词器
Token = collections.namedtuple("Token",['type','value'])
def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match,None):
        tok = Token(m.lastgroup,m.group())
        if tok.type != 'WS':
            yield tok

#parser     语法分析器

class ExpressionEvaluator:
    '''
    Implementation of a recursive descent parser. Each method
implements a single grammar rule. Use the ._accept() method
to test and accept the current lookahead token. Use the ._expect()
method to exactly match and discard the next token on on the input
(or raise a SyntaxError if it doesn't match).
    '''
    def parse(self,text):
        self.tokens = generate_tokens(text)
        self.tok = None # Last symbol consumed
        self.nexttok = None #Next symbol tokenized
        self._advance() #load first lookahead token
        return self.expr()
    def _advance(self):
        'Advance one token ahead'
        self.tok,self.nexttok = self.nexttok,next(self.tokens,None)
    def _accept(self,toktype):
        'Test and consume the next token if it matches toktype'
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False
    def _except(self,toktype):
        'Consume next token if it matches toktype or raise SyntaxError'
        if not self._accept(toktype):
            raise SyntaxError('Expected'+toktype)

    # Grammar rules follow
    def expr(self):
        "exception ::= term {('+'|'-')term}*"
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            right = self.term()
            if op == 'PLUS':
                exprval +=right
            elif op == 'MINUS':
                exprval -=right
        return exprval
    def term(self):
        "term ::= factor { ('*'|'/') factor }*"
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            right = self.factor()
            if op == 'TIMES':
                termval *=right
            elif op == 'DIVIDE':
                termval /=right
        return termval
    def factor(self):
        "factor ::= NUM | ( expr )"
        if self._accept('NUM'):
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            exprval = self.expr()
            self._except('RPAREN')
            return exprval
        else:
            raise SyntaxError('Excepted NUMBER OR LPAREN')
def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2+3'))
    print(e.parse('2+3*4'))
    print(e.parse('2+(3+4)*5'))
if __name__ == '__main__':
    descent_parser()

# tips

# 文本解析是一个很大的主题，一般会占用学生学习编译课程时刚开始的三周时间。
# 如果你在找寻关于语法，解析算法等相关的背景知识的话，你应该去看一下编译器书
# 籍。很显然，关于这方面的内容太多，不可能在这里全部展开。
# 尽管如此，编写一个递归下降解析器的整体思路是比较简单的。开始的时候，你先
# 获得所有的语法规则，然后将其转换为一个函数或者方法。因此如果你的语法类似这
# 样：

# expr ::= term { ('+'|'-') term }*
# term ::= factor { ('*'|'/') factor }*
# factor ::= '(' expr ')'
# | NUM

# 你应该首先将它们转换成一组像下面这样的方法：
# class ExpressionEvaluator:
        # ...
        # def expr(self):
        # ...
        # def term(self):
        # ...
        # def factor(self):
# expr ::= factor { ('+'|'-'|'*'|'/') factor }*
# factor ::= '(' expression ')'
# | NUM

# 这个语法看上去没啥问题，但是它却不能察觉到标准四则运算中的运算符优先级。
# 比如，表达式 "3 + 4 * 5" 会得到 35 而不是期望的 23. 分开使用” expr”和” term”

# 规则可以让它正确的工作。
# 对于复杂的语法，你最好是选择某个解析工具比如 PyParsing 或者是 PLY。下面
# 是使用 PLY 来重写表达式求值程序的代码：

