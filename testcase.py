import unittest
from unittest.mock import patch, MagicMock
import pygame
import random

class TestGameFunctions(unittest.TestCase):
   pass

class TestGame(unittest.TestCase):
   @patch('pygame.image.load')
   @patch('pygame.transform.scale')
   def test_load_and_resize_image(self):
        image_path = "space1.jpg"
        size = (50, 50)
        mock_image = MagicMock()
        mock_image.get_size.return_value = size
        with patch('pygame.image.load', return_value=mock_image):
            resized_image = load_and_resize_image(image_path, size)
        self.assertEqual(resized_image.get_size(), size)

   @patch('pygame.Surface.blit')
   def test_draw_image(self, mock_blit):
       mock_surface = MagicMock()
       mock_image = MagicMock()

       from catchthemouse import draw_image # replace 'your_module' with the actual module name
       draw_image(mock_surface, mock_image, 10, 20)

       mock_blit.assert_called_once_with(mock_image, (10, 20))
    
   def test_check_collision(self):
        with self.assertRaises(SystemExit):
            # Test when there is a collision
            self.assertTrue(check_collision(0, 0, 0, 0, 50, 50, 50, 50))

            # Test when there is no collision
        self.assertFalse(check_collision(0, 0, 0, 0, 60, 60, 70, 70))

if __name__ == '__main__':
   unittest.main()
