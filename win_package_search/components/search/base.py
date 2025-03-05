"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:17
FilePath: win_package_search/components/search/base.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from abc import ABC, abstractmethod
from typing import List
from ...components.result import PackageResult
from ...components.log_engine import Loggable


class PackageSearch(ABC, Loggable):
    """
    Abstract base class for a package searcher.
    """
    def __init__(self, parent_logger, package_manager_name: str):
        self.__name = None
        self.__session_history = []
        self.__result_collection = None
        super(PackageSearch, self).__init__(parent_logger)

        self.package_manager_name = package_manager_name

    @property
    @abstractmethod
    def RESULT_COLLECTION_CLASS(self):
        pass

    @property
    def package_manager_name(self) -> str:
        """
        The name of the package manager used to find the packages.

        Returns:
            str:
                The name of the package manager used to find the packages.
        """
        return self.__name

    @package_manager_name.setter
    def package_manager_name(self, new: str):
        """
        Sets the name of the package manager used to find the packages.
        """
        if self.__name is not None:
            raise ValueError("Package manager name is already set.")

        if not isinstance(new, str):
            raise TypeError("Package manager name must be a string.")

        self.__name = new

    @property
    def result_collection(self) -> 'PackageCollection':
        """
        The collection of packages found by the search.
        """
        if self.__result_collection is None and self.package_manager_name is not None:
            self.__result_collection = self.RESULT_COLLECTION_CLASS(self.package_manager_name)
        return self.__result_collection

    @result_collection.setter
    def result_collection(self, new: 'PackageCollection'):
        """
        Sets the collection of packages found by the search.
        """
        if self.__result_collection is not None:
            raise ValueError("Result collection is already set.")

        if not isinstance(new, self.RESULT_COLLECTION_CLASS):
            raise TypeError("Result collection must be a PackageCollection.")

        self.__result_collection = new

    @abstractmethod
    def search(self, query: str) -> List[PackageResult]:
        pass
