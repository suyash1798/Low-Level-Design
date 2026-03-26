from __future__ import annotations

class Node:
    key: str
    value: str
    prev: Node
    next: Node

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None