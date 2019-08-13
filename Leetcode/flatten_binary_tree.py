def flatten(tree):
    if not tree:
        return []
    return flatten(tree[1])+[tree[0]]+flatten(tree[2])
tree = [5,[2,[1,[],[]],[]],[7,[6,[],[]],[10,[],[]]]]
print(flatten(tree))