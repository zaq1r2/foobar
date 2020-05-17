# used as referance http://python.algorithmexamples.com/web/graphs/edmonds_karp_multiple_source_and_sink.html

def solution(entrances, exits, path):
    source = entrances[0]
    sink = exits[0]
    if len(entrances) > 1 or len(exits) > 1:
        path = normalize(entrances, exits, path)
        source = 0
        sink = len(path) - 1
    max_flow = push_relabel(path, source, sink)
    return max_flow


def normalize(sources, sinks, graph):
    newInputWeight = 0
    for source in sources:
        newInputWeight += sum(graph[source])

    size = len(graph) + 1 

    for row in graph:
        row.insert(0,0)

    graph.insert(0, [0] * size)

    for source in sources:
        graph[0][source + 1] = newInputWeight
    
    size = len(graph) + 1
    for room in graph:
        room.append(0)
    graph.append([0] * size)
    for sink in sinks:
        graph[sink + 1][size - 1] = newInputWeight
    return graph
    


def push_relabel(graph, source, sink): 

    def push(from_index, to_index):
        preflow_delta = min(excesses[from_index], graph[from_index][to_index] - preflow[from_index][to_index])
        preflow[from_index][to_index] += preflow_delta
        preflow[to_index][from_index] -= preflow_delta
        excesses[from_index] -= preflow_delta
        excesses[to_index] += preflow_delta

    def relabel(vertex_index):
        min_height = None
        for to_index in range(vertex_count):
            if (
               graph[vertex_index][to_index] -preflow[vertex_index][to_index]
                > 0
            ):
                if min_height is None or heights[to_index] < min_height:
                    min_height = heights[to_index]
 
        if min_height is not None:
           heights[vertex_index] = min_height + 1

    def process_vertex(vertex_index):
        while excesses[vertex_index] > 0:
            for neighbour_index in range(vertex_count):
                if graph[vertex_index][neighbour_index] - preflow[vertex_index][neighbour_index] > 0 and heights[vertex_index] > heights[neighbour_index]:
                    push(vertex_index, neighbour_index)
 
            relabel(vertex_index)

    vertex_count = len(graph)
    preflow = [[0] * vertex_count for _ in range(vertex_count)]
    heights = [0] * vertex_count
    excesses = [0] * vertex_count
    heights[source] = vertex_count

    for next_vertex_index, flow_cap in enumerate(graph[source]):
        preflow[source][next_vertex_index] += flow_cap
        preflow[next_vertex_index][source] -= flow_cap
        excesses[next_vertex_index] += flow_cap

    vertices_list = [i for i in range(vertex_count) if i != source and i != sink]

    i = 0
    while i < len(vertices_list):
        vertexIndex = vertices_list[i]
        previousHeight = heights[vertexIndex]
        process_vertex(vertexIndex)
        if heights[vertexIndex] > previousHeight:
                # if it was relabeled, swap elements
                # and start from 0 index
            vertices_list.insert(0, vertices_list.pop(i))
            i = 0
        else:
            i += 1
 
    return sum(preflow[source])

 
    
                

print(solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))