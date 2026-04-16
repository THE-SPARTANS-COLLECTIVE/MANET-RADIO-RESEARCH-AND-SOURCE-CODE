import hashlib
import hmac

class ECCEncryptor:
    """HMAC-based Packet Integrity and Authentication."""
    def __init__(self, secret_key="SPARTAN_SECRET"):
        self.key = secret_key.encode()

    def sign_packet(self, data_string):
        """Creates a cryptographic signature for a packet."""
        return hmac.new(self.key, data_string.encode(), hashlib.sha256).hexdigest()

    def verify_packet(self, data_string, signature):
        """Verifies if the packet was tampered with."""
        expected = self.sign_packet(data_string)
        return hmac.compare_digest(expected, signature)
