"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:16
FilePath: win_package_search/components/result/collection/__init__.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from .winget import WingetResultCollection
from .choco import ChocoResultCollection


__all__ = [
    'ChocoResultCollection',
    'WingetResultCollection'
]
