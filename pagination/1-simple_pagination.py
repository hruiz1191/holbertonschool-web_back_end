#!/usr/bin/env python3
""" File that contains functions for pagination with hypermedia metadata """

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing the start and end indexes for the page.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple of start and end index.
    """
    return (page_size * (page - 1), page * page_size)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """
        Loads and caches the dataset.

        Returns:
            List[List[str]]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline='') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """
        Returns a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List[str]]: The paginated rows of the dataset.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Returns a dictionary with hypermedia pagination metadata.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Any]: A dictionary containing pagination metadata.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if (page * page_size) < total_items else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
