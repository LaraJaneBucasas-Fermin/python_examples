from Oven import Oven
from Air_conditioning import Air_conditioning
from waterDispenser import WaterDispenser

Oven1 = Oven("Samsung", 12, "Applepie")
Air_conditioning1 = Air_conditioning("Epson", "frE34", 21)
waterDispenser1 = WaterDispenser("Everest", 42, 75)

Oven1.bake()
Oven1.clean()
Air_conditioning1.set_temperature()
Air_conditioning1.turn_on()
waterDispenser1.dispense_cold_water()
waterDispenser1.dispense_hot_water()
