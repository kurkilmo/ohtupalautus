from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        deserialized = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono
        # ja muodosta Project-olio sen tietojen perusteella
        deps_list = deserialized["tool"]["poetry"]["dependencies"].keys()
        dev_deps_list = deserialized["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()

        return Project(
            deserialized["tool"]["poetry"]["name"],
            deserialized["tool"]["poetry"]["description"],
            deserialized["tool"]["poetry"]["license"],
            deserialized["tool"]["poetry"]["authors"],
            deps_list,
            dev_deps_list)
