class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course : [] for course in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        visited = set()
        res = []

        def dfs(course, cycle):
            if course in visited:
                return True
            
            if course in cycle:
                return False

            cycle.add(course)

            for adj_course in graph[course]:
                if not dfs(adj_course, cycle):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for course in graph.keys():
            if course not in visited and not dfs(course, set()):
                return []

        return res if len(res) == numCourses else []
