"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:17
FilePath: win_package_search/components/result/__init__.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from .result import PackageResult
from .collection import ChocoResultCollection, WingetResultCollection


__all__ = [
    'ChocoResultCollection',
    'PackageResult',
    'WingetResultCollection'
]
