import logging

from certbot.plugins.dns_common import DNSAuthenticator

logger = logging.getLogger(__name__)


class LoopiaDnsAuthenticator(DNSAuthenticator):
    def _setup_credentials(self) -> None:
        pass

    def _perform(self, domain: str, validation_name: str, validation: str) -> None:
        logger.debug(
            f"Performing DNS validation for {domain=} with {validation_name=} and {validation=}"
        )

    def _cleanup(self, domain: str, validation_name: str, validation: str) -> None:
        pass
