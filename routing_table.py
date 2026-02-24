import kbucket, node_id

class RoutingTable:

    def __init__(self):
        self.buckets = [kbucket]*256
        self.node = node_id.NodeID("seed")

    def add(self, to_add):
        distance = node_id.NodeID.distance(self.node.id, to_add.id)
        return




