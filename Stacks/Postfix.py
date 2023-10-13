class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation=[]
        solution=0
        first=True
        pushed=False
        if len(tokens)==1:
            return int(tokens[0])
        for i in tokens:
            if i.lstrip("-").isdigit():
                operation.append(int(i))
                pushed=True
            else:
                if i=="+":
                    x=operation.pop()
                    y=operation.pop()
                    solution=x+y
                    operation.append(solution)
                    
                if i=="-" :
                    x=operation.pop()
                    y=operation.pop()
                    solution=y-x
                    operation.append(solution)
                if i=="*"  :
                    x=operation.pop()
                    y=operation.pop()
                    solution=x*y
                    operation.append(solution)
                if i=="/":
                    if first:
                        x=operation.pop()
                        y=operation.pop()
                        solution=int(y/x)
                        operation.append(solution)
                pushed=False
        return (solution)


# push the solution back in stack for homogenity