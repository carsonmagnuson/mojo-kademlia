def distance(id1: bytes, id2: bytes) -> int:
    """
    XOR distance function
    """
    return id1^id2

from hashlib import sha256
def generate_id() -> bytes: 
    """
    SHA_256 NodeID generation function
    """
    return sha256().digest()

from dataclasses import dataclass
from ipaddress import ip_address
@dataclass
class Node:
    """
    Network participant Dataclass
    """
    address: ip_address
    port: int
    node_id: bytes = generate_id()

