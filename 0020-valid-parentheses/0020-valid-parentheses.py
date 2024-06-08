class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            match c:
                case "(":
                    stack.append("(")
                case ")":
                    if stack:
                        prevBracket = stack.pop()
                        stack.append(prevBracket)

                        if(prevBracket != "("):
                            return False
                        else:
                            stack.pop()
                    else:
                        return False
                case "{":
                    stack.append("{")
                case "}":
                    if stack:
                        prevBracket = stack.pop()
                        stack.append(prevBracket)

                        if(prevBracket != "{"):
                            return False
                        else:
                            stack.pop()
                    else:
                        return False
                case "[":
                    stack.append("[")
                case "]":
                    if stack:
                        prevBracket = stack.pop()
                        stack.append(prevBracket)

                        if(prevBracket != "["):
                            return False
                        else:
                            stack.pop()
                    else:
                        return False

        return not stack