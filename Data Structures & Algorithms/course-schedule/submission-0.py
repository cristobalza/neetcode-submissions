class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(course, visited):
            if course in visited:
                return False

            visited.add(course)
            for adj_course in graph[course]:
                if not dfs(adj_course, visited):
                    return False

            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True

        