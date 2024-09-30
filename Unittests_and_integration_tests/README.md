# Unittest and Intergration Tests

## Learning Objectives
- The difference between unit and integration tests is that unit tests take results from a single unit, the function call and integration tests results from various parts.
- Mocking is a process used in unit testing when the unit is being tested has external dependencies.
- parametrizations use for testing functions/ features that have simple input, when testing for a variety of input.
- Fixtures ensure test runs in a clean and controlled environment, avoiding code duplications, includes setting up objects, databases, and files.

## Task
- Task 0: Create a class TestAccessNestedMap, inherits from unittest.TestCase
<ul>
<li>Use @parameterized.expand: to run the same test method multiple times with different sets of input parameters. Each tuple contains nested_map, path, expected.
The  assertEqual is used to check output from function and matches expected value.
</li>
<li></li>
</ul>

