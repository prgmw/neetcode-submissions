class Solution:
    def isValid(self, s: str) -> bool:
        aux = list(s)
        stack = []

        #mapeia a fechamento e abertura
        mapa = {
              ')' : '(',
              ']' : '[',
              '}' : '{'
            }

        for it in aux:
            if it in mapa:
                #Se it é um fechamento e o topo da pilha é a abertura
                if stack and stack[-1] == mapa[it]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(it)
         
        return len(stack) == 0

        