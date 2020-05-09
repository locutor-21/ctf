#!/usr/bin/python3
import sys
import socket
import time

class Vertex:
    def __init__(self, node):
        self.id = node
        self.time = 0
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Mark all nodes unvisited
        self.visited = False
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def add_time(self, time):
        self.time = time

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_time(self):
        return self.time

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def dijkstra(aGraph, start, target):
    '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            cur_dist = current.get_distance()
            interm_dist = cur_dist + current.get_weight(next)
            new_dist = interm_dist + ((next.get_time() - interm_dist) % next.get_time())
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


def solve(lines):
    # Parse input
    number_doors = int(lines[0].split()[0])
    number_paths = int(lines[0].split()[1])
    door_times = lines[1].split()
    paths = lines[2:-3]
    ini = int(lines[-3].split()[0])
    end = int(lines[-3].split()[1])

    # Build graph
    g = Graph()

    for vertex in range(number_doors):
        v = g.add_vertex(str(vertex+1))
        v.add_time(door_times[vertex])

    for path in paths:
        (u, v, weight) = path.split()
        g.add_edge(str(u), str(v), weight)


    # Find shortest path
    dijkstra(g, g.get_vertex(str(ini)), g.get_vertex(str(end)))

    target = g.get_vertex(str(end))
    path = [target.get_id()]
    shortest(target, path)


if __name__ == '__main__':
    # SETUP
    host = "142.93.113.55"
    port = 31085

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    sock.send('start'.encode())
    time.sleep(0.5)

    # START SOLVING PROBLEMS
    first = True
    while True:
        res = sock.recv(8192).decode().strip()
        print(res)

        pos = res.find("Challenge")
        lines = res[pos:].split('\n')
        if first:
            lines = lines[2:]
        else:
            lines = lines[1:]

        solution = solve(lines)

        sock.send(str(solution).encode())
        time.sleep(1.5)
        first = False

    print("Connection closed.")
    sock.close()
