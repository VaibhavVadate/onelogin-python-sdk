"""
    OneLogin API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 3.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from onelogin.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from onelogin.exceptions import ApiAttributeError


def lazy_import():
    from onelogin.model.hook_conditions_inner import HookConditionsInner
    from onelogin.model.hook_options import HookOptions
    globals()['HookConditionsInner'] = HookConditionsInner
    globals()['HookOptions'] = HookOptions


class Hook(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('status',): {
            'READY': "ready",
            'CREATE-QUEUED': "create-queued",
            'CREATE-RUNNING': "create-running",
            'CREATE-FAILED': "create-failed",
            'UPDATE-QUEUED': "update-queued",
            'UPDATE-RUNNING': "update-running",
            'UPDATE-FAILED': "update-failed",
        },
    }

    validations = {
        ('retries',): {
            'inclusive_maximum': 4,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'type': (str,),  # noqa: E501
            'disabled': (bool,),  # noqa: E501
            'timeout': (int,),  # noqa: E501
            'env_vars': ([str],),  # noqa: E501
            'runtime': (str,),  # noqa: E501
            'retries': (int,),  # noqa: E501
            'packages': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'function': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'context_version': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'options': (HookOptions,),  # noqa: E501
            'conditions': ([HookConditionsInner],),  # noqa: E501
            'created_at': (str,),  # noqa: E501
            'updated_at': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'disabled': 'disabled',  # noqa: E501
        'timeout': 'timeout',  # noqa: E501
        'env_vars': 'env_vars',  # noqa: E501
        'runtime': 'runtime',  # noqa: E501
        'retries': 'retries',  # noqa: E501
        'packages': 'packages',  # noqa: E501
        'function': 'function',  # noqa: E501
        'id': 'id',  # noqa: E501
        'context_version': 'context_version',  # noqa: E501
        'status': 'status',  # noqa: E501
        'options': 'options',  # noqa: E501
        'conditions': 'conditions',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, type, env_vars, runtime, packages, function, *args, **kwargs):  # noqa: E501
        """Hook - a model defined in OpenAPI

        Args:
            type (str): A string describing the type of hook. e.g. `pre-authentication`
            env_vars ([str]): Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code.
            runtime (str): The Smart Hooks supported Node.js version to execute this hook with.
            packages ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): An object containing NPM packages that are bundled with the hook function.
            function (str): A base64 encoded string containing the javascript function code.

        Keyword Args:
            disabled (bool): Boolean to enable or disable the hook. Disabled hooks will not run.. defaults to True  # noqa: E501
            timeout (int): The number of seconds to allow the hook function to run before before timing out. Maximum timeout varies based on the type of hook.. defaults to 1  # noqa: E501
            retries (int): Number of retries if execution fails.. defaults to 0  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): The Hook unique ID in OneLogin.. [optional]  # noqa: E501
            context_version (str): The semantic version of the content that will be injected into this hook.. [optional]  # noqa: E501
            status (str): String describing the state of the hook function. When a hook is ready and disabled is false it will be executed.. [optional]  # noqa: E501
            options (HookOptions): [optional]  # noqa: E501
            conditions ([HookConditionsInner]): An array of objects that let you limit the execution of a hook to users in specific roles.. [optional]  # noqa: E501
            created_at (str): ISO8601 format date that they hook function was created.. [optional]  # noqa: E501
            updated_at (str): ISO8601 format date that they hook function was last updated.. [optional]  # noqa: E501
        """

        disabled = kwargs.get('disabled', True)
        timeout = kwargs.get('timeout', 1)
        retries = kwargs.get('retries', 0)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.type = type
        self.disabled = disabled
        self.timeout = timeout
        self.env_vars = env_vars
        self.runtime = runtime
        self.retries = retries
        self.packages = packages
        self.function = function
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, type, env_vars, runtime, packages, function, *args, **kwargs):  # noqa: E501
        """Hook - a model defined in OpenAPI

        Args:
            type (str): A string describing the type of hook. e.g. `pre-authentication`
            env_vars ([str]): Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code.
            runtime (str): The Smart Hooks supported Node.js version to execute this hook with.
            packages ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): An object containing NPM packages that are bundled with the hook function.
            function (str): A base64 encoded string containing the javascript function code.

        Keyword Args:
            disabled (bool): Boolean to enable or disable the hook. Disabled hooks will not run.. defaults to True  # noqa: E501
            timeout (int): The number of seconds to allow the hook function to run before before timing out. Maximum timeout varies based on the type of hook.. defaults to 1  # noqa: E501
            retries (int): Number of retries if execution fails.. defaults to 0  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): The Hook unique ID in OneLogin.. [optional]  # noqa: E501
            context_version (str): The semantic version of the content that will be injected into this hook.. [optional]  # noqa: E501
            status (str): String describing the state of the hook function. When a hook is ready and disabled is false it will be executed.. [optional]  # noqa: E501
            options (HookOptions): [optional]  # noqa: E501
            conditions ([HookConditionsInner]): An array of objects that let you limit the execution of a hook to users in specific roles.. [optional]  # noqa: E501
            created_at (str): ISO8601 format date that they hook function was created.. [optional]  # noqa: E501
            updated_at (str): ISO8601 format date that they hook function was last updated.. [optional]  # noqa: E501
        """

        disabled = kwargs.get('disabled', True)
        timeout = kwargs.get('timeout', 1)
        retries = kwargs.get('retries', 0)
        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.type = type
        self.disabled = disabled
        self.timeout = timeout
        self.env_vars = env_vars
        self.runtime = runtime
        self.retries = retries
        self.packages = packages
        self.function = function
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")