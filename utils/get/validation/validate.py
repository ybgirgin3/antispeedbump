from dataclasses import dataclass

@dataclass
class InnerPath:
    expression: list

@dataclass
class ContentPath:
    id: dict
    username: dict
    following_count: dict
    follower_count: dict
    profile_picture: dict

