import csv
import datetime
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random.random import randint

# Generate RSA Keys
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Encrypt and Decrypt Messages using RSA
def rsa_encrypt(public_key, message):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_message = cipher.encrypt(message.encode('utf-8'))
    return encrypted_message

def rsa_decrypt(private_key, encrypted_message):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode('utf-8')

# Generate Diffie-Hellman Keys
def generate_dh_key():
    p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1
    g = 2
    private_key = randint(2, p - 1)
    public_key = pow(g, private_key, p)
    return private_key, public_key

# Diffie-Hellman key exchange
def diffie_hellman_key_exchange(private_key, peer_public_key, p):
    shared_key = pow(peer_public_key, private_key, p)
    return shared_key

# Check for key revocation based on tenure end date
def check_key_revocation(employee_id, tenure_end_date):
    current_date = datetime.datetime.now().date()
    tenure_end_date = datetime.datetime.strptime(tenure_end_date, '%Y-%m-%d').date()

    if current_date > tenure_end_date:
        print(f"Key for employee {employee_id} has been revoked as the tenure has ended.")
        return True
    return False

# Add new employee to the CSV
def add_employee():
    with open('employee.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        employee_name = input("Enter Employee Name: ")
        employee_id = input("Enter Employee ID: ")
        department = input("Enter Department: ")
        tenure_end = input("Enter Tenure End Date (YYYY-MM-DD): ")

        if check_key_revocation(employee_id, tenure_end):
            print("Employee cannot be added due to revoked key.")
        else:
            writer.writerow([employee_name, employee_id, department, tenure_end])
            print(f"Employee {employee_name} added successfully!")

# Send secure message between two employees
def send_secure_message():
    employee1_id = input("Enter the sender's employee ID: ")
    employee2_id = input("Enter the receiver's employee ID: ")

    # Read the employee data from the CSV
    employees = {}
    with open('employee.csv','r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            employee_name, employee_id, department, tenure_end = row
            employees[employee_id] = {
                'name': employee_name,
                'tenure_end': tenure_end
            }

    # Check if sender or receiver tenure has ended
    if check_key_revocation(employee1_id, employees[employee1_id]['tenure_end']) or check_key_revocation(employee2_id, employees[employee2_id]['tenure_end']):
        print("Message cannot be sent. One or both employees' tenure has ended.")
        return

    # Generate RSA keys for encryption and decryption
    private_key, public_key = generate_rsa_keys()

    # Perform RSA encryption
    message = input("Enter the message to send: ")
    encrypted_message = rsa_encrypt(public_key, message)

    # Perform Diffie-Hellman key exchange
    private_key_A, public_key_A = generate_dh_key()
    private_key_B, public_key_B = generate_dh_key()
    p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1

    shared_key_A = diffie_hellman_key_exchange(private_key_A, public_key_B, p)
    shared_key_B = diffie_hellman_key_exchange(private_key_B, public_key_A, p)

    # Decrypt the message using the receiver's private key
    decrypted_message = rsa_decrypt(private_key, encrypted_message)

    print(f"Message sent successfully from {employees[employee1_id]['name']} to {employees[employee2_id]['name']}")
    print(f"Decrypted Message: {decrypted_message}")

# Menu-driven program
def menu():
    while True:
        print("\n--- SecureCorp Communication System ---")
        print("1. Send a secure message between two employees")
        print("2. Add a new employee to the system")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            send_secure_message()
        elif choice == '2':
            add_employee()
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()