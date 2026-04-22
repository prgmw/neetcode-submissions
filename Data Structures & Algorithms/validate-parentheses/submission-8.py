class Solution:
    def isValid(self, s: str) -> bool:
        aux = list(s)
        stack = []

        mapa = {
              ')' : '(',
              ']' : '[',
              '}' : '{'
            }

        for it in aux:
            if it in mapa:
                #Se it é um fechamento e o topo da pilha é uma abertura
                if stack and stack[-1] == mapa[it]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(it)
         
        return len(stack) == 0

        