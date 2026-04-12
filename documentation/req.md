# Functions
### `ping(ipaddress address, integer port) -> boolean`:
Used to verify that a node is alive/responding.

---
### `store(string key, value) -> boolean`:
Used to store a (key, value) pair in a node. How is this (where the pair is to be stored) decided??
Return True on successful storage, false if error.

---
### `lookup(integer id, boolean value=False) -> KBucket or Value`:
Used to pull a `KBucket` of `Nodes` or a specific value from the network.

---
### `distance(NodeID id1, NodeID id2) -> String`:
Used to derive the `XOR` distance between two `Nodes`. 

---
### `bootstrap(ipadress address, integer port) -> Array`:
Used to stand up a new `Node`.


<br/>

# Objects

### `Router`:
The routing object for all the network `Nodes` that any home `Node` is holding on to, organized in `KBuckets`. This should probably be a static class. You will only have the one instance of it per any one `Node`.

>contains `KBuckets`
---
### `KBucket`:
The distance category object that groups `Nodes` in the `Router`. 

---
### `Node` 
The node object that holds a `NodeID` and the corresponding address. 
>contains `NodeID`

---
### `NodeID`:
The 256 bit identifier for a particular `Node`.
>contains `distance()`



