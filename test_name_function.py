import unittest
from name_function import formatted_name


class TestFormattedName(unittest.TestCase):

    def test_first_last(self):
        """Test names without middle name."""
        self.assertEqual(formatted_name('john', 'doe'), 'John Doe')
        self.assertEqual(formatted_name('  alice  ', "o'connor"), "Alice O'Connor")

    def test_first_middle_last(self):
        """Test names with a middle name."""
        self.assertEqual(formatted_name('john', 'doe', 'paul'), 'John Paul Doe')
        self.assertEqual(formatted_name('  mary-jane  ', '  smith  ', 'ann-marie'), 'Mary-Jane Ann-Marie Smith')

    def test_empty_first_or_last_raises(self):
        """Providing empty first or last should raise ValueError."""
        with self.assertRaises(ValueError):
            formatted_name('', 'Doe')
        with self.assertRaises(ValueError):
            formatted_name('John', '')

    def test_none_middle_treated_as_empty(self):
        """If middle is None, treat it as no middle name."""
        self.assertEqual(formatted_name('jane', 'doe', None), 'Jane Doe')

    def test_whitespace_handling(self):
        """Leading/trailing and multiple inner spaces should be normalized."""
        self.assertEqual(formatted_name('  emma  ', '  watson  '), 'Emma Watson')

    def test_apostrophes_and_hyphens(self):
        """Names with apostrophes and hyphens should preserve punctuation and be capitalized."""
        self.assertEqual(formatted_name("o'neill", 'brady'), "O'Neill Brady")
        self.assertEqual(formatted_name('jean-luc', 'picard'), 'Jean-Luc Picard')

    def test_unicode_and_accents(self):
        """Names with accents should be handled (title() may not change accents)."""
        self.assertEqual(formatted_name('josé', 'niño'), 'José Niño')


if __name__ == '__main__':
    unittest.main()
