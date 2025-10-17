import unittest
import sys
sys.path.append("/home/codio/workspace/")
from boggle_solver import Boggle

def norm_lower(words):
    return sorted([w.lower() for w in words])

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):
    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"],["D", "E", "F"],["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        expected = ["abc", "abdhi", "cfi", "dea"]
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

    def test_4x4_grid(self):
        grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],
                ["G", "Z", "Qu", "R"], ["O", "N", "T", "A"]]
        dictionary = ["art","ego","gent","get","net","new","newt","prat","pry",
                      "qua","quart","quartz","rat","tar","tarp","ten","went",
                      "wet","arty","not","quar"]
        expected = ["art","ego","gent","get","net","new","newt","prat","pry",
                    "qua","quart","quartz","rat","tar","tarp","ten","went",
                    "wet","quar"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

    def test_7x7_grid(self):
        grid = [
          ["H","A","R","B","O","R","S"],
          ["T","R","A","V","E","L","S"],
          ["W","I","N","T","E","R","S"],
          ["S","N","O","W","F","A","L"],
          ["B","R","I","S","K","S","L"],
          ["C","O","L","D","S","E","A"],
          ["B","E","A","C","H","S","S"]
        ]
        dictionary = ["harbor","travels","winter","snowfall",
                      "brisk","cold","beach","seas"]
        expected = ["harbor","travels","winter","snowfall",
                    "brisk","cold","beach","seas"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

    def test_13x13_grid_no_words_found(self):
        grid = [["X","Y","X","Y","X","Y","X","Y","X","Y","X","Y","X"],
                ["Y","X","Y","X","Y","X","Y","X","Y","X","Y","X","Y"]]*6 + \
               [["X","Y","X","Y","X","Y","X","Y","X","Y","X","Y","X"]]
        dictionary = ["HELLO","WORLD","PYTHON","UNITTEST","OPENAI","CHATGPT"]
        mygame = Boggle(grid, dictionary)
        expected = []
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

class TestSuite_Simple_Edge_Cases(unittest.TestCase):
    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a","b","c"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower([]), norm_lower(mygame.getSolution()))

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello","there"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower([]), norm_lower(mygame.getSolution()))

    def test_EmptyDictionary(self):
        grid = [["A","B"],["C","D"]]
        dictionary = []
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower([]), norm_lower(mygame.getSolution()))

    def test_Word_That_Take_The_Entire_Grid(self):
        # These dictionary strings cannot be formed under the rules
        # (8-directional adjacency, no cell reuse, min length 3).
        grid = [["A","B","E","S","T"],
                ["S","T","N","S","T"],
                ["E","I","E","N","S"],
                ["T","T","M","O","U"],
                ["S","T","E","A","B"]]
        dictionary = [
            "abeststnste", "bststenieest", "eienststtmousteststeab",
            "estnststeba", "steieneststb", "sttemieostu", "ustoiemetst"
        ]
        expected = []  # none are constructible without reusing cells
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

class TestSuite_Complete_Coverage(unittest.TestCase):
    def test_NoWordsFromDictionary(self):
        grid = [["A","B","C"],["D","E","F"],["G","H","I"]]
        dictionary = ["xyz","mno"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower([]), norm_lower(mygame.getSolution()))

    def test_PartialWordsFromDictionary(self):
        grid = [["A","B","C"],["D","E","F"],["G","H","I"]]
        dictionary = ["abc","cfi","xyz","ghi"]
        expected = ["abc","cfi","ghi"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

    def test_AllWordsFromDictionary(self):
        grid = [["A","B","C"],["D","E","F"],["G","H","I"]]
        dictionary = ["abc","cfi","beh","def","ghi","adg","aei","ceg"]
        expected = ["abc","cfi","beh","def","ghi","adg","aei","ceg"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

class TestSuite_Qu_and_St(unittest.TestCase):
    def test_GridWithMultipleMultiLetterCellsValidWords(self):
        grid = [["St","A","R"],["Qu","E","T"],["F","G","H"]]
        dictionary = ["star","start","quest","quiet","rat","hat","set"]
        expected = ["star","start","quest","rat"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

    def test_GridWithMoreComplexWords(self):
        grid = [["St","A","R"],["Qu","E","T"],["F","G","H"]]
        dictionary = ["stqufgearth","startequfgh","star","start",
                      "quest","quiet","rat","hat","set"]
        expected = ["star","start","quest","rat",
                    "startequfgh","stqufgearth"]
        mygame = Boggle(grid, dictionary)
        self.assertEqual(norm_lower(expected), norm_lower(mygame.getSolution()))

if __name__ == '__main__':
    unittest.main()
