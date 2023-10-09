from uuid import UUID, uuid4
from .user import User
from history.text_message import TextMessage
from history.video_message import VideoMessage
from history.image_message import ImageMessage


class Chat:
    def __init__(self, name: str, creator_user: User) -> None:
        self.__check_name(name)
        self.__check_creator_user(creator_user)
        self.__name: str = name
        self.__creator_user: User = creator_user
        self.__id: UUID = uuid4()
        self.__users: list[User] = []

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        if not isinstance(name, str):
            raise TypeError(f"Expected str, got {type(name)}")
        self.__name = name

    @property
    def creator_user(self) -> User:
        return self.__creator_user
    
    @property
    def id(self) -> UUID:
        return self.__id
    
    @property
    def users(self) -> list[User]:
        return self.__users
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Chat):
            return False
        return self.__id == other.id and self.__name == other.name

    def user_in_chat(self, user: User) -> bool:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        for u in self.__users:
            if u == user:
                return True
        return False

    def change_creator_user(self) -> None:
        for user in self.__users:
            if user != self.__creator_user:
                self.__creator_user = user
                return

    def add_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        self.__users.append(user)
    
    def remove_user(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        self.__users.remove(user)

    # Maybe this should be in a message display
    def __create_message_prefix(self, user: User) -> str:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        return f"{user.nickname}: "
    
    # idk if this is the best way to do this
    def send_text_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        content = ... # get message from display
        message = TextMessage(content)
        #print(self.__create_message_prefix(user) + message)
    
    def send_image_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        path = ...
        message = ImageMessage(path)
        #print(self.__create_message_prefix(user) + message)
    
    def send_video_message(self, user: User) -> None:
        if not isinstance(user, User):
            raise TypeError(f"Expected User, got {type(user)}")
        if user not in self.__users:
            raise Exception('User not found')
        path = ...
        message = VideoMessage(path)
        #print(self.__create_message_prefix(user) + message)

    def __check_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')
        if len(name) < 3:
            raise ValueError('Name must be at least 3 characters long')

    def __check_creator_user(self, creator_user: User):
        if not isinstance(creator_user, User):
            raise TypeError('Creator user must be a User object')
