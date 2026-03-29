from scipy.io import wavfile
from encryption import decrypt_message

def decode_audio(stego_audio):
    rate, data = wavfile.read(stego_audio)

    data = data.flatten()

    binary_data = ''.join(str(i & 1) for i in data)

    end = binary_data.find('1111111111111110')
    binary_msg = binary_data[:end]

    bytes_data = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    encrypted_bytes = bytes([int(b, 2) for b in bytes_data])

    message = decrypt_message(encrypted_bytes)
    return message