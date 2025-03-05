"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:17
FilePath: win_package_search/components/search/winget.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import subprocess
from typing import List

# Local imports
from . import PackageSearch
from ...components.result import PackageResult
from ...components.result.collection import WingetResultCollection
from . import MOD_LOGGER as PARENT_LOGGER


MOD_LOGGER = PARENT_LOGGER.get_child('winget')


class WingetSearch(PackageSearch):
    """
    A package searcher for the Winget package manager.

    This class provides a way to search for packages using the Winget package manager. It is a subclass of
    `PackageSearch` and implements the abstract methods required to perform a search.
    """
    CMD_STUB          = ['winget', 'search']
    CMD_OUTPUT_OPTION = ['--output', 'json']

    def __init__(self):
        super().__init__(MOD_LOGGER, 'winget')

    @property
    def RESULT_COLLECTION_CLASS(self):
        return WingetResultCollection

    def __assemble_command(self, query: str) -> List[str]:
        """
        Assemble the command to be executed.

        Parameters:
            query (str):
                The query to search for.
        """
        return self.CMD_STUB + [query]

    def search(self, query: str) -> WingetResultCollection:
        """
        Execute a search for packages using the Winget package manager.

        Parameters:
            query (str):
                The query to search for.
        """
        packages = WingetResultCollection(query)
        try:
            result = subprocess.run(
                self.__assemble_command(query),
                capture_output=True,
                text=True,
                check=True
            )
        except subprocess.CalledProcessError as e:
            print(f'[Error] Winget search failed: {e}')
            return packages

        lines = result.stdout.splitlines()
        header_line_index = next((i for i, line in enumerate(lines) if 'Name' in line and 'Id' in line), None)

        if header_line_index is None:
            print(f'[Error] Winget search output does not contain expected headers.')
            return packages

        headers = lines[header_line_index].split()
        name_index = headers.index('Name')
        id_index = headers.index('Id')
        version_index = headers.index('Version') if 'Version' in headers else None

        for line in lines[header_line_index + 2:]:
            if not line.strip():
                continue

            name = line[name_index:id_index].strip()
            pkg_id = line[id_index:version_index].strip() if version_index else line[id_index:].strip()
            version = line[version_index:].strip() if version_index else 'Unknown'
            packages.append(PackageResult(name, version, pkg_id, 'Winget'))

        return packages
