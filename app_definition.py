from dataclasses import dataclass
from typing import List, Optional
import yaml

from apps.static_website import StaticWebsite
# from typing import List
# from apps.static_website import StaticWebsite

# class AppDefinition():
#     name: str
#     static_websites: List[StaticWebsite]

@dataclass
class Apps():
    StaticWebsite: Optional[StaticWebsite] = None

@dataclass
class AppDefinition():
    name: str
    apps: List[Apps]


def create_app_definition_from_yaml(yaml_file_path: str):
    with open(yaml_file_path) as f:
        my_data = yaml.safe_load(f)
        app_def = AppDefinition(**my_data)
        return app_def

if __name__ == "__main__":
    app_def = create_app_definition_from_yaml("tests/test_app_definition.yaml")
    print(app_def.name)
    print(app_def.apps[0].build_directory)
    print(app_def.apps[0].s3_bucket_name)