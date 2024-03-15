# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..errors.too_many_requests_error import TooManyRequestsError
from ..types.dataset_type import DatasetType
from .types.datasets_create_response import DatasetsCreateResponse
from .types.datasets_get_response import DatasetsGetResponse
from .types.datasets_get_usage_response import DatasetsGetUsageResponse
from .types.datasets_list_response import DatasetsListResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        dataset_type: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetsListResponse:
        """
        List datasets that have been created.

        Parameters:
            - dataset_type: typing.Optional[str]. optional filter by dataset type

            - before: typing.Optional[dt.datetime]. optional filter before a date

            - after: typing.Optional[dt.datetime]. optional filter after a date

            - limit: typing.Optional[float]. optional limit to number of results

            - offset: typing.Optional[float]. optional offset to start of results

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import Cohere

        client = Cohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        client.datasets.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "datasets"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "datasetType": dataset_type,
                        "before": serialize_datetime(before) if before is not None else None,
                        "after": serialize_datetime(after) if after is not None else None,
                        "limit": limit,
                        "offset": offset,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsListResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        name: str,
        type: DatasetType,
        keep_original_file: typing.Optional[bool] = None,
        skip_malformed_input: typing.Optional[bool] = None,
        keep_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        optional_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        text_separator: typing.Optional[str] = None,
        csv_delimiter: typing.Optional[str] = None,
        data: core.File,
        eval_data: typing.Optional[core.File] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetsCreateResponse:
        """
        Create a dataset by uploading a file. See ['Dataset Creation'](https://docs.cohere.com/docs/datasets#dataset-creation) for more information.

        Parameters:
            - name: str. The name of the uploaded dataset.

            - type: DatasetType. The dataset type, which is used to validate the data.

            - keep_original_file: typing.Optional[bool]. Indicates if the original file should be stored.

            - skip_malformed_input: typing.Optional[bool]. Indicates whether rows with malformed input should be dropped (instead of failing the validation check). Dropped rows will be returned in the warnings field.

            - keep_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]]. List of names of fields that will be persisted in the Dataset. By default the Dataset will retain only the required fields indicated in the [schema for the corresponding Dataset type](https://docs.cohere.com/docs/datasets#dataset-types). For example, datasets of type `embed-input` will drop all fields other than the required `text` field. If any of the fields in `keep_fields` are missing from the uploaded file, Dataset validation will fail.

            - optional_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]]. List of names of fields that will be persisted in the Dataset. By default the Dataset will retain only the required fields indicated in the [schema for the corresponding Dataset type](https://docs.cohere.com/docs/datasets#dataset-types). For example, Datasets of type `embed-input` will drop all fields other than the required `text` field. If any of the fields in `optional_fields` are missing from the uploaded file, Dataset validation will pass.

            - text_separator: typing.Optional[str]. Raw .txt uploads will be split into entries using the text_separator value.

            - csv_delimiter: typing.Optional[str]. The delimiter used for .csv uploads.

            - data: core.File. See core.File for more documentation

            - eval_data: typing.Optional[core.File]. See core.File for more documentation

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "datasets"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        "type": type,
                        "keep_original_file": keep_original_file,
                        "skip_malformed_input": skip_malformed_input,
                        "keep_fields": keep_fields,
                        "optional_fields": optional_fields,
                        "text_separator": text_separator,
                        "csv_delimiter": csv_delimiter,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            data=jsonable_encoder(remove_none_from_dict({}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"data": data, "eval_data": eval_data})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> DatasetsGetUsageResponse:
        """
        View the dataset storage usage for your Organization. Each Organization can have up to 10GB of storage across all their users.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import Cohere

        client = Cohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        client.datasets.get_usage()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "datasets/usage"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsGetUsageResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DatasetsGetResponse:
        """
        Retrieve a dataset by ID. See ['Datasets'](https://docs.cohere.com/docs/datasets) for more information.

        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import Cohere

        client = Cohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        client.datasets.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"datasets/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsGetResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a dataset by ID. Datasets are automatically deleted after 30 days, but they can also be deleted manually.

        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import Cohere

        client = Cohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        client.datasets.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"datasets/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        dataset_type: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetsListResponse:
        """
        List datasets that have been created.

        Parameters:
            - dataset_type: typing.Optional[str]. optional filter by dataset type

            - before: typing.Optional[dt.datetime]. optional filter before a date

            - after: typing.Optional[dt.datetime]. optional filter after a date

            - limit: typing.Optional[float]. optional limit to number of results

            - offset: typing.Optional[float]. optional offset to start of results

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import AsyncCohere

        client = AsyncCohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        await client.datasets.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "datasets"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "datasetType": dataset_type,
                        "before": serialize_datetime(before) if before is not None else None,
                        "after": serialize_datetime(after) if after is not None else None,
                        "limit": limit,
                        "offset": offset,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsListResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        name: str,
        type: DatasetType,
        keep_original_file: typing.Optional[bool] = None,
        skip_malformed_input: typing.Optional[bool] = None,
        keep_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        optional_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        text_separator: typing.Optional[str] = None,
        csv_delimiter: typing.Optional[str] = None,
        data: core.File,
        eval_data: typing.Optional[core.File] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DatasetsCreateResponse:
        """
        Create a dataset by uploading a file. See ['Dataset Creation'](https://docs.cohere.com/docs/datasets#dataset-creation) for more information.

        Parameters:
            - name: str. The name of the uploaded dataset.

            - type: DatasetType. The dataset type, which is used to validate the data.

            - keep_original_file: typing.Optional[bool]. Indicates if the original file should be stored.

            - skip_malformed_input: typing.Optional[bool]. Indicates whether rows with malformed input should be dropped (instead of failing the validation check). Dropped rows will be returned in the warnings field.

            - keep_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]]. List of names of fields that will be persisted in the Dataset. By default the Dataset will retain only the required fields indicated in the [schema for the corresponding Dataset type](https://docs.cohere.com/docs/datasets#dataset-types). For example, datasets of type `embed-input` will drop all fields other than the required `text` field. If any of the fields in `keep_fields` are missing from the uploaded file, Dataset validation will fail.

            - optional_fields: typing.Optional[typing.Union[str, typing.Sequence[str]]]. List of names of fields that will be persisted in the Dataset. By default the Dataset will retain only the required fields indicated in the [schema for the corresponding Dataset type](https://docs.cohere.com/docs/datasets#dataset-types). For example, Datasets of type `embed-input` will drop all fields other than the required `text` field. If any of the fields in `optional_fields` are missing from the uploaded file, Dataset validation will pass.

            - text_separator: typing.Optional[str]. Raw .txt uploads will be split into entries using the text_separator value.

            - csv_delimiter: typing.Optional[str]. The delimiter used for .csv uploads.

            - data: core.File. See core.File for more documentation

            - eval_data: typing.Optional[core.File]. See core.File for more documentation

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "datasets"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "name": name,
                        "type": type,
                        "keep_original_file": keep_original_file,
                        "skip_malformed_input": skip_malformed_input,
                        "keep_fields": keep_fields,
                        "optional_fields": optional_fields,
                        "text_separator": text_separator,
                        "csv_delimiter": csv_delimiter,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            data=jsonable_encoder(remove_none_from_dict({}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"data": data, "eval_data": eval_data})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsCreateResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> DatasetsGetUsageResponse:
        """
        View the dataset storage usage for your Organization. Each Organization can have up to 10GB of storage across all their users.

        Parameters:
            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import AsyncCohere

        client = AsyncCohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        await client.datasets.get_usage()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "datasets/usage"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsGetUsageResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DatasetsGetResponse:
        """
        Retrieve a dataset by ID. See ['Datasets'](https://docs.cohere.com/docs/datasets) for more information.

        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import AsyncCohere

        client = AsyncCohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        await client.datasets.get(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"datasets/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(DatasetsGetResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a dataset by ID. Datasets are automatically deleted after 30 days, but they can also be deleted manually.

        Parameters:
            - id: str.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.client import AsyncCohere

        client = AsyncCohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        await client.datasets.delete(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"datasets/{jsonable_encoder(id)}"),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.Dict[str, typing.Any], _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
