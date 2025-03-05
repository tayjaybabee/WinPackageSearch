"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:16
FilePath: win_package_search/components/search/searcher.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from . import ChocoSearch, WingetSearch
from ..result.collection import ChocoResultCollection, WingetResultCollection

class PackageSearcher:
    CHOCO  = ChocoSearch()
    WINGET = WingetSearch()

    def __init__(self):
        self.__package_managers = None

    @property
    def package_managers(self):
        if self.__package_managers is None:
            self.__package_managers = [
                self.CHOCO,
                self.WINGET
            ]

        return self.__package_managers

    def search(self):
        pass

    def search_choco(self, query: str) -> ChocoResultCollection:
        return self.CHOCO.search(query)

    def search_winget(self, query: str) -> WingetResultCollection:
        return self.WINGET.search(query)
