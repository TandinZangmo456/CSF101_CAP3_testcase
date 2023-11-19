# Test Case Documentation This document provides an overview of the test cases implemented in the TestGameFunctions and TestGame classes of the project.
 ## TestGameFunctions Class This class is responsible for testing the functions of the main game module.
 ### 'test_load_and_resize_image' #### Resources used - Modules 'unittest' and 'unittest.mock'  for implementing test cases.
 – "Pygame" library for game development.
 #### Reason This test case checks the functionality of the load_and_resize_image function and ensures that images are loaded and resized correctly.
 ### 'test_draw_image' #### Resources used - Modules 'unittest' and 'unittest.mock'  for implementing test cases.
 – “Pygame” library for game development.
 #### Reason Validate the ``draw_image'' function to ensure that it correctly calls the ``blit'' method of the ``Surface'' object with the specified image and coordinates.
 ### 'test_check_collision' #### Resources used - 'unittest' module for test case implementation.
 #### Reason Tests the check_collision function to ensure that  collisions between two rectangles are detected correctly.
 ## TestGame Class This class is responsible for testing the main game module.
 ### General Information - Testing uses the "unittest" module to implement test cases.
 – Mocking is used to isolate  functions and methods under test.
 ### Running the Test To run the test, run the following command: ''bash python testcase.py 
