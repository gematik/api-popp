DOCKER_IMAGE=spilikin/popp-mock:latest


info:
	@echo "Available targets:"
	@echo "  requirements: generate requirements.txt"
	@echo "  dockerbuild: build docker image"
	@echo "  dockerpush: push docker image to registry"

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

docker-build: requirements
	docker buildx build --platform linux/amd64 -t $(DOCKER_IMAGE) .

docker-push: docker-build
	docker push $(DOCKER_IMAGE)


# Directory for storing secrets
SECRETS_DIR = ./secrets

# Variables for file names
KEY_FILE = $(SECRETS_DIR)/popp-signing-key.pem
CERT_FILE = $(SECRETS_DIR)/popp-signing-cert.pem
CSR_FILE = $(SECRETS_DIR)/popp-signing.csr
CA_KEY_FILE = $(SECRETS_DIR)/ca-key.pem
CA_CERT_FILE = $(SECRETS_DIR)/ca-cert.pem

# Validity period for the certificate
DAYS_VALID = 365

# Ensure the secrets directory exists
$(SECRETS_DIR):
	@echo "Creating secrets directory..."
	mkdir -p $(SECRETS_DIR)

# Target to generate the CA's private key
$(CA_KEY_FILE): $(SECRETS_DIR)
	@echo "Generating CA private key..."
	openssl ecparam -name prime256v1 -genkey -noout -out $(CA_KEY_FILE)

# Target to generate the CA's self-signed certificate
$(CA_CERT_FILE): $(CA_KEY_FILE)
	@echo "Generating CA self-signed certificate..."
	openssl req -x509 -new -key $(CA_KEY_FILE) -sha256 -days 365 -out $(CA_CERT_FILE) -subj "/C=DE/ST=Berlin/L=Berlin/O=gematik GmbH/CN=Test Components CA"

# Target to generate the private key
$(KEY_FILE): $(CA_CERT_FILE)
	@echo "Generating private key..."
	openssl ecparam -name prime256v1 -genkey -noout -out $(KEY_FILE)

# Target to generate the certificate signing request (CSR)
$(CSR_FILE): $(KEY_FILE) | $(SECRETS_DIR)
	@echo "Generating certificate signing request (CSR)..."
	openssl req -new -key $(KEY_FILE) -out $(CSR_FILE) -subj "/C=DE/ST=Berlin/L=Berlin/O=gematik GmbH/CN=Test POPP Signer"

# Target to generate the certificate signed by the CA
$(CERT_FILE): $(CSR_FILE) $(CA_KEY_FILE) $(CA_CERT_FILE)
	@echo "Signing certificate with CA..."
	openssl x509 -req -in $(CSR_FILE) -CA $(CA_CERT_FILE) -CAkey $(CA_KEY_FILE) -CAcreateserial -out $(CERT_FILE) -days $(DAYS_VALID)

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -f $(KEY_FILE) $(CERT_FILE) $(CSR_FILE) $(SECRETS_DIR)/*.srl

# Target to generate both the key and the certificate
all: $(CERT_FILE)

.PHONY: clean all

