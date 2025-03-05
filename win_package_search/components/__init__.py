"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:15
FilePath: win_package_search/components/__init__.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from .result import PackageResult
from .log_engine import ROOT_LOGGER


MOD_LOGGER = ROOT_LOGGER.get_child('components')


__all__ = [
    'PackageResult'
]
