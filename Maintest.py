from Main import Main
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    main = Main()


    def testCompareIfTheyAreEquivalent(self):
        self.assertEqual(self.main.isAcceptedNFA("aaaab"), self.main.isAcceptedNFAEliminated("aaaab"))
        self.assertEqual(self.main.isAcceptedNFA("bba"), self.main.isAcceptedNFAEliminated("bba"))
        self.assertEqual(self.main.isAcceptedNFA("c"), self.main.isAcceptedNFAEliminated("c"))
        self.assertEqual(self.main.isAcceptedNFA("aca"), self.main.isAcceptedNFAEliminated("aca"))


if __name__ == '__main__':
    unittest.main()