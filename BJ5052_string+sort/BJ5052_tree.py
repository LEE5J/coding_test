# 트리구조가 필요하다고 판단.



if __name__ == "__main__":
    import sys
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent
    sys.stdin = open(BASE_DIR / "input.txt", "r")
    input = sys.stdin.readline

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.child = {'end': False}

def append(tree: TreeNode,number):
    current_node = tree
    for num in list(number):
        if num in current_node.child:
            current_node = current_node.child[num]
            if current_node.child['end'] == True:
                return 1
        else:
            current_node.child[num]=TreeNode(num)
            current_node = current_node.child[num]
    current_node.child['end'] = True
    if len(list(current_node.child.keys())) != 1:
        return 1
    return 0

t = int(input())
for _ in range(t):
    n = int(input())
    root = TreeNode("")
    for i in range(n):
        if 0 == append(root, input().strip()):
            if i == n-1:
                print("YES")
            continue
        else:
            print("NO")
            if n-1 != i:
                for __ in range(n-i-1):
                    input()
            break
        