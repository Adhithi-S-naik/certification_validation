import solcx
import json

# Install Solidity compiler version 0.8.10
solcx.install_solc('0.8.10')

# Read Solidity contract source code
with open('Certification.sol', 'r') as file:
        contract_source_code = file.read()

        # Compile Solidity contract source code
        compiled_sol = solcx.compile_source(contract_source_code, solc_version='0.8.10')

        # Retrieve contract interface
        contract_interface = compiled_sol['<stdin>:Certification']

        # Print contract interface for verification
        print(json.dumps(contract_interface, indent=4))

        # Save contract interface to a file
        with open('Certification.json', 'w') as f:
                json.dump(contract_interface, f, indent=4)
