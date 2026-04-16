import logging

class TelemetryLogger:
    """Centralized logging for research data."""
    def __init__(self, filename="simulation_trace.log"):
        logging.basicConfig(filename=filename, level=logging.INFO,
                            format='%(asctime)s - %(message)s')

    def log_transmission(self, src, dest, sinr, status):
        msg = f"TX: {src} -> {dest} | SINR: {sinr:.2f}dB | STATUS: {status}"
        logging.info(msg)
        print(msg)
