class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(course, cycle):
            if course in visited:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for adj_course in graph[course]:
                if not dfs(adj_course, cycle):
                    return False
            visited.add(course)
            cycle.remove(course)

            return True

        visited = set()

        for course in range(numCourses):
            if not dfs(course, set()):
                return False
            # visited.add(course)

        return True

        