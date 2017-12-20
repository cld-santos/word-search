import os
from os import listdir
import re


class ItemLoader():

    def load_items(self, src_name, data):
        raise Exception('You must implement!')


class SourceLoader():

    def __init__(self, item_loader):
        self.item_loader = item_loader
        self.sources = {}

    def load(self):
        raise Exception('You must implement!')


class FileSystemLoader(SourceLoader):

    def __init__(self, item_loader, source_dir='data/', cache_dir='cache/'):
        super().__init__(item_loader)
        self.source_dir = source_dir
        self.cache_dir = cache_dir
        self.cached_words = []
        if not os.path.exists(self.cache_dir):
            os.mkdir(self.cache_dir)

    def load(self):
        for file in listdir(self.source_dir):
            self.sources[file] = []
            self.load_each_file(file)

    def load_each_file(self, file_name):
        with open(self.source_dir + file_name, "r", encoding='utf-8') as f:
            file_content = f.readlines()

        self.sources[file_name] = file_content[0].split(' ')
        self.item_loader.load_items(file_name, self.sources[file_name])

    def load_cached_words(self):
        if not os.path.exists(self.cache_dir + 'words.txt'):
            raise Exception('Não há indices de pesquisa disponíveis.\nEfetue o pre-processamento e tente novamente.')

        with open(self.cache_dir + 'words.txt', "r", encoding='utf-8') as f:
            for line in f:
                self.cached_words.append(line)

    def dump(self):
        files_keys = list(self.sources.keys())
        found_symbols = re.compile("[a-zA-Z0-9']+")
        with open(self.cache_dir + 'words.txt', "w", encoding='utf-8') as f:
            for k, v in self.item_loader.words.items():
                word = re.findall(found_symbols, k)
                if not word:
                    continue
                f.write(word[0] + '\n')

        with open(self.cache_dir + 'words_files.txt', "w", encoding='utf-8') as f:
            for k, v in self.item_loader.words.items():
                word = re.findall(found_symbols, k)
                if not word:
                    continue
                f.write(','.join([str(files_keys.index(item)) for item in v.sources]) + '\n')

        with open(self.cache_dir + 'files.txt', "w", encoding='utf-8') as f:
            for file_name in files_keys:
                f.write(file_name + '\n')


class Word():

    def __init__(self, text):
        self.text = text
        self.sources = []


class WordLoader(ItemLoader):

    def __init__(self):
        self.words = {}

    def load_items(self, src_name, raw_data):
        data = raw_data
        for word in data:
            if not word:
                continue
            try:
                if src_name not in self.words[word].sources:
                    self.words[word].sources.append(src_name)
            except:
                self.words[word] = Word(word)
                self.words[word].sources.append(src_name)

