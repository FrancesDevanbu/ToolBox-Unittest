import unittest

def clean(Numlist):
    for item in Numlist:
        if item < 0:
            Numlist.remove(item)
    return Numlist

def sort(Numlist):
    Numlist.sort()
    return Numlist

def clean_sort(Numlist):
    clean(Numlist)
    sort(Numlist)
    return Numlist


class TestCleanSort(unittest.TestCase):
    def test_clean(self):
        self.assertEqual(clean([1,2,-1,0]),[1,2,0])
    def test_sort(self):
        self.assertEqual(sort([1,4,2,-1]),[-1,1,2,4])
    def test_clean_sort(self):
        self.assertEqual(clean_sort([1,-1,4,0]),[0,1,4])
if __name__ == '__main__':
    unittest.main()
