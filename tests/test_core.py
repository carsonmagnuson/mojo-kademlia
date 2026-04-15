import pytest
from ipaddress import ip_address
from kadempy.core import distance, generate_id, Node

@pytest.mark.parametrize(
    "id1_int, id2_int, expected_distance",
    [
        (0, 0, 0), # Identical nodes
        (1, 1, 0), # Identical nodes (non-zero)
        (0b101, 0b011, 0b110), # 5 XOR 3 = 6
        (0b1111, 0b0000, 0b1111), # 15 XOR 0 = 15
        (2**256 - 1, 0, 2**256 - 1), # Maximum architectural bounds
    ]
)

def test_distance(id1_int, id2_int, expected_distance):
    """Test XOR distance metric."""

    assert distance(id1_int, id2_int) == expected_distance

def test_generate_id():
    """Test SHA-256 Node ID generation"""
    test_id = generate_id()

    assert type(test_id) == bytes
    assert len(test_id) == (256//8)
    assert 0 <= int.from_bytes(test_id, byteorder='big') < 2**256

def test_node_class():
    """Test Node object creation"""
    addr = ip_address('192.168.0.1')
    test_node = Node(addr, 8080)

    assert test_node
    assert test_node.address == addr
    assert 0 <= test_node.port <= 65535
    assert type(test_node.node_id) == bytes
    assert len(test_node.node_id) == (256//8)
    assert 0 <= int.from_bytes(test_node.node_id, byteorder='big') < 2**256




