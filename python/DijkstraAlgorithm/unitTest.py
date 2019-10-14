import unittest
from main import Graph   
g =  [
            [0, 4, 0, 0, 0, 0, 0, 8, 0], 
            [4, 0, 8, 0, 0, 0, 0, 11, 0], 
            [0, 8, 0, 7, 0, 4, 0, 0, 2], 
            [0, 0, 7, 0, 9, 14, 0, 0, 0], 
            [0, 0, 0, 9, 0, 10, 0, 0, 0], 
            [0, 0, 4, 14, 10, 0, 2, 0, 0], 
            [0, 0, 0, 0, 0, 2, 0, 1, 6], 
            [8, 11, 0, 0, 0, 0, 1, 0, 7], 
            [0, 0, 2, 0, 0, 0, 6, 7, 0] 
    ]

class TestDijkstra(unittest.TestCase):

 

    def test_success(self):
         
        gr = Graph(9,0,4,g)
        self.assertEqual(gr.retShortestPath(), 21)

    def test_failed(self):

        gr = Graph(9,0,4,g)
        self.assertEqual(gr.retShortestPath(), 20)


if __name__ == '__main__':
    unittest.main()

