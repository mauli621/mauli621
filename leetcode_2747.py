
class Solution(object):
    def countServers(self, n, logs, x, queries):

        logs.sort(key=lambda a: a[1])

        q = []

        for i in range(len(queries)):
            q.append([queries[i], i])

        q.sort()

        count = {}
        result = [0] * len(queries)

        left = 0
        right = 0

        for i in range(len(q)):

            start = q[i][0] - x
            end = q[i][0]

            # Add logs inside the ending time
            while right < len(logs) and logs[right][1] <= end:

                server = logs[right][0]

                if server in count:
                    count[server] += 1
                else:
                    count[server] = 1

                right += 1

            # Remove logs outside the starting time
            while left < right and logs[left][1] < start:

                server = logs[left][0]

                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            result[q[i][1]] = n - len(count)

        return result
