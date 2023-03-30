"""
This type stub file was generated by pyright.
"""

_GDAL_VERSION = ...
supported_drivers = ...
driver_mode_mingdal = ...
def vector_driver_extensions(): # -> dict[Unknown, Unknown]:
    """
    Returns
    -------
    dict:
        Map of extensions to the driver.
    """
    ...

def driver_from_extension(path):
    """
    Attempt to auto-detect driver based on the extension.

    Parameters
    ----------
    path: str or pathlike object
        The path to the dataset to write with.

    Returns
    -------
    str:
        The name of the driver for the extension.
    """
    ...

_driver_converts_to_str = ...
_driver_field_type_unsupported = ...
_drivers_not_supporting_timezones = ...
_drivers_not_supporting_milliseconds = ...
