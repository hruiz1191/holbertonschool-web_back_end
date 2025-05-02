#!/usr/bin/env python3
""" File that contains functions for pagination """

import csv
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end index for a pagination request.

    Args:
        page (int): Current page number (1-indexed).
        page_size (int): Number of items per page.

    Returns:
        Tuple[int, int]: Start and end indices for slicing.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


class Server:
    """ Server class to paginate a database of popular baby names. """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset.

        Returns:
            List[List]: Dataset rows without header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the data for a given page.

        Args:
            page (int): Current page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: Data for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()
        start, end = index_range(page, page_size)
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns pagination info with metadata.

        Args:
            page (int): Current page number.
            page_size (int): Items per page.

        Returns:
            Dict: A dictionary with pagination metadata.
        """
        data = self.dataset()
        page_data = self.get_page(page, page_size)
        total_items = len(data)
        total_pages = total_items // page_size + (1 if total_items % page_size else 0)

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
