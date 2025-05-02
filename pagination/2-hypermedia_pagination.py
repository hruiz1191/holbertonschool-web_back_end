#!/usr/bin/env python3
""" File that contains functions for pagination """
import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """ Function that returns the index and size of a page """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """ Server class to paginate a database of popular baby names. """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Displays the correct amount of items per page """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Returns page info including hypermedia metadata """
        data = self.dataset()
        total_pages = len(data) // page_size + (1 if len(data) % page_size != 0 else 0)

        return {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
