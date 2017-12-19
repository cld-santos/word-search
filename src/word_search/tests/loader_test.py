import shutil
import unittest
from word_search.loader import (
    FileSystemLoader,
    WordLoader, 
    ItemLoader,
    SourceLoader)


class LoaderTest(unittest.TestCase):

    def test_implement_load(self):
        word_loader = WordLoader()
        source_loader = SourceLoader(word_loader)
        must_raise_exception = False
        try:
            source_loader.load()
        except:
            must_raise_exception = True
        self.assertTrue(must_raise_exception)

    def test_implement_load_items(self):
        item_loader = ItemLoader()
        must_raise_exception = False
        try:
            item_loader.load_items('', '')
        except:
            must_raise_exception = True
        self.assertTrue(must_raise_exception)

    def test_must_pre_process_files(self):
        shutil.rmtree('word_search/tests/cache/')
        word_loader = WordLoader()
        file_sys_loader = FileSystemLoader(
            word_loader,
            source_dir='word_search/tests/data/',
            cache_dir='word_search/tests/cache/')
        file_sys_loader.load()
        file_sys_loader.dump()
        file_sys_loader.load_cached_words()
        self.assertIsNotNone(file_sys_loader.sources)
        self.assertIsNotNone(file_sys_loader.item_loader.words)
        self.assertIn('they', file_sys_loader.item_loader.words.keys())
        self.assertTrue(len(file_sys_loader.item_loader.words['they'].sources) == 2)
        self.assertIn('meu-arquivo-dois.txt', list(file_sys_loader.sources.keys()))
