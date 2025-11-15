# Test Results

This file captures the verbose output of running the project's unit tests.

(Recorded run from this workspace)
```
test_apostrophes_and_hyphens (test_name_function.TestFormattedName.test_apostrophes_and_hyphens)
Names with apostrophes and hyphens should preserve punctuation and be capitalized. ... ok
test_empty_first_or_last_raises (test_name_function.TestFormattedName.test_empty_first_or_last_raises)
Providing empty first or last should raise ValueError. ... ok
test_first_last (test_name_function.TestFormattedName.test_first_last)
Test names without middle name. ... ok
test_first_middle_last (test_name_function.TestFormattedName.test_first_middle_last)
Test names with a middle name. ... ok
test_none_middle_treated_as_empty (test_name_function.TestFormattedName.test_none_middle_treated_as_empty)        
If middle is None, treat it as no middle name. ... ok
test_unicode_and_accents (test_name_function.TestFormattedName.test_unicode_and_accents)
Names with accents should be handled (title() may not change accents). ... ok
test_whitespace_handling (test_name_function.TestFormattedName.test_whitespace_handling)
Leading/trailing and multiple inner spaces should be normalized. ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```
