## So quick note I have 6 Coloumns and 4 rows
## and ig thats it.I cant anyhting else to warn yall about so.
import board
from kmk.handlers.sequences import send_string
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKKeyboard
from kmk.modukles.encoder import EncoderHandler
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType

senweget = KMKeyboard()
senweget.name = "Senweget"
senweget.manufacture = "Hack Club Phantom"

layers = Layers()
holdtap = Holdtap()
encoder_Handler = EncoderHandler()
senweget.modlues.extend([Layers, holdtap, encoder_handler])

split = Split(
    split_type = SplitType.UART,
    data_pin = board.GP5  ## TRS Pin 
    split_flip = True,
)
senweget.modules.append(split)

senweget.modules.col_pins = (
    board.GP1, #col1
    board.GP2, #col2
    board.GP3, #col3
    board.GP4, #col4
    board.GP5, #col5
    board.GP6, #col6
)
senweget.modules.row_pins = (
    board.GP7,  #row1
    board.GP26, #row2
    board.GP27, #row3
    board.GP28, #row4
)
senweget.modules.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP29, board.GP8,board.GP14),)  # Encoder pins

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE),), # Layer 0:Volume control 
    ((KC.MS_WH_UP, KC.MS_WH_DN, KC.TRNS),), # Layer 1: SCROLL
    ((KC.BRID, KC.BRIU, KC.TRNS),), # Layer 2: BRIGHTNESS
]

LOWER = KC.MO(1)
RAISE = KC.MO(2)

senweget.keymap = [
   
    # Layer 0 QWERTY
   [
     # ROW 1
     KC.TAB, 
     KC.Q,
     KC.W,
     KC.E,
     KC.R,
     KC.T,
     KC.Y,
      #ROW 2
     KC.LCTRL,
     KC.A,
     KC.S,
     KC.D,
     KC.F,
     KC.G,
        # ROW 3
     KC.LSHIFT,
     KC.Z,
     KC.X,
     KC.C,
     KC.V,
     KC.B,
        # ROW 4 
     KC.LGUI,
     LOWER,
     KC.SPC,
   ],
]
if __name__ == "__main__":
    senweget.go()
