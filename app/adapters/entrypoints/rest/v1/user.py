import sqlite3
from datetime import datetime
from typing import Any, Coroutine
from urllib import response

from dependency_injector.wiring import Provide, inject, Provider
from fastapi import APIRouter, Depends, Response, status

from app.adapters.entrypoints.rest import http
from app.adapters.entrypoints.rest.v1.model import user
from app.adapters.entrypoints.rest.v1.model.user import (CreateUserV1Request,
                                                         CreateUserV1Response, CreateUserV1ListResponse,
                                                         CreateUserV1ResponseError)
from dependency_injector.wiring import inject

from app.configs.dependecy import UserRepositoryProvider
from app.domain.models.user import User
from app.adapters.repositories import UserRepository
from app.domain.ports.user import UserPort
from app.logging_config import configure_logging


logger = configure_logging()
router = APIRouter()
provider = UserRepositoryProvider()

@router.get("/api/v1/users", response_model=CreateUserV1ListResponse,status_code=status.HTTP_200_OK)
@inject
async def read_all_users(
        user_port: UserPort = Depends(lambda: provider.get_user_repository())) -> CreateUserV1ListResponse:
    """
    Buscar todos os usuários cadastrados no banco de dados.

    **Retorno:**
    - Um objeto `CreateUserV1ListResponse`, que contém um array de `CreateUserV1Response` com os detalhes
    dos usuários cadastrados.

    **Códigos de Status:**
    - 200: Sucesso na busca dos usuários.
    - 500: Erro interno do servidor.
    """

    try:
        users_data = await user_port.get_all_users()
    except Exception as e:
        logger.error(f"Erro ao buscar usuários: {e}")
        return CreateUserV1ListResponse(users=[])

    list_users = [
        CreateUserV1Response(
            user_id=data.id,
            user_name=data.user_name,
            user_email=data.user_email
        ) for data in users_data
    ]

    return CreateUserV1ListResponse(users=list_users)


@router.get("/api/v1/users/{user_id}", response_model=CreateUserV1Response, status_code=status.HTTP_200_OK)
@inject
async def read_user(
        user_id: int,
        response: Response,
        user_port: UserPort = Depends(lambda: provider.get_user_repository())
) -> CreateUserV1Response:
    """
    Buscar um usuário cadastrado no banco de dados pelo ID.

    **Retorno:**
    - Um objeto `CreateUserV1Response` com os detalhes do usuário, ou erro se não encontrado.

    **Códigos de Status:**
    - 200: Sucesso na busca do usuário.
    - 404: Usuário não encontrado.
    - 500: Erro interno do servidor.
    """

    try:
        user = await user_port.get_user_by_id(user_id=user_id)

        if user:
            return CreateUserV1Response(
                user_id=user.id,
                user_name=user.user_name,
                user_email=user.user_email
            )
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return CreateUserV1Response(
                user_id=user_id
            )
    except Exception as e:
        logger.error(f"Erro ao buscar usuário com ID {user_id}: {e}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return CreateUserV1Response(
            user_id=user_id,
            user_name="",
            user_email="",
        )
#
#
# @router.post("/api/v1/users", response_model=CreateUserV1Response, status_code=status.HTTP_201_CREATED)
# @inject
# async def create_user(
#         create_user_request: CreateUserV1Request,
#         response: Response,
#         user_port: UserPort = Depends(lambda: provider.get_user_repository()),
# ) -> CreateUserV1ResponseError | CreateUserV1Response:
#     """
#     Cria um novo usuário.
#
#     **Parâmetros:**
#     - `create_user_request`: Objeto que contém os dados do usuário a ser criado:
#         - `name`: Nome do usuário (string, obrigatório).
#         - `email`: Email do usuário (string, obrigatório).
#
#     **Retorno:**
#     - Um objeto `CreateUserV1Response` contendo o `user_id` do usuário criado.
#
#     **Códigos de Status:**
#     - 201: Usuário criado com sucesso.
#     - 500: Erro interno do servidor.
#     """
#
#     user = User(
#         user_name=create_user_request.user_name,
#         user_email=create_user_request.user_email
#     )
#
#     try:
#         user = await user_port.create_user(user=user)
#         return CreateUserV1Response(user_id=user.id)
#     except Exception as e:
#         logger.error(f"Erro ao criar usuário: {e}")
#         response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
#         return CreateUserV1ResponseError(
#             message="Erro ao criar usuário."
#         )
#
#
# @router.delete("/api/v1/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# @inject
# async def delete_user(
#         user_id: int,
#         response: Response,
#         user_port: UserPort = Depends(Provide[Container.user_port])
# ):
#     try:
#         await user_port.delete_user(user_id=user_id)
#         return response.status_code  # Retorna 204 sem conteúdo
#     except Exception as e:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"detail": "User not found"}  # Ou outra mensagem de erro