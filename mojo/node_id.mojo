from random import random_ui64, seed


struct NodeID(ImplicitlyCopyable):
  var id: UInt256

  comptime __copyinit__is_trivial = True

  fn __init__(out self):
    self.id = NodeID.generate_id()

  fn __copyinit__(out self, existing: Self):
    self.id = existing.id

  @staticmethod
  fn generate_id() -> UInt256:
      seed()
      var max_val: UInt64 = 9223372036854775807
      var part1 = random_ui64(0, max_val)
      var part2 = random_ui64(0, max_val)
      var part3 = random_ui64(0, max_val)
      var part4 = random_ui64(0, max_val)
      
      var result: UInt256 = (UInt256(part1) << 192) | (UInt256(part2) << 128) | (UInt256(part3) << 64) | UInt256(part4)
      return result

  @staticmethod
  fn distance(id1: UInt256, id2: UInt256) -> UInt256:
    var dist = id1 ^ id2
    return dist

fn main():
  var node1 = NodeID()
  var node2 = NodeID()
  print(node1.id)
  var distance = NodeID.distance(node1.id, node2.id)
  print(distance)


