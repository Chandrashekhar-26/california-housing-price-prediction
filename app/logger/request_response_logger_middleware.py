from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware, Response
import time
from .logger import logger


class RequestResponseLoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        # Log only prediction
        if request.url.path != "/app/api/v1/housing-price/predict":
            return await call_next(request)

        start_time = time.time()

        # Log Request and Response
        body_bytes = await request.body()
        body_text = body_bytes.decode("utf-8") if body_bytes else ""

        # Process request
        response = await call_next(request)
        duration = time.time() - start_time
        text_response, response = await self.response_to_text(response)

        log_data = {
            'request': {
                'mothod': request.method,
                'url': request.url,
                'body': body_text
            },
            'response': {
                'status': response.status_code,
                'body': text_response,
                'duration': duration
            }
        }

        logger.log_info(f"{log_data}")

        return response

    async def response_to_text(self, response):
        body = b""
        async for chunk in response.body_iterator:
            body += chunk

        # Create or Rebuild a cloned response with the same content and properties as it is only read once
        cloned_response = Response(
            content=body,
            status_code=response.status_code,
            headers=dict(response.headers),
            media_type=response.media_type,
        )

        return body.decode("utf-8", errors="ignore"), cloned_response
