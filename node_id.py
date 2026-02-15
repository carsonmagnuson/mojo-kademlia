import hashlib

class NodeID:
    def generate_id(self, seed):
        m = hashlib.sha256()
        m.update(seed.encode())
        return m.digest()

    def __init__(self, seed):
        self.id = self.generate_id(seed)

new = NodeID("random")
print(new.id)
