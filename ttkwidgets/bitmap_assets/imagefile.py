imagefile = """
#define imagefile_width 16
#define imagefile_height 16
static unsigned char imagefile_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x22, 0x4c, 0x72, 0x52,
   0xfa, 0x52, 0x02, 0x4c, 0x02, 0x40, 0xfa, 0x40, 0x8a, 0x40, 0xfa, 0x40,
   0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };
"""

{varname}_mask = """
#define imagefile_mask_width 16
#define imagefile_mask_height 16
static unsigned char imagefile_mask_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x22, 0x4c, 0x72, 0x52,
   0xfa, 0x52, 0x02, 0x4c, 0x02, 0x40, 0xfa, 0x40, 0x8a, 0x40, 0xfa, 0x40,
   0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };
"""