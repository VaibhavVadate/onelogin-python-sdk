# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr

from typing import List, Optional

from onelogin.models.get_event_by_id200_response import GetEventById200Response
from onelogin.models.get_event_types200_response import GetEventTypes200Response
from onelogin.models.get_events200_response import GetEvents200Response

from onelogin.api_client import ApiClient
from onelogin.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class EventsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_event_by_id(self, event_id : StrictInt, **kwargs) -> GetEventById200Response:  # noqa: E501
        """Get Event by ID  # noqa: E501

        Get Event By ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_by_id(event_id, async_req=True)
        >>> result = thread.get()

        :param event_id: (required)
        :type event_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetEventById200Response
        """
        kwargs['_return_http_data_only'] = True
        return self.get_event_by_id_with_http_info(event_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_event_by_id_with_http_info(self, event_id : StrictInt, **kwargs):  # noqa: E501
        """Get Event by ID  # noqa: E501

        Get Event By ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_by_id_with_http_info(event_id, async_req=True)
        >>> result = thread.get()

        :param event_id: (required)
        :type event_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetEventById200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'event_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['event_id']:
            _path_params['event_id'] = _params['event_id']

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "GetEventById200Response",
            '400': "GenerateToken400Response",
            '401': "GenerateToken400Response",
            '404': "GenerateToken400Response",
        }

        return self.api_client.call_api(
            '/api/1/events/{event_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_event_types(self, content_type : Optional[StrictStr] = None, **kwargs) -> GetEventTypes200Response:  # noqa: E501
        """Get Event Types  # noqa: E501

        Get Event types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_types(content_type, async_req=True)
        >>> result = thread.get()

        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetEventTypes200Response
        """
        kwargs['_return_http_data_only'] = True
        return self.get_event_types_with_http_info(content_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_event_types_with_http_info(self, content_type : Optional[StrictStr] = None, **kwargs):  # noqa: E501
        """Get Event Types  # noqa: E501

        Get Event types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event_types_with_http_info(content_type, async_req=True)
        >>> result = thread.get()

        :param content_type:
        :type content_type: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetEventTypes200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'content_type'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_event_types" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_type']:
            _header_params['Content-Type'] = _params['content_type']

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "GetEventTypes200Response",
        }

        return self.api_client.call_api(
            '/api/1/events/types', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_events(self, id : StrictInt, event_type_id : Optional[List[StrictInt]] = None, client_id : Optional[StrictInt] = None, directory_id : Optional[StrictInt] = None, created_at : Optional[StrictStr] = None, resolution : Optional[StrictStr] = None, since : Optional[StrictStr] = None, until : Optional[StrictStr] = None, user_id : Annotated[Optional[StrictInt], Field(description="Set to the id of the user that you want to return.")] = None, **kwargs) -> GetEvents200Response:  # noqa: E501
        """Get Events  # noqa: E501

        Get Events  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events(id, event_type_id, client_id, directory_id, created_at, resolution, since, until, user_id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param event_type_id:
        :type event_type_id: List[int]
        :param client_id:
        :type client_id: int
        :param directory_id:
        :type directory_id: int
        :param created_at:
        :type created_at: str
        :param resolution:
        :type resolution: str
        :param since:
        :type since: str
        :param until:
        :type until: str
        :param user_id: Set to the id of the user that you want to return.
        :type user_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetEvents200Response
        """
        kwargs['_return_http_data_only'] = True
        return self.get_events_with_http_info(id, event_type_id, client_id, directory_id, created_at, resolution, since, until, user_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_events_with_http_info(self, id : StrictInt, event_type_id : Optional[List[StrictInt]] = None, client_id : Optional[StrictInt] = None, directory_id : Optional[StrictInt] = None, created_at : Optional[StrictStr] = None, resolution : Optional[StrictStr] = None, since : Optional[StrictStr] = None, until : Optional[StrictStr] = None, user_id : Annotated[Optional[StrictInt], Field(description="Set to the id of the user that you want to return.")] = None, **kwargs):  # noqa: E501
        """Get Events  # noqa: E501

        Get Events  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_events_with_http_info(id, event_type_id, client_id, directory_id, created_at, resolution, since, until, user_id, async_req=True)
        >>> result = thread.get()

        :param id: (required)
        :type id: int
        :param event_type_id:
        :type event_type_id: List[int]
        :param client_id:
        :type client_id: int
        :param directory_id:
        :type directory_id: int
        :param created_at:
        :type created_at: str
        :param resolution:
        :type resolution: str
        :param since:
        :type since: str
        :param until:
        :type until: str
        :param user_id: Set to the id of the user that you want to return.
        :type user_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetEvents200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'event_type_id',
            'client_id',
            'directory_id',
            'created_at',
            'resolution',
            'since',
            'until',
            'user_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_events" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('event_type_id') is not None:  # noqa: E501
            _query_params.append(('event_type_id', _params['event_type_id']))
            _collection_formats['event_type_id'] = 'multi'
        if _params.get('client_id') is not None:  # noqa: E501
            _query_params.append(('client_id', _params['client_id']))
        if _params.get('directory_id') is not None:  # noqa: E501
            _query_params.append(('directory_id', _params['directory_id']))
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))
        if _params.get('created_at') is not None:  # noqa: E501
            _query_params.append(('created_at', _params['created_at']))
        if _params.get('resolution') is not None:  # noqa: E501
            _query_params.append(('resolution', _params['resolution']))
        if _params.get('since') is not None:  # noqa: E501
            _query_params.append(('since', _params['since']))
        if _params.get('until') is not None:  # noqa: E501
            _query_params.append(('until', _params['until']))
        if _params.get('user_id') is not None:  # noqa: E501
            _query_params.append(('user_id', _params['user_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))

        # process the form parameters
        _form_params = []
        _files = {}

        # process the body parameter
        _body_params = None

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "GetEvents200Response",
            '400': "GenerateToken400Response",
            '401': "GenerateToken400Response",
        }

        return self.api_client.call_api(
            '/api/1/events', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))