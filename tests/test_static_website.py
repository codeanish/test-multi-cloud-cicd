
import pytest
from apps.static_website import StaticWebsite


def test_static_website_aws():
    website = StaticWebsite(
        build_directory=".next", 
        s3_bucket_name="codeanish-test-blah"
        )
    assert website.build_directory == ".next"
    assert website.s3_bucket_name == "codeanish-test-blah"
    assert website.azure_blob_name == None

def test_static_website_azure():
    website = StaticWebsite(
        build_directory=".next", 
        azure_blob_name="codeanish-test-blah"
        )
    assert website.build_directory == ".next"
    assert website.azure_blob_name == "codeanish-test-blah"
    assert website.s3_bucket_name == None

def test_static_website_invalid_config_no_deploy_location():
    with pytest.raises(Exception):
        StaticWebsite(
            build_directory=".next"
            )