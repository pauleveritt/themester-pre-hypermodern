from themester.themabaster import copy_asset_files


def test_copy_asset_files():
    assert 9 == copy_asset_files(1, 2)
