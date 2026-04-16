from core.physical_layer import PhysicalLayer
from core.mac_layer import MACLayer
from routing.aodv_protocol import AODVProtocol
from security.ecc_encryptor import ECCEncryptor
from utils.gps_sim import GPSUnit
from utils.logger import TelemetryLogger

def run_spartan_radio():
    # 1. Initialize Radio
    phy = PhysicalLayer()
    mac = MACLayer()
    gps = GPSUnit(x=100, y=100)
    crypto = ECCEncryptor()
    log = TelemetryLogger()

    # 2. Simulate Packet Creation
    payload = "SECURE_COORD_DATA"
    sig = crypto.sign_packet(payload)
    
    # 3. Simulate "The Air"
    distance = 450 # meters
    sinr = phy.calculate_sinr(distance)
    
    if sinr > 10: # Threshold for 16-QAM
        status = "SUCCESS"
    else:
        status = "SIGNAL_LOST"

    log.log_transmission("NODE_01", "BASE_STATION", sinr, status)

if __name__ == "__main__":
    print("--- TSC: MANET RADIO STARTING ---")
    run_spartan_radio()
