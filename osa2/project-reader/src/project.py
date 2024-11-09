class Project:
    def __init__(self,
                 name,
                 description,
                 project_license,
                 authors,
                 dependencies,
                 dev_dependencies
        ):
        self.name = name
        self.license = project_license
        self.authors = authors
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _list_list(self, data: list):
        return "\n".join(list(map(lambda s: f"- {s}", data)))

    def __str__(self):
        return (
            f"""Name: {self.name}
Description: {self.description}
License: {self.license}

Authors:
{self._list_list(self.authors)}

Dependencies:
{self._list_list(self.dependencies)}

Development dependencies:
{self._list_list(self.dev_dependencies)}""")
