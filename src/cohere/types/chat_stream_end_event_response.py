# This file was auto-generated by Fern from our API Definition.

import typing

from .non_streamed_chat_response import NonStreamedChatResponse
from .search_queries_only_response import SearchQueriesOnlyResponse

ChatStreamEndEventResponse = typing.Union[NonStreamedChatResponse, SearchQueriesOnlyResponse]