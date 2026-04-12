# Functions
### `ping(ipaddress address, integer port) -> boolean`:
Used to verify that a node is alive/responding.

### `store(string key, value) -> boolean`:
Used to store a (key, value) pair in a node. How is this (where the pair is to be stored) decided??
Return True on successful storage, false if error.

### `lookup(integer id, boolean value=False) -> KBucket or Value`:
Used to pull a `KBucket` of `Nodes` or a specific value from the network.

### `distance(NodeID id1, NodeID id2) -> String`:
Used to derive the `XOR` distance between two `Nodes`. 

### `bootstrap(ipadress address, integer port) -> Array`:
Used to stand up a new `Node`.

# Objects
`RoutingTable` contains `KBucket`

`Node` contains `NodeID`


