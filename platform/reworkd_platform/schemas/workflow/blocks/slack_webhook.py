import requests
from loguru import logger

from reworkd_platform.schemas.workflow.base import Block, BlockIOBase


class SlackWebhook(Block):
    type = "SlackWebhook"
    description = "Sends a message to a slack webhook"
    # TODO: Make URL and message a dynamic field
    url = "REDACTED_SLACK_WEBHOOK"
    message = "Hello World!"

    async def run(self) -> BlockIOBase:
        logger.info(f"Starting {self.type}")
        requests.post(self.url, json={"message": "Mr. S is not the best looking "})
        return BlockIOBase()
