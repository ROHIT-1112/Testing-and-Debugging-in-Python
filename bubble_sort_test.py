
import unittest
import bubblesort as st

class  Test_TestValue(unittest.TestCase):
    def test_simple(self):
        testlist = [5,4,3,2,1]
        expectedList = testlist.copy()
        expectedList.sort()
        actualList = st.bubblesort(testlist)
        self.assertEqual(actualList,expectedList)

    def  test_empty(self):
        testList = []
        expectedList = testList.copy()
        expectedList.sort()
        actualList= st.bubblesort(testList)
        self.assertEqual(actualList , expectedList)