from typing import Any, Awaitable, Callable, Coroutine

import structlog
from fastapi import Request, Response
from fastapi.routing import APIRoute

logger = structlog.getLogger()

class MiddlewareRoute(APIRoute):
    _before_request_chain: list[Callable[[Request], Awaitable[None]]] = []
    _after_response_chain: list[Callable[[Request, Response], Awaitable[None]]] = []
    _exception_handlers: dict[type[Exception], Callable[[Request, Exception], Awaitable[Response]]] = {}
    _default_exc_handler: Callable[[Request, Exception], Awaitable[Response]]

    @classmethod
    def add_before_request(
        cls,
        processor: Callable[[Request], Awaitable[None]],
    ) -> Callable[[Request], Awaitable[None]]:
        cls._before_request_chain.append(processor)
        return processor

    @classmethod
    def add_after_response(
        cls,
        processor: Callable[[Request, Response], Awaitable[None]],
    ) -> Callable[[Request, Response], Awaitable[None]]:
        cls._after_response_chain.append(processor)
        return processor

    @classmethod
    def add_exception_handler(
        cls,
        *exceptions: type[Exception],
    ) -> Callable[
        [Callable[[Request, Exception], Awaitable[Response]]], Callable[[Request, Exception], Awaitable[Response]]
    ]:
        def _handler(
            processor: Callable[[Request, Exception], Awaitable[Response]],
        ) -> Callable[[Request, Exception], Awaitable[Response]]:
            for exc in exceptions:
                cls._exception_handlers[exc] = processor
            return processor

        return _handler

    @classmethod
    def set_default_exception_handler(cls, processor: Callable[[Request, Exception], Awaitable[Response]]) -> None:
        cls._default_exc_handler = processor

    async def _process_before_request_chain(self, request: Request) -> None:
        for processor in self._before_request_chain:
            await processor(request)

    async def _process_after_response_chain(self, request: Request, response: Response) -> None:
        for processor in self._after_response_chain:
            await processor(request, response)

    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        original_route_handler = super().get_route_handler()

        async def middleware_handler(request: Request) -> Response:
            try:
                await self._process_before_request_chain(request)
                response = await original_route_handler(request)
                await self._process_after_response_chain(request, response)
                return response
            except Exception as ex:
                handler = self._exception_handlers.get(ex.__class__, MiddlewareRoute._default_exc_handler)
                return await handler(request, ex)

        return middleware_handler
