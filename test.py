import unittest
from tkinter import TclError
from worldlistgui import worldlist_generator  

class TestWorldlistGenerator(unittest.TestCase):
    def test_worldlist_generator(self):
        try:
            worldlist_generator()
        except TclError:
            self.fail("worldlist_generator() raised TclError unexpectedly!")

if __name__ == '__main__':
    unittest.main()