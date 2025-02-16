# coding: utf-8

"""
    API documentation

    API for thingiverse.com

    The version of the OpenAPI document: 0.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from thingiverse.models.banner0_page_ad_get200_response import Banner0PageAdGet200Response
from thingiverse.models.banner_schema import BannerSchema

from thingiverse.api_client import ApiClient, RequestSerialized
from thingiverse.api_response import ApiResponse
from thingiverse.rest import RESTResponseType


class BannerApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def banner0_page_ad_get(
        self,
        location: Annotated[StrictStr, Field(description="This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page")],
        query: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword to perform a search in link parameter of banner")] = None,
        category_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The id of thing category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="The type of link of the banner")] = None,
        search: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Banner0PageAdGet200Response:
        """(Deprecated) Get banner (ad) for a certain page


        :param location: This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page (required)
        :type location: str
        :param query: This parameter is used as a keyword to perform a search in link parameter of banner
        :type query: str
        :param category_id: The id of thing category
        :type category_id: int
        :param type: The type of link of the banner
        :type type: str
        :param search: This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner
        :type search: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501
        warnings.warn("GET /banner/0/page-ad is deprecated.", DeprecationWarning)

        _param = self._banner0_page_ad_get_serialize(
            location=location,
            query=query,
            category_id=category_id,
            type=type,
            search=search,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Banner0PageAdGet200Response",
            '401': "ThingsPost401Response",
            '403': "ThingsPost403Response",
            '404': "ThingsPost404Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def banner0_page_ad_get_with_http_info(
        self,
        location: Annotated[StrictStr, Field(description="This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page")],
        query: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword to perform a search in link parameter of banner")] = None,
        category_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The id of thing category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="The type of link of the banner")] = None,
        search: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Banner0PageAdGet200Response]:
        """(Deprecated) Get banner (ad) for a certain page


        :param location: This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page (required)
        :type location: str
        :param query: This parameter is used as a keyword to perform a search in link parameter of banner
        :type query: str
        :param category_id: The id of thing category
        :type category_id: int
        :param type: The type of link of the banner
        :type type: str
        :param search: This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner
        :type search: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501
        warnings.warn("GET /banner/0/page-ad is deprecated.", DeprecationWarning)

        _param = self._banner0_page_ad_get_serialize(
            location=location,
            query=query,
            category_id=category_id,
            type=type,
            search=search,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Banner0PageAdGet200Response",
            '401': "ThingsPost401Response",
            '403': "ThingsPost403Response",
            '404': "ThingsPost404Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def banner0_page_ad_get_without_preload_content(
        self,
        location: Annotated[StrictStr, Field(description="This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page")],
        query: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword to perform a search in link parameter of banner")] = None,
        category_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The id of thing category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="The type of link of the banner")] = None,
        search: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """(Deprecated) Get banner (ad) for a certain page


        :param location: This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page (required)
        :type location: str
        :param query: This parameter is used as a keyword to perform a search in link parameter of banner
        :type query: str
        :param category_id: The id of thing category
        :type category_id: int
        :param type: The type of link of the banner
        :type type: str
        :param search: This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner
        :type search: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501
        warnings.warn("GET /banner/0/page-ad is deprecated.", DeprecationWarning)

        _param = self._banner0_page_ad_get_serialize(
            location=location,
            query=query,
            category_id=category_id,
            type=type,
            search=search,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Banner0PageAdGet200Response",
            '401': "ThingsPost401Response",
            '403': "ThingsPost403Response",
            '404': "ThingsPost404Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _banner0_page_ad_get_serialize(
        self,
        location,
        query,
        category_id,
        type,
        search,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if location is not None:
            
            _query_params.append(('location', location))
            
        if query is not None:
            
            _query_params.append(('query', query))
            
        if category_id is not None:
            
            _query_params.append(('category_id', category_id))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/banner/0/page-ad',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def banner_get(
        self,
        location: Annotated[StrictStr, Field(description="This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page")],
        query: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword to perform a search by link parameter of banner")] = None,
        category_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The id of thing category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="The type of link of the banner")] = None,
        search: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> BannerSchema:
        """(Deprecated) Get a banner (ad)


        :param location: This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page (required)
        :type location: str
        :param query: This parameter is used as a keyword to perform a search by link parameter of banner
        :type query: str
        :param category_id: The id of thing category
        :type category_id: int
        :param type: The type of link of the banner
        :type type: str
        :param search: This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner
        :type search: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501
        warnings.warn("GET /banner is deprecated.", DeprecationWarning)

        _param = self._banner_get_serialize(
            location=location,
            query=query,
            category_id=category_id,
            type=type,
            search=search,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BannerSchema",
            '401': "ThingsPost401Response",
            '403': "ThingsPost403Response",
            '404': "ThingsPost404Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def banner_get_with_http_info(
        self,
        location: Annotated[StrictStr, Field(description="This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page")],
        query: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword to perform a search by link parameter of banner")] = None,
        category_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The id of thing category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="The type of link of the banner")] = None,
        search: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[BannerSchema]:
        """(Deprecated) Get a banner (ad)


        :param location: This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page (required)
        :type location: str
        :param query: This parameter is used as a keyword to perform a search by link parameter of banner
        :type query: str
        :param category_id: The id of thing category
        :type category_id: int
        :param type: The type of link of the banner
        :type type: str
        :param search: This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner
        :type search: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501
        warnings.warn("GET /banner is deprecated.", DeprecationWarning)

        _param = self._banner_get_serialize(
            location=location,
            query=query,
            category_id=category_id,
            type=type,
            search=search,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BannerSchema",
            '401': "ThingsPost401Response",
            '403': "ThingsPost403Response",
            '404': "ThingsPost404Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def banner_get_without_preload_content(
        self,
        location: Annotated[StrictStr, Field(description="This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page")],
        query: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword to perform a search by link parameter of banner")] = None,
        category_id: Annotated[Optional[Annotated[int, Field(strict=True, ge=0)]], Field(description="The id of thing category")] = None,
        type: Annotated[Optional[StrictStr], Field(description="The type of link of the banner")] = None,
        search: Annotated[Optional[StrictStr], Field(description="This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """(Deprecated) Get a banner (ad)


        :param location: This parameter is responsible for getting the banner for the corresponding type of page at the specified location on the page (required)
        :type location: str
        :param query: This parameter is used as a keyword to perform a search by link parameter of banner
        :type query: str
        :param category_id: The id of thing category
        :type category_id: int
        :param type: The type of link of the banner
        :type type: str
        :param search: This parameter is used as a keyword or array of keywords to perform a search in industry parameter of banner
        :type search: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501
        warnings.warn("GET /banner is deprecated.", DeprecationWarning)

        _param = self._banner_get_serialize(
            location=location,
            query=query,
            category_id=category_id,
            type=type,
            search=search,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "BannerSchema",
            '401': "ThingsPost401Response",
            '403': "ThingsPost403Response",
            '404': "ThingsPost404Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _banner_get_serialize(
        self,
        location,
        query,
        category_id,
        type,
        search,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if location is not None:
            
            _query_params.append(('location', location))
            
        if query is not None:
            
            _query_params.append(('query', query))
            
        if category_id is not None:
            
            _query_params.append(('category_id', category_id))
            
        if type is not None:
            
            _query_params.append(('type', type))
            
        if search is not None:
            
            _query_params.append(('search', search))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'BearerAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/banner',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


