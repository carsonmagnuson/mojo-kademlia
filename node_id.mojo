from random import random_ui64, seed


struct NodeID:
  var id: UInt256

  fn __init__(out self):
    self.id = self.generate_id()

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

fn main():
  var node1 = NodeID()

  print(node1.id)


