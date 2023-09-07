
from dataclasses import dataclass
from typing import Optional


@dataclass
class StaticWebsite():
    build_directory: str
    s3_bucket_name: Optional[str] = None
    azure_blob_name: Optional[str] = None

    def __post_init__(self):
        if not isinstance(self.build_directory, str):
            raise TypeError('build_directory should be of type str')
        if not isinstance(self.s3_bucket_name, str) and not isinstance(self.azure_blob_name, str):
            raise AttributeError("Either s3_bucket_name or azure_blob_name need to be set for a static website deployment")
        # if not isinstance(self.s3_bucket_name, str):
        #     raise TypeError('s3_bucket_name should be of type str')
