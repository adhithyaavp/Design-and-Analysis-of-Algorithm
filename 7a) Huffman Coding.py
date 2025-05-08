import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_coding(s):
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1

    heap = [Node(char, fr) for char, fr in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = Node(None, a.freq + b.freq)
        merged.left = a
        merged.right = b
        heapq.heappush(heap, merged)

    def build_code(node, code=""):
        if node:
            if node.char is not None:
                codes[node.char] = code
            build_code(node.left, code + "0")
            build_code(node.right, code + "1")

    codes = {}
    build_code(heap[0])
    return codes

text = "huffman"
codes = huffman_coding(text)
print("Huffman Codes:", codes)
