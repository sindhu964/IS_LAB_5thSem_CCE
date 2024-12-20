import random
import sympy
import time
import os
import logging
from datetime import datetime, timedelta

# Set up logging for auditing and compliance
logging.basicConfig(filename='key_management.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s %(message)s')

class RabinCryptosystem:
    def __init__(self, key_size=1024):
        self.key_size = key_size

    # Generate public and private key pairs using Rabin Cryptosystem
    def generate_keys(self):
        p = sympy.randprime(2**(self.key_size // 2 - 1), 2**(self.key_size // 2))
        q = sympy.randprime(2**(self.key_size // 2 - 1), 2**(self.key_size // 2))
        n = p * q
        return (n, (p, q))  # Public key (n) and private key (p, q)

    # Store keys securely (store private keys in encrypted files if needed)
    def store_private_key(self, clinic_id, private_key):
        with open(f'{clinic_id}_private_key.txt', 'w') as f:
            f.write(str(private_key))

    def store_public_key(self, clinic_id, public_key):
        with open(f'{clinic_id}_public_key.txt', 'w') as f:
            f.write(str(public_key))

    # Load public and private keys
    def load_private_key(self, clinic_id):
        with open(f'{clinic_id}_private_key.txt', 'r') as f:
            return eval(f.read())

    def load_public_key(self, clinic_id):
        with open(f'{clinic_id}_public_key.txt', 'r') as f:
            return eval(f.read())

    # Encrypt a message (message must be a number less than n)
    def encrypt(self, public_key, message):
        return pow(message, 2, public_key)

    # Decrypt a message
    def decrypt(self, private_key, ciphertext):
        p, q = private_key
        n = p * q
        # Rabin decryption results in multiple plaintext possibilities
        mp = pow(ciphertext, (p + 1) // 4, p)
        mq = pow(ciphertext, (q + 1) // 4, q)
        return self._chinese_remainder_theorem(mp, mq, p, q)

    # Chinese Remainder Theorem to get the plaintext
    def _chinese_remainder_theorem(self, mp, mq, p, q):
        def egcd(a, b):
            if a == 0:
                return (b, 0, 1)
            else:
                g, y, x = egcd(b % a, a)
                return (g, x - (b // a) * y, y)
        
        g, x_p, x_q = egcd(p, q)
        n = p * q
        plaintext1 = (mp * x_q * q + mq * x_p * p) % n
        return plaintext1  # This would be the correct plaintext based on context

# Main key management class
class KeyManagementService:
    def __init__(self):
        self.rabin = RabinCryptosystem()
        self.key_expiry_duration = timedelta(days=365)  # 12 months key expiry
    
    # Generate keys for a hospital or clinic
    def generate_and_store_keys(self, clinic_id):
        public_key, private_key = self.rabin.generate_keys()
        self.rabin.store_private_key(clinic_id, private_key)
        self.rabin.store_public_key(clinic_id, public_key)
        
        # Log the key generation event
        logging.info(f"Keys generated for {clinic_id}")
        print(f"Keys generated and stored for {clinic_id}")

    # Revoke keys for a hospital or clinic
    def revoke_keys(self, clinic_id):
        try:
            os.remove(f'{clinic_id}_private_key.txt')
            os.remove(f'{clinic_id}_public_key.txt')
            logging.info(f"Keys revoked for {clinic_id}")
            print(f"Keys revoked for {clinic_id}")
        except FileNotFoundError:
            logging.error(f"Attempted to revoke non-existing keys for {clinic_id}")
            print(f"No keys found for {clinic_id}")

    # Renew keys for all hospitals and clinics
    def renew_keys(self, clinic_id):
        print(f"Renewing keys for {clinic_id}")
        self.generate_and_store_keys(clinic_id)
        logging.info(f"Keys renewed for {clinic_id}")

    # Automatically renew keys based on expiry (e.g., 12 months)
    def auto_renew_keys(self, clinics):
        current_date = datetime.now()
        for clinic_id, expiry_date in clinics.items():
            if current_date >= expiry_date:
                self.renew_keys(clinic_id)
                clinics[clinic_id] = current_date + self.key_expiry_duration
                logging.info(f"Auto-renewed keys for {clinic_id}")

    # Display audit logs
    def display_audit_logs(self):
        with open('key_management.log', 'r') as log_file:
            logs = log_file.read()
            print(logs)

# Simulated list of clinics and their key expiration dates
clinics = {
    "clinicA": datetime.now() - timedelta(days=400),  # Already expired
    "clinicB": datetime.now() + timedelta(days=10),
}

# Menu-driven interface
def menu():
    kms = KeyManagementService()
    while True:
        print("\n--- Key Management System ---")
        print("1. Generate and store keys for a hospital/clinic")
        print("2. Revoke keys for a hospital/clinic")
        print("3. Auto-renew expired keys")
        print("4. Display audit logs")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            clinic_id = input("Enter clinic ID: ")
            kms.generate_and_store_keys(clinic_id)
        elif choice == '2':
            clinic_id = input("Enter clinic ID to revoke: ")
            kms.revoke_keys(clinic_id)
        elif choice == '3':
            kms.auto_renew_keys(clinics)
        elif choice == '4':
            kms.display_audit_logs()
        elif choice == '5':
            print("Exiting system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    menu()