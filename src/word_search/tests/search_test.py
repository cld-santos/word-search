import unittest
from word_search.loader import FileSystemLoader, WordLoader
from word_search.searcher import WordSearch
from word_search.tests.util import CACHE_DIR, SOURCE_DIR


class SearchTest(unittest.TestCase):

    def setUp(self):
        self.word_loader = WordLoader()
        self.word_search = WordSearch(
            FileSystemLoader(
                self.word_loader,
                source_dir=SOURCE_DIR,
                cache_dir=CACHE_DIR),
            self.word_loader)
        self.word_search.pre_process()
        self.word_search.dump()
        self.word_search.load_cache()

    def test_must_not_found_useless_word(self):
        occurrences = self.word_search.search('lula')
        self.assertTrue(occurrences == '')

    def test_must_found_simple_word(self):
        occurrences = self.word_search.search('media')
        self.assertIn('meu-arquivo-um.txt', occurrences)

    def test_must_found_simbolized_word(self):
        occurrences = self.word_search.search("you're me")
        self.assertIn('meu-arquivo-tres.txt', occurrences)

    def test_must_occurrences_with_different_cases(self):
        occurrences = self.word_search.search('ThEy')
        self.assertIn('meu-arquivo-dois.txt', occurrences)

    def test_must_found_more_than_one_word(self):
        occurrences = self.word_search.search('they antoni')
        self.assertIn('meu-arquivo-tres.txt', occurrences)

    def test_must_occurrences_near_punctuation(self):
        occurrences = self.word_search.search('always')
        self.assertIn('meu-arquivo-dois.txt', occurrences)
        self.assertIn('meu-arquivo-um.txt', occurrences)
