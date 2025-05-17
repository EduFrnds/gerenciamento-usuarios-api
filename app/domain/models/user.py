import re
import string

from app.domain.ports.repository.user import IUsersRepository


class WeakPasswordError(Exception):
    def __init__(self, password, message: str = 'Senha é muito fraca'):
        self.message = message
        super().__init__(self.message)

def is_strong_pass(
    passwd: str,
    chars: int = 8,
    lowers: int = 3,
    uppers: int = 1,
    digits: int = 1,
):
    is_strong = re.search(
        (
            '(?=^.{%i,}$)'
            '(?=.*[a-z]{%i,})'
            '(?=.*[A-Z]{%i})'
            '(?=.*[0-9]{%i,})'
            '(?=.*[%s}]+)'
        )
        % (chars, lowers, uppers, digits, re.escape(string.punctuation)),
        passwd,
    )

    if not is_strong:
        if len(passwd) < chars:
            return WeakPasswordError(
                passwd, f'A senha deve ter pelo menos {chars} caracteres'
            )
        if not any(char.isdigit() for char in passwd):
            return WeakPasswordError(
                passwd, 'A senha deve conter pelo menos um dígito'
            )
        if not any(char.isupper() for char in passwd):
            return WeakPasswordError(
                passwd, 'A senha deve conter pelo menos uma letra maiúscula'
            )
        if not any(char.islower() for char in passwd):
            return WeakPasswordError(
                passwd, 'A senha deve conter pelo menos uma letra minúscula'
            )
        if not any(char in string.punctuation for char in passwd):
            return WeakPasswordError(
                passwd, 'A senha deve conter pelo menos um caractere especial'
            )
    return True

class User:

    def __init__(self):
        pass

    @classmethod
    def register(cls, user, repository: IUsersRepository):
        response = repository.find(username=user.username)

        if response:
            return False

        response = is_strong_pass(user.password)
        if not isinstance(response, bool):
            return response, None

        user = repository.register(user)

        return True, user

    # @classmethod
    # def authenticate_user(
    #         cls,
    #         user_crendentials,
    #         repository: IUsersRepository
    # ) -> Tuple[bool, Optional[UserModel], Optional[str]]:
    #
    #     user = repository.find(
    #         username=user_crendentials.username, password=user_crendentials.password
    #     )
    #     if not user:
    #         return False, None, "User not found"
    #
    #     if user.password != user_crendentials.password:
    #         return False, None, "Invalid credentials"
    #
    #     return True, user, None
