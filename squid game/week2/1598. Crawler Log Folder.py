class Solution:
    def minOperations(self, logs: List[str]) -> int:

        stack = []
        for i in range(len(logs)):
            if stack and logs[i] == "../":
                stack.pop()
            elif logs[i] !=  "./" and logs[i] != "../":
                stack.append(logs[i])
        # print(stack)
        return len(stack)