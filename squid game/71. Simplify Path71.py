class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []
        path  = path.split("/")
        # print(path)
        for i in range(len(path)):
            if stack and path[i] == "..":
                stack.pop()
            elif path[i] not in [".", "", ".."]:
                stack.append(path[i])
        ans = "/" + "/".join(stack)
        return ans