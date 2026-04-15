import pytest
from kadempy.core import distance

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

def test_node_id_xor_distance(id1_int, id2_int, expected_distance):
    """Test XOR distance metric."""

    assert distance(id1_int, id2_int) == expected_distance
