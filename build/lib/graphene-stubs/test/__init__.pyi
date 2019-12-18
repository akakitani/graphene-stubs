from graphene.types.schema import Schema as Schema
from typing import Any, Optional

def default_format_error(error: Any) -> Any: ...
def format_execution_result(execution_result: Any, format_error: Any) -> Any: ...

class Client:
    schema: Any = ...
    execute_options: Any = ...
    format_error: Any = ...
    def __init__(self, schema: Any, format_error: Optional[Any] = ..., **execute_options: Any) -> None: ...
    def format_result(self, result: Any) -> Any: ...
    def execute(self, *args: Any, **kwargs: Any) -> Any: ...