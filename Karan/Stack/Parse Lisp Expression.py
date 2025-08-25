class Solution:
    def evaluate(self, expression: str) -> int:
        def helper(tokens, env):
            if tokens[0] != '(':
                if tokens.isdigit() or (tokens[0] == '-' and tokens[1:].isdigit()):
                    return int(tokens)
                for e in reversed(env):
                    if tokens in e:
                        return e[tokens]
            tokens = tokens[1:-1]
            parts = []
            i = 0
            while i < len(tokens):
                if tokens[i] == '(':
                    start = i
                    count = 1
                    i += 1
                    while i < len(tokens) and count:
                        if tokens[i] == '(':
                            count += 1
                        elif tokens[i] == ')':
                            count -= 1
                        i += 1
                    parts.append(tokens[start:i])
                else:
                    start = i
                    while i < len(tokens) and tokens[i] != ' ':
                        i += 1
                    parts.append(tokens[start:i])
                while i < len(tokens) and tokens[i] == ' ':
                    i += 1
            if parts[0] == 'add':
                return helper(parts[1], env) + helper(parts[2], env)
            elif parts[0] == 'mult':
                return helper(parts[1], env) * helper(parts[2], env)
            elif parts[0] == 'let':
                new_env = env + [{}]
                i = 1
                while i < len(parts) - 1:
                    new_env[-1][parts[i]] = helper(parts[i+1], new_env)
                    i += 2
                return helper(parts[-1], new_env)
        return helper(expression, [])