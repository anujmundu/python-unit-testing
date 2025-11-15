# Python Unit Testing Assignment: name formatter

This small project implements a `formatted_name` function and comprehensive unit tests using Python's built-in `unittest` framework.

Files included

- `name_function.py` — contains `formatted_name(first, last, middle='')` which returns a neatly formatted full name. It strips whitespace, validates required fields, and capitalizes name parts using `title()` to handle hyphens and apostrophes.
- `test_name_function.py` — unit tests covering normal usage and edge cases.
- `main_demo.py` — interactive demo script you can run to try the function.
- `requirements.txt` — declares Python >= 3.8.

How to run

1. Create a virtual environment (optional but recommended):

```pwsh
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install requirements (none beyond Python itself):

```pwsh
pip install -r requirements.txt
```

3. Run tests:

```pwsh
python -m unittest discover -v
```

4. Try the demo:

```pwsh
python main_demo.py
```

Notes on behavior

- The function requires both first and last names; passing empty strings or None for these will raise `ValueError`.
- The middle name is optional; passing `None` or leaving it blank results in the same output as omitting it.
- The function uses `str.title()` which correctly capitalizes words and handles hyphens/apostrophes in common cases. For advanced locale-aware capitalization you might want to use external libraries.

Test results

All tests in `test_name_function.py` should pass. See the repository test run for confirmation.

Test run (example output from this workspace):

```
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Completion summary

- Files created: `name_function.py`, `test_name_function.py`, `main_demo.py`, `requirements.txt`, `README.md`.
- All unit tests pass locally using `python -m unittest discover -v`.

Next steps (optional):

- Add more locale-aware capitalization handling if you need special casing.
- Add CI (GitHub Actions) to run tests on push.

Troubleshooting and developer workflow

What to do when the test has failed

- Don't panic. A failed test is a precise signal about where expected behavior differs from actual behavior.
- Read the test failure output carefully — it shows which test method failed and the assert message or traceback.
- Reproduce the failure locally by running only the failing test. Example:

```pwsh
python -m unittest test_name_function.TestFormattedName.test_first_last -v
```

- Inspect the implementation and the test. Decide whether the test expectation is correct (test bug) or the implementation is wrong.

Passing a test

- When you run `python -m unittest -v` and see `OK`, your tests passed.
- For incremental development, run the single test you just wrote first. Example:

```pwsh
python -m unittest test_name_function.TestFormattedName.test_whitespace_handling -v
```

- Committing only when tests pass keeps the main branch green. Consider adding a pre-commit hook or CI that runs tests.

Failing a test

- Typical causes:
	- A regression introduced by a recent change.
	- Incorrect test assumptions.
	- Environment differences (Python version, locale).
- Steps to resolve a failing test:
	1. Run the failing test alone to reproduce and get a focused traceback.
	2. Add temporary prints or use a debugger to inspect variables (or write a small reproducible script).
	3. Fix the implementation or correct the test expectations.
	4. Re-run the whole test suite to ensure no other tests are affected.

Adding new tests

- Decide the behavior you want to guarantee. Tests should be small, deterministic, and fast.
- Add a new method to `TestFormattedName` whose name starts with `test_`.
- Keep tests isolated: don't rely on external resources or stateful globals.
- Example: to add a test for multi-word last names:

```python
def test_multi_word_last_name(self):
		self.assertEqual(formatted_name('anna', "van der", 'meer'), 'Anna Van Der Meer')
```

- After adding tests, run the new test first and then the full suite.

- If adding many tests, consider grouping related tests into separate TestCase classes and use `setUp()`/`tearDown()` for shared setup.

Best practices

- Keep tests fast and deterministic.
- Use descriptive test method names and short docstrings.
- Run the test suite often during development.
- Add tests for edge cases (empty inputs, None values, hyphens/apostrophes, unicode).

Author

Anuj Mundu

🎓 MCA, Maulana Azad National Institute of Technology (MANIT), Bhopal

📧 Email: anujmark.edwin.ame@gmail.com

[LinkedIn](https://www.linkedin.com/in/anuj-mundu) | [GitHub](https://github.com/anujmundu) | [LeetCode](https://leetcode.com/anujmundu)
