graph = {
  '1' : ['2','4'],
  '2' : ['3', '5'],
  '3' : ['6'],
  '4' : ['3', '7'],
  '5' : ['6', '8'],
  '6' : [],
  '7' : ['6', '8'],
  '8' : []
}


def dfs(graph, node):
    visited = []
    stack = []

    visited.append(node)
    stack.append(node) 

    while stack:
        s = stack.pop()
        print(s, end = " ")

        # reverse iterate through edge list so results match recursive version
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)


def main():
    dfs(graph, '1')


main()