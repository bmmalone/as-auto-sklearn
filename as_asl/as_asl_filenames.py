###
#   This module contains functions to construct filenames for the as_asl
#   library.
###

import os


def _get_compression_str(compression_type=None):
    compression_str = ""
    if (compression_type is not None) and  (len(compression_type) > 0):
        compression_str = ".{}".format(compression_type)
    return compression_str

def _get_fold_str(fold=None):
    fold_str = ""
    if (fold is not None) and (len(str(fold)) > 0):
        fold_str = ".fold-{}".format(fold)
    return fold_str

def _get_note_str(note=None):
    note_str = ""
    if (note is not None) and  (len(note) > 0):
        note_str = ".{}".format(note)
    return note_str

def _get_scenario_str(scenario=None):
    scenario_str = ""
    if (scenario is not None) and  (len(scenario) > 0):
        scenario_str = ".{}".format(scenario)
    return scenario_str

###
# F
###
def get_feature_selector_filename(base_path, selector_type,
        compression_type="gz", scenario=None, note=None):
    """ Get the path to a file containing a fit feature selector

    Parameters
    ----------
    base_path: path-like (e.g., a string)
        The path to the base data directory

    selector_type: string
        The identifier for the type of selector (e.g., "rf-ensemble")

    compression_type: string or None
        The extension for the type of compression. Please see the joblib docs
        for more details about supported compression types and extensions.

        Use None for no compression.

    scenario: string or None
        The name of the scenario for which the selector was learned

    note: string or None
        Any additional note to include in the filename. This should probably
        not contain spaces or special characters.

    Returns
    -------
    selector_filename: string
        The path to the selector file
    """
    
    fname = [
        "feature-selector.",
        selector_type,
        _get_scenario_str(scenario),
        _get_note_str(note),
        ".pkl",
        _get_compression_str(compression_type)
    ]

    fname = ''.join(fname)
    fname = os.path.join(base_path, fname)
    return fname



###
# M
###
def get_model_filename(base_path, model_type, fold=None,
        compression_type="gz", scenario=None, note=None):
    """ Get the path to a file containing a fit model

    Parameters
    ----------
    base_path: path-like (e.g., a string)
        The path to the base data directory

    model_type: string
        The identifier for the type of model (e.g., "bo-baseline")

    fold: int-like or None
        The cross-validation fold

    compression_type: string or None
        The extension for the type of compression. Please see the joblib docs
        for more details about supported compression types and extensions.

        Use None for no compression.

    scenario: string or None
        The name of the scenario for which the selector was learned

    note: string or None
        Any additional note to include in the filename. This should probably
        not contain spaces or special characters.

    Returns
    -------
    model_filename: string
        The path to the model file
    """

    fname = [
        "model.",
        model_type,
        _get_fold_str(fold),
        _get_scenario_str(scenario),
        _get_note_str(note),
        ".pkl",
        _get_compression_str(compression_type)
    ]

    fname = ''.join(fname)
    fname = os.path.join(base_path, fname)
    return fname

def get_schedule_filename(base_path, scenario, note=None):
    """ Get the path to a file containing a schedule

    Parameters
    ----------
    base_path: path-like (e.g., a string)
        The path to the base data directory

    scenario: string
        The name of the scenario for which the schedule was selected

    note: string or None
        Any additional note to include in the filename. This should probably
        not contain spaces or special characters.

    Returns
    -------
    schedule_filename: string
        The path to the schedule file
    """
    
    fname = [
        "schedule",
        _get_scenario_str(scenario),
        _get_note_str(note),
        ".json"
    ]

    fname = ''.join(fname)
    fname = os.path.join(base_path, fname)
    return fname

