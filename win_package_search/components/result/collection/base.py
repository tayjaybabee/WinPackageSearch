"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:15
FilePath: win_package_search/components/result/collection/base.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from abc import ABC, abstractmethod
from collections import UserList
from typing import List, Optional
from win_package_search.components.result import PackageResult
from win_package_search.components.result.collection.metaclasses import PackageCollectionMeta


class PackageCollection(ABC, UserList,metaclass=PackageCollectionMeta):
    """
    Abstract base class for a collection of packages found by a search.
    """
    ALLOWED_PACKAGE_MANAGERS = ['Chocolatey', 'Winget']

    def __init__(self, package_manager_name: str) -> None:
        self.__name     = None
        self.__packages = []
        self.__query    = None
        self.__SESSION_HISTORY = []
        super().__init__()

        self.package_manager_name = package_manager_name

    @property
    def SESSION_HISTORY(self):
        return self.__SESSION_HISTORY

    @property
    def package_count(self) -> int:
        """
        The number of packages found by the search.

        Returns:
            int:
                The number of packages found by the search.
        """
        return len(self)

    @property
    def package_manager_name(self) -> Optional[str]:
        """
        The name of the package manager used to find the packages.

        Returns:
            Optional[str]:
                The name of the package manager used to find the packages, or None if the package manager is
                unknown\not set.
        """
        return self.__name

    @package_manager_name.setter
    def package_manager_name(self, new: str) -> None:
        """
        Sets the name of the package manager used to find the packages.

        Parameter:
            new (str):
                The name of the package manager used to find the packages.

        Raises:
            TypeError:
                If the package manager name is not a string.

            ValueError:
                If the package manager name is not one of the allowed package managers.

            ValueError:
                If the package manager name is already set.
        """
        print(new)

        if self.__name is not None:
            raise ValueError("Package manager name is already set.")

        if not isinstance(new, str):
            raise TypeError("Package manager name must be a string.")

        for allowed in self.ALLOWED_PACKAGE_MANAGERS:
            print(allowed.lower(), new.lower())
            if new.lower() == allowed.lower():
                self.__name = allowed
                return

        raise ValueError(f"Invalid package manager name: {new}")

    @property
    def package_names(self) -> List[str]:
        """
        The names of the packages found by the search.
        """
        return [p.name for p in self]

    @property
    def packages(self) -> List[PackageResult]:
        """
        The list of packages found by the search.
        """
        return list(self)

    @property
    def query(self) -> Optional[str]:
        """
        The query used to find the packages.

        Returns:
            Optional[str]:
            The query used to find the packages, or None if the query is not set.
        """
        return self.__query

    @query.setter
    def query(self, new: str) -> None:
        if self.__query:
            raise ValueError("Query is already set.")

        if not isinstance(new, str):
            raise TypeError(f"Query must be a string, not {type(new)}!")

        self.__query = new

    @query.deleter
    def query(self) -> None:
        self.__query = None

    def append(self, package: PackageResult) -> None:
        """
        Append a package to the collection.

        Parameter:
            package (PackageResult):
                The package to append.

        Raises:
            TypeError:
                If the package is not of type PackageResult.
        """
        if not isinstance(package, PackageResult):
            raise TypeError('Package must be of type PackageResult')

        super().append(package)

    def reset(self, query: str) -> None:
        """
        Reset the collection.
        """
        print(self)
        self.__SESSION_HISTORY.append({self.query: self})
        del self.query
        self.clear()
        self.query = query

