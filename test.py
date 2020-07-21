import unittest
from spotget import spot_get_tracklist

class TestSpotGet(unittest.TestCase):
    def test_length(self):
        """
        Test that the length of the tracklist is correct.
        """
        data = "6WaIQHxEHtZL0RZ62AuY0g"
        result = spot_get_tracklist(data)
        self.assertEqual(len(result), 26)
        
    def test_item(self):
        """
        Test that a song on the tracklist is correct.
        """
        data = "2WT1pbYjLJciAR26yMebkH"
        result = spot_get_tracklist(data)
        self.assertEqual(result[3], "Time - 2011 Remastered Version")
        
    def test_invalid_id(self):
        """
        Test that an invalid id raises an error.
        """
        data = "2WT1pbYjLJciAR26yMebk"
        result = spot_get_tracklist(data)
        self.assertEqual(result, "No album found with that id")
    
if __name__ == "__main__":
    unittest.main()