"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:16
FilePath: win_package_search/components/search/__init__.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from ...components import MOD_LOGGER as PARENT_LOGGER

MOD_LOGGER = PARENT_LOGGER.get_child('search')

from .base import PackageSearch
from .choco import ChocoSearch
from .winget import WingetSearch




__all__ = [
    'ChocoSearch',
    'PackageSearch',
    'WingetSearch'
]
