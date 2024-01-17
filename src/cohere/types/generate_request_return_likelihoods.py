# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GenerateRequestReturnLikelihoods(str, enum.Enum):
    """
    One of `GENERATION|ALL|NONE` to specify how and if the token likelihoods are returned with the response. Defaults to `NONE`.

    If `GENERATION` is selected, the token likelihoods will only be provided for generated text.

    If `ALL` is selected, the token likelihoods will be provided both for the prompt and the generated text.
    """

    GENERATION = "GENERATION"
    ALL = "ALL"
    NONE = "NONE"

    def visit(
        self,
        generation: typing.Callable[[], T_Result],
        all: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GenerateRequestReturnLikelihoods.GENERATION:
            return generation()
        if self is GenerateRequestReturnLikelihoods.ALL:
            return all()
        if self is GenerateRequestReturnLikelihoods.NONE:
            return none()