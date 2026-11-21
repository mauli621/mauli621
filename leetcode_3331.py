
class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        tree = [[] for _ in range(n)]

        for i in range(1, n):
            tree[parent[i]].append(i)

        ans = [1] * n
        stack = [[] for _ in range(26)]

        st = [(0, -1, 0)]

        while st:
            node, par, state = st.pop()
            idx = ord(s[node]) - ord('a')

            if state == 0:
                stack[idx].append(node)

                st.append((node, par, 1))

                for child in tree[node]:
                    st.append((child, node, 0))

            else:
                if len(stack[idx]) > 1:
                    new_parent = stack[idx][-2]
                else:
                    new_parent = par

                if new_parent != -1:
                    ans[new_parent] += ans[node]

                stack[idx].pop()

        return ans
