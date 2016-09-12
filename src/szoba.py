import abc


class Something(abc.ABC):
    def __init__(self, parent, name, container):
        self.name = name
        self.parent = parent
        self.container = container
        self._assert_dscfl_path_is_valid()
        self.description = self._get_description()

    def _assert_dscfl_path_is_valid(self):
        assert "\\" or "/" in self.description
        assert "things" in self.description

    def _get_description(self):
        with open("") as descfl:
            return None


class Room(Something):
    def __init__(self, parent, name, coordinates):
        Something.__init__(self, parent, name, container=True)
        self.children = []
        self.coordinates = coordinates


class Item(Something):
    def __init__(self, parent, name, movable, container):
        Something.__init__(self, parent, name, container=container)
        self.children = []
        self.movable = movable


if __name__ == '__main__':
    pass
