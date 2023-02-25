from typing import Optional
from ural.types import AnyUrlTarget

def is_amp_url(url: AnyUrlTarget) -> bool: ...
def is_google_link(url: AnyUrlTarget) -> bool: ...
def extract_url_from_google_link(url: str) -> Optional[str]: ...

class GoogleDriveParsedItem(object):
    type: str
    id: str

    def __init__(self, _type: str, _id: str): ...
    @property
    def url(self) -> str: ...
    def get_export_url(self, format: str = ...) -> str: ...

class GoogleDriveFile(GoogleDriveParsedItem): ...
class GoogleDrivePublicLink(GoogleDriveParsedItem): ...

def parse_google_drive_url(url: AnyUrlTarget) -> Optional[GoogleDriveParsedItem]: ...
def extract_id_from_google_drive_url(url: AnyUrlTarget) -> Optional[str]: ...