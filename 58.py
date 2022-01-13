def rgb(r, g, b):
    hex_r = hex_g = hex_b = ''
    if r < 0:
        hex_r = '0x0'
    if r > 255:
        hex_r = '0xFF'
    if 0 < r <= 255:
        hex_r = hex(r)
    if g < 0:
        hex_g = '0x0'
    if g > 255:
        hex_g = '0xFF'
    if 0 < g <= 255:
        hex_g = hex(g)
    if b < 0:
        hex_b = '0x0'
    if b > 255:
        hex_b = '0xFF'
    if 0 < b <= 255:
        hex_b = hex(b)
    return (hex_r[2:].zfill(2) + hex_g[2:].zfill(2) + hex_b[2:].zfill(2)).upper()


print(rgb(0,0,0))
