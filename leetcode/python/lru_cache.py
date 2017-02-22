class LRUCache(object):
    """
    Hash table + double linked list
    Time: O(1)
    """
    class LinkNode(object):
        def __init__(self, k, x):
            self.key = k
            self.val = x
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.val_hash = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            node = self.val_hash[key]
            if node.next is not None:
                if node.prev is None:
                    self.head = node.next
                    node.next.prev = None
                else:
                    node.next.prev = node.prev
                    node.prev.next = node.next
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
            return node.val
        except:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            self.get(key)
            self.val_hash[key].val = value
        except:
            node = self.LinkNode(key, value)
            self.val_hash[key] = node
            if self.head:
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                self.head = node
                self.tail = node
            if len(self.val_hash) > self.capacity:
                # remove head
                del self.val_hash[self.head.key]
                self.head = self.head.next
                self.head.prev = None


# if __name__ == '__main__':
#     c = LRUCache(2)
#     c.put(1, 1)
#     c.put(2, 2)
#     print c.get(1)
#     c.put(3, 3)
#     print c.get(2)
#     c.put(4, 4)
#     print c.get(1)
#     print c.get(3)
#     print c.get(4)
