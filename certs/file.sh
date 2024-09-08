# Get configuration from user                                   # [dn]
read -p "Country Code (e.g., US): " Country                     # C
read -p "State/Province name (e.g., California): " State        # ST
read -p "City (e.g., San Francisco): " City                     # L
read -p "Organization (Best Company) " Organization             # O
read -p "Department (e.g., IT): " Department                    # OU
read -p "Common Name (www.mycompany.com): " CommonName          # CN
read -p "Your server name (e.g., localhost, test.com): " DNS
read -p "Your server IP address (e.g., 127.0.0.1): " IP

read -p "Confirm ? (Y/N): " confirm && [[ $confirm = [yY] || $confirm == [yY][eE][sS] ]] || exit 1

# Generate the CA key
openssl genrsa -out ca.key 2048

# Create the CA configuration file
cat > csr.conf <<EOL
[req]
default_bits = 2048
prompt = no
default_md = sha256
req_extensions = req_ext
distinguished_name = dn

[dn]
C = $Country
ST = $State
L = $City
O = $Organization
OU = $Department
CN = $CommonName

[req_ext]
subjectAltName = @alt_names

[alt_names]
DNS.1 = $DNS
IP.1 = $IP
EOL

# Create a certificate signing request (CSR) using the CA key and configuration
openssl req -new -sha256 -key ca.key -out ca.csr -config csr.conf

# Create a self-signed certificate for the CA
openssl x509 -req -sha256 -days 730 -in ca.csr -signkey ca.key -out ca.crt

# Generate the server key
openssl genrsa -out server.key 2048

# Create a server certificate signing request (CSR) using the server key and the same configuration
openssl req -new -sha256 -key server.key -out server.csr -config csr.conf

# Create the server certificate configuration file
cat > cert.conf <<EOL
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
subjectAltName = @alt_names

[alt_names]
DNS.1 = $DNS
EOL

# Create a signed certificate for the server using the CA certificate and key
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 3650 -sha256 -extfile cert.conf

# Create a combined PEM file containing the server key, server certificate, and CA certificate
cat server.key > cert.pem
cat server.crt >> cert.pem
cat ca.crt >> cert.pem
