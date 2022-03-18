def compare_data_with_expected(expected, real):
    assert expected == real, "Expected '{}', but got '{}'".format(
        expected, real)
