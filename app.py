from flask import Flask, render_template, request, redirect, url_for
import hashlib
import json
from time import time

# Initialize Flask
app = Flask(__name__)

# -------------------------------
# Blockchain Class
# -------------------------------
class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_agreements = []
        self.new_block(previous_hash='1', proof=100)  # Genesis block

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'agreements': self.current_agreements,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_agreements = []
        self.chain.append(block)
        return block

    def new_agreement(self, landlord, tenant, property_addr, rent_amount, duration_months):
        agreement = {
            'landlord': landlord,
            'tenant': tenant,
            'property_addr': property_addr,
            'rent_amount': rent_amount,
            'duration_months': duration_months,
        }
        self.current_agreements.append(agreement)
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# Initialize blockchain
blockchain = Blockchain()

# -------------------------------
# Flask Routes
# -------------------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_agreement():
    if request.method == 'POST':
        landlord = request.form['landlord']
        tenant = request.form['tenant']
        property_addr = request.form['property_addr']
        rent_amount = request.form['rent_amount']
        duration_months = request.form['duration_months']

        # Add agreement
        index = blockchain.new_agreement(landlord, tenant, property_addr, rent_amount, duration_months)

        # Create a new block
        last_proof = blockchain.last_block['proof']
        proof = blockchain.proof_of_work(last_proof)
        previous_hash = blockchain.hash(blockchain.last_block)
        blockchain.new_block(proof, previous_hash)

        return redirect(url_for('view_chain'))
    return render_template('create_agreement.html')

@app.route('/chain')
def view_chain():
    return render_template('view_chain.html', chain=blockchain.chain)

# -------------------------------
# Run app
# -------------------------------
if __name__ == '__main__':
    app.run(debug=True)
