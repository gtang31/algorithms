import pdb


class Solution(object):

    def __init__(self):
        pass

    def find_flights(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        """
        self.dst = dst
        self.paths = {}
        self.distance = []
        while flights:
            _src, _dst, cost = flights.pop()
            if _src not in self.paths:
                self.paths[_src] = [[_dst, cost]]
            else:
                self.paths[_src].append([_dst, cost])

        if src not in self.paths:
            return -1
        else:
            self._bfs(src, dst, K)
            # self._dfs(str(src), 0, self.paths[src])

        self.distance.sort(key=lambda x: [x[1], x[0]])
        for d in self.distance:
            if len(d[0].split('-'))-2 <= K:
                print(d)
                return d[1]
        return -1

    def _dfs(self, path, cost, sources):
        """
        DFS through a dictionary. Implementation via recursion; takes too long
        """
        for dest, c in sources:
            if str(dest) in path.split('-'):
                continue
            elif dest == self.dst:
                # base case
                self.distance.append([path+'-'+str(dest), cost+c])
            else:
                if dest in self.paths:
                    # make sure we don't get any keyerros
                    self._dfs(path+'-'+str(dest), cost+c, self.paths[dest])

    def _bfs(self, src, dst, K):
        """
        BFS. An iterative implementation offers easier way to keep track
        of local variables such as min_cost and K
        """
        min_cost = float('inf')
        q = [[str(src), src, 0]]
        while q:
            path, source, cost = q.pop(0)
            if source not in self.paths:
                continue
            for dest, cst in self.paths[source]:
                if (str(dest) in path.split('-')) or (len(path.split('-'))-2 > K) or (cost+cst > min_cost):
                    # keep track of current cost and stops traveled
                    # to save resources
                    continue
                elif dest == dst:
                    min_cost = min(min_cost, cost+cst)
                    self.distance.append([path+'-'+str(dest), cost+cst])
                else:
                    q.append([path+'-'+str(dest), dest, cost+cst])


# test cases
assert(Solution().find_flights(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1) == 200)
assert(Solution().find_flights(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0) == 500)
assert(Solution().find_flights(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1) == -1)
assert(Solution().find_flights(5, [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]], 0, 4, 1) == 5)
assert(Solution().find_flights(3, [[0,1,2],[1,2,1],[2,0,10]], 1, 2, 1) == 1)
assert(Solution().find_flights(10, [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]], 6, 0, 7) == 14)
assert(Solution().find_flights(15, [[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]], 1, 4, 10) == 169)
# print(Solution().find_flights(17, [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]], 13, 4, 13))
# print(Solution().find_flights(5, [[3,0,8],[1,4,1],[1,0,4],[1,3,3],[3,4,1],[2,3,3],[2,0,10]], 1, 4, 4))

