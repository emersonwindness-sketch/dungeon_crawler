class map:
    def __init__(self, name, description, access, has_container, container_name):
        self.name = name
        self.description = description
        self.access = access
        self.has_container = has_container
        self.container_name = container_name

class npc:
    def __init__(self, name, dialog):
        self.name = name
        self.dialog = dialog

