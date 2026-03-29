import numpy as np
from scipy.io import wavfile
from encryption import encrypt_message

def encode_audio(input_audio, output_audio, secret_msg):
    rate, data = wavfile.read(input_audio)

    data = data.flatten()

    encrypted_msg = encrypt_message(secret_msg)
    binary_msg = ''.join(format(byte, '08b') for byte in encrypted_msg)
    binary_msg += '1111111111111110'

    if len(binary_msg) > len(data):
        raise ValueError("Message too long!")

    for i in range(len(binary_msg)):
        data[i] = (data[i] & ~1) | int(binary_msg[i])

    wavfile.write(output_audio, rate, data)