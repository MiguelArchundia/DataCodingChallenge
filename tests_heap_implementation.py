import unittest
from unittest.mock import patch
from io import StringIO
import os
import tempfile
import heap_implementation 


class Test_heap_implementation(unittest.TestCase):

    @patch('builtins.input', side_effect=['/nonexistent/path.txt'])
    def test_process_file(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = heap_implementation.process_file()
            self.assertTrue("Error: The file + /nonexistent/path.txt does not exist." in mock_stdout.getvalue())
            self.assertEqual(result, "/Users/marchundia/DataCodingChallenge/output.txt")

    @patch('builtins.input', side_effect=['not_an_integer', '5'])
    def test_getUserInput(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = heap_implementation.getUserInput()
            self.assertTrue("That's not a valid integer. Please try again." in mock_stdout.getvalue())
            self.assertEqual(result, 5)

    def test_read_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(b'1 2 3 4 5 6')
            temp_file_name = temp_file.name
        result = heap_implementation.read_file(temp_file_name)
        os.unlink(temp_file_name)  # clean up
        self.assertEqual(result, [(1, 2), (3, 4), (5, 6)])

    def test_heapify_2d(self):
        arr = [(1, 2), (3, 4), (5, 6)]
        result = heap_implementation.heapify_2d(arr)
        self.assertEqual(result, [(-6, (5, 6)), (-4, (3, 4)), (-2, (1, 2))])

    def test_heappush(self):
        heap = [(-6, (5, 6)), (-4, (3, 4)), (-2, (1, 2))]
        heap_implementation.heappush(heap, (7, 8))
        # Check that the highest-priority item is at the root of the heap
        self.assertEqual(heap[0], (-8, (7, 8)))
        # Optionally, you can check the length of the heap to ensure the item was added
        self.assertEqual(len(heap), 4)

    def test_heappop(self):
        heap = [(-8, (7, 8)), (-4, (3, 4)), (-2, (1, 2)), (-6, (5, 6))]
        result = heap_implementation.heappop(heap)
        self.assertEqual(result, (7, 8))


if __name__ == '__main__':
    unittest.main()
