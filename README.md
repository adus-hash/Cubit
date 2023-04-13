# Cubit
Cubit is a python console app for my imaginary cryptocurrency. I've made this project because i wanted to know how cryptocurrency works and also implement basics concepts
like digital signature, SHA256, RSA cipher, blockchain..., firstly each Client need an ID, ID is a 5 letter string, through this ID you can log in to your account or send/recieve payments, and program generate_ids.py will generate 11 881 376 IDs (from 'aaaaa' to 'zzzzz') saved in .txt file, after each new Client will be created, fisrt ID from this file will be assigned to this Client and deleted from .txt file (because this ID is not free anymore)

## Client
Client is a .txt file which contains:

- name - name is a md5 hash of "VekJe" + age_of_user
- amount of Cubits
- private key for RSA
- public key for RSA
- 0/1 - is miner or not

But Client.py contains these functions:

- prime_nums() - uses Sieve of Eratosthenes to find prime numbers between 1-300, return an array of prime nums

- nsd(a, b) - greatest common factor, uses Euclid's algorithm, return GCF of two nums

- choose_e(N) - random num between N / 3 and N / 2, return this num if GCF(num, N) == 1

- create_inverse(e, N) - returns the inverse of e in modulo N

- encoding(plain_text, public_key) - every letter for plain text is encrypted with this formula ascii(i) ** e mod N where public key is (e, N)

- decoding(cipher_text, private_key) - every letter for cipher text is dencrypted with this formula ascii(j) ** d mod N where private key is (d, N)

- new_client() - for every new client you need to calculace public and private key, firstly you pick two random prime nums, then you multiply then to create your modulo N then you run choose_e(N) you've just created public_key, after that you run create_inverse(e, N) and that create private key, then every information you write to Clients .txt file

- get_ID() - returns first ID from .txt file and removes it from that file

- make_transaction(sender_id, recipient_id, amount, private_key) - encoding(sha256(sender_ID + amount + recipient_ID, private_key)), returns non-encrypted and encrypted transaction # transaction look like this 'aaaaa0003aaaab', User 'aaaaa' is sending 3 Cubits to User 'aaaab'

- verification(original_transaction, encoded_transaction, public_key) - for the transaction to take place, the receiver must match the digest and the decrypted transaction. You as a reciever you get digest and encrypted digest (encrypted with sender private key), what you do with this is, firstly decrypt encrypted messeg with sender public key and if that matches with digest transaction take a place.
