from typing import TextIO, Optional


class DependencyLoader:
    def __init__(self, dep_file: str):
        self.dep_file: str = dep_file
        self.dep_handle: Optional[TextIO] = None

    def __enter__(self):
        with open(self.dep_file, "r") as d:
            self.dep_handle = d
            return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.dep_handle:
            try:
                self.dep_handle.close()
            except:
                pass
