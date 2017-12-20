import os
import shutil
import unittest
from word_search.loader import (
    FileSystemLoader,
    WordLoader, 
    ItemLoader,
    SourceLoader)
from word_search.tests.util import CACHE_DIR, SOURCE_DIR


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

    def test_must_fail_trying_load_cache_without_it(self):
        if os.path.exists(CACHE_DIR):
            shutil.rmtree(CACHE_DIR)

        word_loader = WordLoader()
        file_sys_loader = FileSystemLoader(
            word_loader,
            source_dir=SOURCE_DIR,
            cache_dir=CACHE_DIR)
        must_raise_exception = False
        try:
            file_sys_loader.load_cached_words()
        except:
            must_raise_exception = True

        self.assertTrue(must_raise_exception)

    def test_must_pre_process_files(self):
        if os.path.exists(CACHE_DIR):
            shutil.rmtree(CACHE_DIR)
        word_loader = WordLoader()
        file_sys_loader = FileSystemLoader(
            word_loader,
            source_dir=SOURCE_DIR,
            cache_dir=CACHE_DIR)
        file_sys_loader.load()
        file_sys_loader.dump()
        file_sys_loader.load_cached_words()
        self.assertIsNotNone(file_sys_loader.sources)
        self.assertIsNotNone(file_sys_loader.item_loader.words)
        self.assertIn('they', file_sys_loader.item_loader.words.keys())
        self.assertTrue(len(file_sys_loader.item_loader.words['they'].sources) == 2)
        self.assertIn('meu-arquivo-dois.txt', list(file_sys_loader.sources.keys()))
