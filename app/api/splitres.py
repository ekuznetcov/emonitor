from io import StringIO
import re
import os
import argparse
from statistics import mean
from typing import Dict, List
import sys


def path_to_dict(path):
    """
    This function returns JSON tree of the files

    Args:
         path (str): path to the file or directory with files with the messtat-extension.

    Returns:
        d (dict): JSON tree of the files
    """

    if os.path.isdir(path):
        d = {'name': os.path.basename(path)}
        d['children'] = [path_to_dict(os.path.join(path, x)) for x in list(filter(
            lambda name: name.endswith('.messtat') or os.path.isdir(os.path.join(path, name)), os.listdir(path)))]
        d['path'] = path
        return d
    else:
        if path.endswith('.messtat'):
            d = {'name': os.path.basename(path)}
            d['path'] = path
            d['file'] = 'messtat'
            return d


def get_messtat_files(file_path):
    """
    Function calculates the min, max, average and sum of
    power consumption value and writes this data to a file.

    Args:
        file_path (str): path to the file or directory with files with the messtat-extension.
        result_dir (str): path to the directory in which will be written files.

    Returns:
        return_val (list): list with file_names
    """

    if os.path.isdir(file_path):
        return path_to_dict(file_path)

    elif file_path.endswith('.messtat'):
        result_dict = {"filename": file_path, "isopen": False,
                       "isactive": False}
        return_val.append(result_dict)
    else:
        print("File isn\'t exist!", file=sys.stderr)
        return_val = None

    return return_val


def messtat_parser(file_name):
    """
    This function parse messtat files and cut from them
    necessary information(info about power consumption in J).

    Args:
        file_name (str): path to the file or directory with files with the messtat-extension.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        energy_data (list): list of values which parsed from messtat file.
        cpu_data: double-demensional list of cpu cores values
    """

    energy_data = list()
    cpu_data = list()
    err = 0

    try:
        with open(file_name, 'r') as file:
            for line in file.read().split('\n'):
                if 'package' in line:
                    num = float(re.findall(
                        r'\d+[,.]\d+', line.split(' ')[1])[0].replace(",", "."))
                    energy_data.append(num)
                else:
                    cpu_data.append([float(digit.replace(',', '.'))
                                    for digit in line.split()])
    except PermissionError as ex:
        data = str(ex)
        err = -1
    except FileNotFoundError as ex:
        data = str(ex)
        err = -1
    cpu_data.pop()  # Because there is an empty line at the end of the file, it creates an empty list, breaks the zip function
    cpu_data = list(map(list, zip(*cpu_data)))
    return energy_data, cpu_data


def statistics(data: list) -> dict:
    """
    Function that count min, max, average and sum of elements in data list.

    Args:
        data (list): list of values which parsed from messtat file.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        results_dict (dict): dictionary which contain min, max, average and sum of data elements.
    """
    results_dict = dict()
    err = 0
    try:
        results_dict = {
            'Min': min(data),
            'Max': max(data),
            'Mean': sum(data)/len(data),
            'Sum': sum(data),
        }
    except TypeError as ex:
        results_dict = str(ex)
        err = -1
    except ValueError as ex:
        results_dict = {}
        err = 0

    return err, results_dict


def cpu_stat(datasets: list, name: str) -> list:
    """
    Function that count min, max, mean of CPU cores workload.
                        min, max, mean of busy CPU cores.

    Args:
        data (list): list of the list of values with parsed messtat cpu_data.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        results_dict (list): list wof the dicts which contain min, max, average and sum of data elements.
        busy_cores_stat (dict): dictionary which contain min, max, average of processor cores.
    """
    cores_workload = []
    number_busy_cores = []
    for data in datasets:
        cores_workload.append({
            'Min': min(data),
            'Max': max(data),
            'Mean': sum(data)/len(data),
        })
    transpose_datasets = list(map(list, zip(*datasets)))
    for data in transpose_datasets:
        amount = len(list(filter(lambda val: val > 5, data)))
        number_busy_cores.append(amount)
    busy_cores_stat = {
        'Name': name,
        'Min': min(number_busy_cores),
        'Max': max(number_busy_cores),
        'Mean': sum(number_busy_cores)/len(number_busy_cores),
        'Amount': len(transpose_datasets[0])
    }

    return cores_workload, busy_cores_stat


def splitres(file_path):
    """
    Function calculates the min, max, average and sum of
    power consumption value and writes this data to a file.

    Args:
        file_path (str): path to the file or directory with files with the messtat-extension.
        result_dir (str): path to the directory in which will be written files.

    Returns:
        return_val (list): list of result which will be written to a file.(need it for testing)
    """
    file_path = str(file_path)
    print(file_path)

    if os.path.isdir(file_path):
        return_val = {}
        for root, _pre_dir, files in os.walk(file_path):
            for file in files:
                if file.endswith('.messtat'):
                    path = os.path.join(root, file)
                    energy_data, cpu_data = messtat_parser(path)
                    result_dict = {"name": file, "energy_data": energy_data,
                                   "cpu_data": cpu_data}
                    return_val[file] = result_dict
    elif file_path.endswith('.messtat'):
        energy_data, cpu_data = messtat_parser(file_path)
        result_dict = {"name": os.path.basename(file_path), "energy_data": energy_data,
                       "energy_stat": statistics(energy_data), "cpu_data": cpu_data, "cpu_stat": cpu_stat(cpu_data, os.path.basename(file_path))}
        return_val = (result_dict)
    else:
        print("File isn\'t exist!", file=sys.stderr)
        return_val = None

    return return_val
