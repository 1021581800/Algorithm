expression = "3+(6*7-2)+2*3"

def middle2behind(expresssion):
    result = []             # 结果列表
    stack = []              # 栈
    for item in expresssion:
        if item.isnumeric():      # 如果当前字符为数字那么直接放入结果列表
            result.append(item)
        else:                     # 如果当前字符为一切其他操作符
            if len(stack) == 0:   # 如果栈空，直接入栈
                stack.append(item)
            elif item in '*/(':   # 如果当前字符为*/（，直接入栈
                stack.append(item)
            elif item == ')':     # 如果右括号则全部弹出（碰到左括号停止）
                t = stack.pop()
                while t != '(':
                    result.append(t)
                    t = stack.pop()
            # 如果当前字符为加减且栈顶为乘除，则开始弹出
            elif item in '+-' and stack[len(stack)-1] in '*/':
                if stack.count('(') == 0:           # 如果有左括号，弹到左括号为止
                    while stack:
                        result.append(stack.pop())
                else:                               # 如果没有左括号，弹出所有
                    t = stack.pop()
                    while t != '(':
                        result.append(t)
                        t = stack.pop()
                    stack.append('(')
                stack.append(item)  # 弹出操作完成后将‘+-’入栈
            else:
                stack.append(item)# 其余情况直接入栈（如当前字符为+，栈顶为+-）

    # 表达式遍历完了，但是栈中还有操作符不满足弹出条件，把栈中的东西全部弹出
    while stack:
        result.append(stack.pop())
    # 返回字符串
    return "".join(result)


(middle2behind(expression))

def behind_evaluator(expresssion):
    operatora = '+-*/'
    stack = []
    for x in expression:
        if x not in operatora:
            stack.append(float(x))
            continue
        if len(stack)< 2:
            raise SyntaxError("缺少  数")
        a = stack.pop()
        b = stack.pop()

        if x =="+":
            c = b+a
        elif x =="-":
            c = b-a
        elif x =="*":
            c = b*a
        else :
            c = b//a
        stack.append(c)

    if len(stack) ==1:
        return stack.pop()