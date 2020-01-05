from typing import Dict
import toml
from . import DependencyLoader


class PoetryDependencyLoader(DependencyLoader):

    def get_dependencies(self) -> Dict[str, str]:
        deps = toml.load(self.dep_handle)
        return {}
