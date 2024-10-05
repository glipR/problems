There are many different ways that Alice can carve out a particular tree structure, as the two contrasting sample outputs show. However, we can find some pretty concrete rules the instructions must follow:

* Alice may only visit any particular node by tunneling up the tree *once*. So once she has tunneled up to that node, she needs to carve out the entire of the subtree rooted at this node before leaving this node back down the tree. (why?)
* For a similar reason, Alice may only go BACK when the entirety of the tree in front of her is carved out.

Using this fact, a recursive structure to the problem arises:

1. Start at the root
2. For each child of the root node:
    - Tunnel to that child
    - Follow the instructions that carve out this subtree, and end up back at the child node
    - Go backwards to the root node

Combining all of these instructions we're able to generate a list of instructions that carves out the entire tree. Use the following image for a clearer description.

![](./recursive_tunnel.png)

The main implementation pains are reading in the graph (since the edges could be going either way) and implementing the recursive instruction generation.

Both of these can be solved with a single run of Depth First Search (DFS). (Alice actually always carves out a DFS path)
