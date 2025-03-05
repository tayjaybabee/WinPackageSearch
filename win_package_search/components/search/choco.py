"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:18
FilePath: win_package_search/components/search/choco.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import re
import subprocess
from typing import List
from ...components.search import PackageSearch
from ...components.result import PackageResult
from ...components.result.collection import ChocoResultCollection
from . import MOD_LOGGER as PARENT_LOGGER


MOD_LOGGER = PARENT_LOGGER.get_child('choco')


class ChocoSearch(PackageSearch):
    CMD_STUB = ['choco', 'search']
    CHOCO_LINE_REJECTS = ['Chocolatey', 'Search for']

    def __init__(self):
        super().__init__(MOD_LOGGER, 'Chocolatey')

    @property
    def RESULT_COLLECTION_CLASS(self):
        return ChocoResultCollection

    def search(self, query: str) -> ChocoResultCollection:
        try:
            result = subprocess.run(
                self.CMD_STUB + [query],
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f'[Error] Choco search failed: {e}')
            return []

        packages = self.RESULT_COLLECTION_CLASS(query)

        for line in result.stdout.splitlines():
            if not line.strip() or any(reject in line for reject in self.CHOCO_LINE_REJECTS):
                continue

            res = re.match(r"^(?P<name>\S+)\s+(?P<version>\S+)\s+-\s+(?P<desc>.*)$", line)

            if res:
                packages.append(PackageResult(res.group('name'), res.group('desc'), res.group('version'), 'Chocolatey'))

            else:
                parts = line.split()
                if len(parts) >= 2:
                    name = parts[0]
                    version = parts[1]
                    desc = ' '.join(parts[2:]).lstrip('-').strip() if len(parts) > 2 else ''

                    packages.append(PackageResult(name, desc, version, 'Chocolatey'))

        return packages
