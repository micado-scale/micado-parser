from ruamel.yaml import YAML, representer


class NonAliasingRTRepresenter(representer.RoundTripRepresenter):
    """Turn off auto-aliases in ruamel.yaml"""

    def ignore_aliases(self, _):
        return True


yaml = YAML()
yaml.default_flow_style = False
yaml.preserve_quotes = True
yaml.Representer = NonAliasingRTRepresenter


def dump_order_yaml(data, path):
    """Dump the dictionary to a yaml file"""

    with open(path, "w") as file:
        yaml.dump(data, file)


def get_yaml_data(path, stream=False):
    """Retrieve the yaml dictionary form a yaml file and return it"""

    if stream:
        return yaml.load(path)

    with open(path, "r") as file:
        data = yaml.load(file)

    return data


def resolve_get_functions(
    dict_to_search, key_to_find, test_result_fn, resolve_result_fn, *args
):
    """Recursively update a dict with TOSCA 'get' functions

    Args:
        dict_to_search (dict): Dictionary to iterate through
        key_to_find (str): 'get' function to search for (eg 'get_input')
        test_result_fn (func): Function to test the result
        resolve_result_fn (func): Function to resolve the result
        args (*): Extra args to pass to resolve_result_fn

    Returns:
        None: Modifies the dictionary in place
    """
    for key, value in dict_to_search.items():
        if key == key_to_find:
            return value

        elif isinstance(value, dict):
            result = resolve_get_functions(
                value, key_to_find, test_result_fn, resolve_result_fn, *args
            )
            if test_result_fn(result):
                dict_to_search[key] = resolve_result_fn(result, *args)

        elif isinstance(value, list):
            for index, item in enumerate(value):
                if not isinstance(item, dict):
                    continue
                result = resolve_get_functions(
                    item, key_to_find, test_result_fn, resolve_result_fn, *args
                )
                if test_result_fn(result):
                    dict_to_search[key][index] = resolve_result_fn(result, *args)
