class PrefixtoPostFix:
    def isOperator(self, x):
        return x in {'-', '+', '/', '*', '^'}

    def convert(self, expression):
        stack = []
        for i in range(len(expression)-1, -1, -1):
            c = expression[i]
            if self.isOperator(c):
                s1 = stack.pop()
                s2 = stack.pop()
                temp = s1 + s2 + c
                stack.append(temp)
            else:
                stack.append(c)
        result = stack.pop()
        return result


if __name__ == "__main__":
    prefix = "*/93+*24-76"
    print("Prefix Expression:", prefix)
    print("Postfix Expression:", PrefixtoPostFix().convert(prefix))
