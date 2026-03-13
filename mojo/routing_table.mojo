from node_id import NodeID

struct RoutingTable:
  # var buckets = InlineArray[InlineArray[NodeID, 20], 256] 
  # Maybe we implement this later...but for now I don't want to worry about stack overflows.

  var buckets: List[List[NodeID]]
  

  fn __init__(out self):
    self.buckets = List[List[NodeID]]()
    for _ in range(256):
      var bucket = List[NodeID]()
      bucket.reserve(20)
      self.buckets.append(bucket^)

fn main():
  var test = RoutingTable()
  print(test.buckets[0][0].id)

