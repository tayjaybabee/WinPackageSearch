"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:15
FilePath: win_package_search/components/result/collection/choco.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from .base import PackageCollection


class ChocoResultCollection(PackageCollection):
    def __init__(self, query: str = None) -> None:
        super().__init__('chocolatey')
        if query is not None:
            self.query = query

