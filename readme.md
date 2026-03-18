# Mojo Kademlia

This is a mojo implementation of [Kademlia](https://en.wikipedia.org/wiki/Kademlia). 

## `Node`
This class represents all peers in the network, including the host computer.
- `create_id(seed)` - to generate a permanent 256-bit node identifier for the host-node upon bootstrap
- `distance_to(other_node)` - to compute XOR distance metric between two nodes
## `KBucket`
This class represents the buckets in which id's are stored, implementing lazy splitting when we exceed 20 nodes.
- `add_contact(node)` - insert a node in the front (should be in order of most recently seen)
- `remove_contact(node)` - remove an inactive node
- `is_full()` - check if the kbucket has reached capacity
- 
- 

## RoutingTable

# Storage

## KademliaProtocol

## IterativeLookup

## KademliaNode

## Installation

```bash
...
```

## Usage

todo...

## Acknowledgments


## License

[MIT License](LICENSE)
