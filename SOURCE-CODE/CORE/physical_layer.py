import numpy as np

class PhysicalLayer:
    """Mathematical model of the Radio Frequency (RF) environment."""
    def __init__(self, freq_hz=2.4e9, tx_power_dbm=20.0):
        self.c = 299792458  # Speed of light m/s
        self.freq = freq_hz
        self.wavelength = self.c / self.freq
        self.tx_power_dbm = tx_power_dbm
        self.noise_floor_dbm = -100.0

    def calculate_path_loss(self, distance, exponent=2.7):
        """Log-distance path loss model."""
        if distance < 1: distance = 1
        # FSPL (Free Space Path Loss) + Shadowing
        loss = 20 * np.log10(distance) + 20 * np.log10(self.freq) - 147.55
        return loss

    def get_snr(self, rx_power_dbm):
        """Calculates Signal-to-Noise Ratio."""
        return rx_power_dbm - self.noise_floor_dbm

    def is_packet_recoverable(self, snr, ber_threshold=1e-5):
        """Determines if the signal is above the thermal noise threshold."""
        return snr > 10.0  # Simplified 10dB threshold for QPSK
