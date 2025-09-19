def concat_glyphs(g1, g2, g3):
    temp = []
    for i, j, k in zip(g1, g2, g3):
        temp.extend([i, j, k])
    return temp


r_glyphs = {
    'C_reg': bytearray([0x3C, 0x66, 0x60, 0x60, 0x60, 0x66, 0x3C, 0x00]),
    'D_reg': bytearray([0x78, 0x6C, 0x66, 0x66, 0x66, 0x6C, 0x78, 0x00]),
    'E_reg': bytearray([0x7E, 0x60, 0x60, 0x78, 0x60, 0x60, 0x7E, 0x00]),
    'H_reg': bytearray([0x66, 0x66, 0x66, 0x7E, 0x66, 0x66, 0x66, 0x00]),
    'X_reg': bytearray([0x66, 0x66, 0x3C, 0x18, 0x3C, 0x66, 0x66, 0x00]),
    'B_reg': bytearray([0x7C, 0x66, 0x66, 0x7C, 0x66, 0x66, 0x7C, 0x00]),
    'I_reg': bytearray([0x3C, 0x18, 0x18, 0x18, 0x18, 0x18, 0x3C, 0x00]),
    'N_reg': bytearray([0x66, 0x76, 0x7E, 0x7E, 0x6E, 0x66, 0x66, 0x00])
}

i_glyphs ={
    'C_inv': bytearray([x ^ 0xff for x in r_glyphs['C_reg']]),
    'D_inv': bytearray([x ^ 0xff for x in r_glyphs['D_reg']]),
    'E_inv': bytearray([x ^ 0xff for x in r_glyphs['E_reg']]),
    'H_inv': bytearray([x ^ 0xff for x in r_glyphs['H_reg']]),
    'X_inv': bytearray([x ^ 0xff for x in r_glyphs['X_reg']]),
    'B_inv': bytearray([x ^ 0xff for x in r_glyphs['B_reg']]),
    'I_inv': bytearray([x ^ 0xff for x in r_glyphs['I_reg']]),
    'N_inv': bytearray([x ^ 0xff for x in r_glyphs['N_reg']]),
}

c_glyphs = {
    'DEC_INV': bytearray(concat_glyphs(i_glyphs['D_inv'], i_glyphs['E_inv'], i_glyphs['C_inv'])),
    'HEX_INV': bytearray(concat_glyphs(i_glyphs['H_inv'], i_glyphs['E_inv'], i_glyphs['X_inv'])),
    'BIN_INV': bytearray(concat_glyphs(i_glyphs['B_inv'], i_glyphs['I_inv'], i_glyphs['N_inv'])),
}




