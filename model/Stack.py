class Stack:
    def __int__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


#   匹配  表达式的括号
word = "(3+2)*3-(88+1)"


def bracketsBalance(word):
    stk = Stack()
    for ch in word:
        if ch in ['[', '(', '{']:
            stk.push(ch)
            #左符号的情况 下  入栈
        elif ch in [']', ')', '}']:
            # 栈里没有对应的左符号   退出
            if stk.isEmpty():
                return False
            #检测弹出最近的一个左符号 与现在的右符号是否匹配
            chFromStack = stk.pop()

            if ch == ']' and chFromStack !='[' or ch == ')' and chFromStack !='(' or ch == '}' and chFromStack != '{' :
                return False
    return stk.isEmpty()

#后缀表达式
def stack1(str):
    stack = Stack()
    result = []
    for i in str:
        if i not in ['*','/','-','+']:
            stack.push(i)
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            num = 0
            if i == '*':
                num = num1 * num2
            elif i == '/':
                num = num1 / num2
            elif i == '+':
                num = num1 + num2
            else:

                num = num1 - num2
            stack.push(num)

#       中序 转后续

def middle2behind(expression):
    #   后缀表达式
    result = []
    #   栈
    stack = []
    #   从左到右
    for item in expression:
        #   是数字的情况直接入栈
        if item.isnumeric():
            result.append(item)
        else:
            #   不是数字 且栈为空的情况
            if len(stack) == 0:
                stack.append(item)
            #   是 乘除的情况
            elif item in '*/(':
                stack.append(item)
            #  遇到右括号    弹出到左括号为止
            elif item == ')':
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            #      是加减的情况     同时站里面有运算级更有先的情况
            elif item in '+-' and stack[len(stack)-1] in '*/':
                #      没有左括号   全部弹出
                if stack.count('(') == 0:
                    while stack:
                        result.append(stack.pop())
                #       有左括号，弹出到左括号位置
                else:
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    #  pop掉的（ 加回去
                    stack.append('(')
                #  弹出操作完后入栈 +-
                stack.append(item)
            else:
                stack.append(item)
        # 栈里还有东西要清空
    while stack:
        result.append(stack.pop())
    return "".join(result)

expression = "3+(6*7-2)+2*3"
print(middle2behind(expression))

