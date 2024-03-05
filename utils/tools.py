
import configparser
import os

def read_ini_config(section_name, key_name, file_name=os.path.dirname(os.path.abspath(__file__)) + "/../default.ini"):
    config = configparser.ConfigParser()
    config.read(file_name)
    value = config.get(section_name, key_name)
    return value

def rename_dict_key(dict_obj, old_key, new_key):
    """
    将字典中的指定键名 old_key 修改为 new_key，但对应的值不变。

    Args:
        dict_obj (dict): 需要修改键名的字典对象。
        old_key (str): 需要修改的键名。
        new_key (str): 修改后的键名。

    Returns:
        dict: 修改键名后的字典对象。

    """
    if old_key in dict_obj:
        dict_obj[new_key] = dict_obj.pop(old_key)
    return dict_obj

def delete_file_if_exists(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)