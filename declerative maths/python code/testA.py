import unittest 
from programA import stack_frame_lines

class TestStackFrame(unittest.TestCase):

  def test_stack_frame(self):
    result = stack_frame_lines(5,10)
    
    self.assertIn("bp+2 : a = 5", result)
    self.assertIn("bp+4 : b = 10" result)
    self.assertIn("AX+BX = 15", result)

if __name__ == "__main__":
  unittest.main()
