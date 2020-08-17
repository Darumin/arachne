from typing import Any
from functools import partial


def return_attribute(given: Any, attribute: str) -> str:
    return getattr(given, attribute)


def room_description(given: Any) -> str:
    desc = return_name(given)
    desc += "\n" + return_examined(given)
    return desc


return_name = partial(return_attribute, attribute="name")
return_examined = partial(return_attribute, attribute="when_examined")