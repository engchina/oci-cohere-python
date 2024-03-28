# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Hyperparameters(pydantic.BaseModel):
    """
    The fine-tuning hyperparameters.
    """

    early_stopping_patience: typing.Optional[int] = pydantic.Field(default=None)
    """
    Stops training if the loss metric does not improve beyond the value of
    `early_stopping_threshold` after this many times of evaluation.
    """

    early_stopping_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    How much the loss must improve to prevent early stopping.
    """

    train_batch_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The batch size is the number of training examples included in a single
    training pass.
    """

    train_epochs: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of epochs to train for.
    """

    learning_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    The learning rate to be used during training.
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}