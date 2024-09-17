import os
import json
import hashlib
import random
import string

BLOCKS_DIR = './blocks'
DEFAULT_PREV_HASH = "00000000000000000000000000000000"

# Helper function to calculate SHA-256 hash
def calculate_hash(nonce, text, prevHash):
    data = f"{nonce}:{text}:{prevHash}".encode('utf-8')
    return hashlib.sha256(data).hexdigest()

# Helper function to check if the hash has 29 leading zero bits
def hash_meets_difficulty(hash_str, leading_zero_bits=29):
    # Convert hash to binary and check leading zeros
    return bin(int(hash_str, 16))[2:].zfill(256)[:leading_zero_bits] == '0' * leading_zero_bits

# Helper function to generate random names
def generate_name():
    return ''.join(random.choices(string.ascii_uppercase, k=5))

# Helper function to generate random coin amount
def generate_amount():
    return random.randint(1, 100)

# Helper function to get the last block number and its hash
def get_last_block_info():
    files = sorted([f for f in os.listdir(BLOCKS_DIR) if f.startswith("block-") and f.endswith(".txt")])
    
    if not files:
        return 0, DEFAULT_PREV_HASH
    
    last_file = files[-1]
    with open(os.path.join(BLOCKS_DIR, last_file), 'r') as f:
        block_data = json.load(f)
        return int(last_file.split('-')[1].split('.')[0]), block_data['hash']

# Main function to run the infinite loop
def main():
    if not os.path.exists(BLOCKS_DIR):
        os.makedirs(BLOCKS_DIR)
    
    # Initialize block info
    last_block_num, prevHash = get_last_block_info()

    while True:
        # Generate random names and amount
        A = generate_name()
        B = generate_name()
        C = generate_amount()
        text = f"Person {A} is transferring {C} coins to person {B}"

        nonce = 0
        while True:
            if nonce % 1000000 == 0:
                print(f"attempting to mint \"{text}\" with nonce {nonce}")

            # Calculate the hash for this nonce
            hash_str = calculate_hash(nonce, text, prevHash)

            # Check if the hash meets the difficulty condition (48 leading zero bits)
            if hash_meets_difficulty(hash_str):
                # Block information to be saved
                new_block_num = last_block_num + 1
                block_data = {
                    'nonce': nonce,
                    'text': text,
                    'prevHash': prevHash,
                    'hash': hash_str
                }

                # Write the block to a new file
                block_filename = os.path.join(BLOCKS_DIR, f"block-{new_block_num}.txt")
                with open(block_filename, 'w') as block_file:
                    json.dump(block_data, block_file, indent=4)

                # Update prevHash and last_block_num for the next iteration
                prevHash = hash_str
                last_block_num = new_block_num

                print(f"Block {new_block_num} has been mined and saved.")
                break
            
            nonce += 1

if __name__ == "__main__":
    main()
