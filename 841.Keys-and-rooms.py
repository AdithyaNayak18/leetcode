class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        vis=set()
        def dfs(room):
            vis.add(room)
            for i in rooms[room]:
                if i not in vis:
                    dfs(i)
        dfs(0)
        return len(vis)==len(rooms)
