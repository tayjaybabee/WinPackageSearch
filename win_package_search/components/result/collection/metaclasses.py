"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:17
FilePath: win_package_search/components/result/collection/metaclasses.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from abc import ABCMeta
from typing import Dict


class PackageCollectionMeta(ABCMeta):
    _instances: Dict[str, 'PackageCollection'] = {}

    def __call__(cls, *args, **kwargs):

        instance = super().__call__(*args, **kwargs)
        manager_name = getattr(instance, 'package_manager_name', None)
        query = getattr(instance, 'query', None)

        if manager_name:
            normalized_name = cls._normalize_name(manager_name)
            if normalized_name in cls._instances:
                existing = cls._instances[normalized_name]

                if hasattr(existing, 'query') and existing.query != query:
                    if hasattr(existing, 'reset'):
                        existing.reset(query)

                return existing

            cls._instances[normalized_name] = instance

        return instance

    @staticmethod
    def _normalize_name(name: str) -> str:
        """
        Normalize the package manager name.

        Parameters:
            name (str):
                The name of the package manager.

        Returns:
            str:
                The normalized name of the package manager; lowercased and stripped.
        """
        return name.lower().strip()
