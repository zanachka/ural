from typing import NamedTuple, Optional, Union
from ural.types import AnyUrlTarget

class InstagramUser(NamedTuple):
    name: str

class InstagramPost(NameError):
    id: str
    name: str

def is_instagram_post_shortcode(value: str) -> bool: ...
def is_instagram_username(value: str) -> bool: ...
def is_instagram_url(url: AnyUrlTarget) -> bool: ...
def parse_instagram_url(
    url: AnyUrlTarget,
) -> Optional[Union[InstagramUser, InstagramPost]]: ...
def extract_username_from_instagram_url(url: AnyUrlTarget) -> Optional[str]: ...