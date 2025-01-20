from enum import Enum


class BookState(Enum):
    AVAILABLE = "available"
    CHECKED_OUT = "checked_out"
    LOST = "lost"


class UserState(Enum):
    COMMON = "common"
    ADMIN = "admin"
    VIP = "vip"
    BANNED = "banned"
