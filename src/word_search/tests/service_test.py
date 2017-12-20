import os
import unittest
from word_search.services import SearchLayer
from word_search.tests.util import CACHE_DIR


class SearchLayerTest(unittest.TestCase):

    def test_pre_process(self):
        search_layer = SearchLayer()
        search_layer.pre_process()
        self.assertTrue(os.path.exists(CACHE_DIR))
        self.assertTrue(os.path.exists(CACHE_DIR + 'words.txt'))
        self.assertTrue(os.path.exists(CACHE_DIR + 'files.txt'))
        self.assertTrue(os.path.exists(CACHE_DIR + 'words_files.txt'))

    def test_search_words(self):
        search_layer = SearchLayer()
        occurrences, time_elapsed = search_layer.search("walt disney")
        self.assertTrue(len(occurrences)-1 == 53)

