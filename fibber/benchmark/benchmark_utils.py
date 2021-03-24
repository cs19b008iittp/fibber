import os

import pandas as pd

from fibber import get_root_dir


def update_detailed_result(aggregated_result, result_dir=None):
    """Read dataset detailed results and add a row to the file. Create a new file if the table
    does not exist.

    Args:
        aggregated_result (dict): the aggregated result as a dict.
        result_dir (str or None): the directory to save results. If None, use
            ``<fibber_root_dir>/results/``.
    """
    if result_dir is None:
        result_dir = os.path.join(get_root_dir(), "results")
    os.makedirs(result_dir, exist_ok=True)
    result_filename = os.path.join(result_dir, "detail.csv")
    if os.path.exists(result_filename):
        results = pd.read_csv(result_filename)
    else:
        results = pd.DataFrame()

    results = results.append(aggregated_result, ignore_index=True)
    results.to_csv(result_filename, index=False)


def update_attack_robust_result(aggregated_result, robust_tuned_clf_desc,
                                robust_tuning_steps, result_dir=None):
    """Read results of attacking robust classifiers, and add a row to the file.
    Create a new file if the table does not exist.

    Args:
        aggregated_result (dict): the aggregated result as a dict.
        robust_tuned_clf_desc (str): the robust tuning description.
        robust_tuning_steps (int): the number of robust tuning steps.
        result_dir (str or None): the directory to save results. If None, use
            ``<fibber_root_dir>/results/``.
    """
    if result_dir is None:
        result_dir = os.path.join(get_root_dir(), "results")
    os.makedirs(result_dir, exist_ok=True)
    result_filename = os.path.join(result_dir, "robust_detail.csv")
    if os.path.exists(result_filename):
        results = pd.read_csv(result_filename)
    else:
        results = pd.DataFrame()

    aggregated_result["robust_tuned_clf_desc"] = robust_tuned_clf_desc
    aggregated_result["robust_tuning_steps"] = robust_tuning_steps
    results = results.append(aggregated_result, ignore_index=True)
    results.to_csv(result_filename, index=False)


def load_detailed_result():
    """Read detailed results from file.

    Returns:
        (pandas.DataFrame): the detailed result table. Returns an empty DataFrame if file does not
        exist.
    """
    result_dir = os.path.join(get_root_dir(), "results")
    result_filename = os.path.join(result_dir, "detail.csv")
    if os.path.exists(result_filename):
        return pd.read_csv(result_filename)
    else:
        return pd.DataFrame()


def update_overview_result(overview_result):
    """write overview result to file.

    Args:
        overview_result (pandas.DataFrame): the overview result.
    """
    result_dir = os.path.join(get_root_dir(), "results")
    os.makedirs(result_dir, exist_ok=True)
    result_filename = os.path.join(result_dir, "overview.csv")
    overview_result.to_csv(result_filename, index=None)
