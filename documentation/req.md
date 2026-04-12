

## 1\. Functions (RPCs)

Functions that represent the network-level Remote Procedure Calls for node communication and data propagation.

### `ping`

Verifies the operational status and reachability of a remote node.

  * **Signature:** `ping(address: IPAddress, port: Integer) -> Boolean`
  * **Parameters:**
      * `address` *(IPAddress)*: IPv4/IPv6 address of the target node.
      * `port` *(Integer)*: Listening port of the target node.
      * **Returns:** *(Boolean)* `true` if the node acknowledges the ping within the timeout threshold; otherwise `false`.

### `store`

Store key-value pair in a designated node. 
  * **Signature:** `store(key: String, value: Any) -> Boolean`
  * **Parameters:**
      * `key` *(String)*: The plaintext identifier for the data payload.
      * `value` *(Any)*: The data payload to be serialized and stored.
  * **Returns:** *(Boolean)* `true` upon successful storage; `false` if the operation fails or is rejected.

### `find_node`

Queries the network to retrieve the $k$ closest nodes to a given 256-bit identifier.

  * **Signature:** `find_node(target_id: NodeID) -> Array<Node>`
  * **Parameters:**
      * `target_id` *(NodeID)*: The 256-bit identifier being searched for.
  * **Returns:** *(Array\<Node\>)* A collection of the closest known nodes.

### `find_value`

Tries to retrieve a specific value associated with a key. If the node does not have said value, acts like `find_node` to return the closest known nodes to continue searching.

  * **Signature:** `find_value(key: String) -> Value | Array<Node>`
  * **Parameters:**
      * `key` *(String)*: The key for the requested data.
  * **Returns:** Returns the deserialized `Value` if present. If not, returns an `Array<Node>` representing the next logical routing hops.

### `bootstrap`

Initializes a new node using an existing node in the network and populates an initial routing table.

  * **Signature:** `bootstrap(address: IPAddress, port: Integer) -> Array<Node>`
  * **Parameters:**
      * `address` *(IPAddress)*: The IP address of the known bootstrap node.
      * `port` *(Integer)*: The port of the bootstrap node.
  * **Returns:** *(Array\<Node\>)* The initial set of network nodes returned by the bootstrap peer to seed the local `Router`.

-----


## 2\. System Objects

Data Structures that maintain the local state of the Kademlia protocol.

### `Router`

The routing manager object for the local node, organizing `Node` contacts into a list of `KBucket` objects.
  * **Contains:** `Array<KBucket>`

### `KBucket`

A bounded distance category utilized by the `Router`. Aggregates a specific maximum number (typically $k=20$) of remote `Node` objects that share a similar XOR distance from the local node.

  * **Contains:** `Array<Node>`

### `Node`

The representation of a network participant that holds necessary metadata for P2P connection.

  * **Attributes:**
      * `id` *(NodeID)*: The immutable identifier of the peer.
      * `address` *(IPAddress)*: The network routing address.
      * `port` *(Integer)*: The active communication port.

### `NodeID`

The 256-bit identifier representing a specific `Node` in the network search space.

  * **Methods:**
      * `distance(target: NodeID) -> BigInt`: Calculates the absolute logical distance between this ID and a target ID using a bitwise XOR operation. 

