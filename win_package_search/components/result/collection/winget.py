"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:15
FilePath: win_package_search/components/result/collection/winget.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from .base import PackageCollection


class WingetResultCollection(PackageCollection):
    """
    A collection of Winget packages found by a search.
    """

    def __init__(self, query: str) -> None:
        super().__init__('winget')
        if query is not None:
            self.query = query
