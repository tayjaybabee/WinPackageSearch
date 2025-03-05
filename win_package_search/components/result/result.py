"""
Author: Taylor B. tayjaybabee@gmail.com
Date: 2025-03-05 07:09:49
LastEditors: Taylor B. tayjaybabee@gmail.com
LastEditTime: 2025-03-05 07:10:17
FilePath: win_package_search/components/result/result.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
class PackageResult:
    def __init__(
            self,
            package_name: str,
            package_description: str,
            package_version: str,
            package_source: str
    ):
        """
        Constructor for PackageResult class.

        Parameters:
            package_name (str):
                The name of the package.

            package_description (str):
                The description of the package.

            package_version (str):
                The version of the package.

            package_source (str):
                The source of the package.
        """
        self.__description = None
        self.__name        = None
        self.__source      = None
        self.__version     = None

        self.name        = package_name
        self.description = package_description
        self.version     = package_version
        self.source      = package_source

    def __str__(self):
        return f"{self.name} {self.version} from {self.source}"

    @property
    def description(self) -> str:
        """
        Represents the description of the package.
        """
        return self.__description

    @description.setter
    def description(self, new: str):
        """
        Sets the description of the package. This can not be set after initialization. Internal use only.
        """
        if self.__description is not None:
            raise ValueError("Description can not be set after initialization.")

        if not isinstance(new, str):
            raise TypeError("Description must be a string.")

        self.__description = new

    @property
    def name(self) -> str:
        """
        Represents the name of the package.
        """
        return self.__name

    @name.setter
    def name(self, new: str):
        """
        Sets the name of the package. This can not be set after initialization. Internal use only.
        """
        if self.__name is not None:
            raise ValueError("Name can not be set after initialization.")

        if not isinstance(new, str):
            raise TypeError("Name must be a string.")

        self.__name = new

    @property
    def source(self) -> str:
        """
        Represents the source of the package.
        """
        return self.__source

    @source.setter
    def source(self, new: str):
        """
        Sets the source of the package. This can not be set after initialization. Internal use only.
        """
        if self.__source is not None:
            raise ValueError("Source can not be set after initialization.")

        if not isinstance(new, str):
            raise TypeError("Source must be a string.")

        self.__source = new

    @property
    def version(self) -> str:
        """
        Represents the version of the found package.
        """
        return self.__version

    @version.setter
    def version(self, new: str) -> None:
        """
        Represents the version of the found package. This can not be set after initialization. Internal use only.

        Returns:
            .None
        """
        if self.__version is not None:
            raise ValueError("Version can not be set after initialization.")

        if not isinstance(new, str):
            raise TypeError

        self.__version = new