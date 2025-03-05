"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:16
FilePath: win_package_search/components/log_engine.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from inspy_logger import InspyLogger, Loggable


ROOT_LOGGER = InspyLogger('WinPackageSearch', console_level='DEBUG', no_file_logging=True)


__all__ = [
    'Loggable',
    'ROOT_LOGGER'
]
