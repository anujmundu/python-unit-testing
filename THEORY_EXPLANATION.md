# Theory Explanation: Unit Testing and unittest in Python

## What is unit testing?
Unit testing is the practice of testing the smallest testable parts of an application—units—independently to ensure they behave as expected. A unit is typically a single function, method, or class.

## Importance of unit testing
- Early bug detection: catches issues at the code level before integration.
- Documentation: tests document expected behavior of code.
- Refactoring safety: tests provide confidence when changing implementation.
- Design feedback: writing tests often leads to cleaner, more modular code.

## Python's `unittest` module structure
- Test modules: files (typically named `test_*.py`) that contain tests.
- TestCase classes: subclass `unittest.TestCase` and group related tests.
- Test methods: methods inside TestCase whose names start with `test_`.
- Test discovery: `python -m unittest discover` finds and runs tests.

## Test cases vs test methods
- Test case (in the `unittest` context) usually refers to a class derived from `unittest.TestCase` that groups multiple test methods.
- Test method is an individual method in that class that performs a single assertion scenario.

## Assert methods
`unittest.TestCase` provides many assert methods; common ones include:
- `assertEqual(a, b)`: check equality
- `assertTrue(x)`, `assertFalse(x)`: truthiness
- `assertRaises(exc, callable, *args)`: check exception
- `assertIn(a, b)`: membership
- `assertAlmostEqual(a, b)`: floating point comparisons

## Test-driven development (TDD) concepts
- Write a failing test that specifies a desired behavior.
- Implement the minimal code to make the test pass.
- Refactor the code while keeping tests green.

TDD encourages small, incremental development and results in a robust test suite covering intended behavior.
