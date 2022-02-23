def on_bluetooth_connected():
    basic.show_leds("""
        . # # # .
                . # . . .
                . # . . .
                . # . . .
                . # # # .
    """)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_leds("""
        . # # . .
                . # . # .
                . # . # .
                . # . # .
                . # # . .
    """)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_uart_data_received():
    global uart_string
    uart_string = bluetooth.uart_read_until(serial.delimiters(Delimiters.HASH))
    if uart_string == "G0":
        pins.digital_write_pin(DigitalPin.P0, 0)
    if uart_string == "G1":
        pins.digital_write_pin(DigitalPin.P0, 1)
    if uart_string == "O0":
        pins.digital_write_pin(DigitalPin.P1, 0)
    if uart_string == "O1":
        pins.digital_write_pin(DigitalPin.P1, 1)
    if uart_string == "R0":
        pins.digital_write_pin(DigitalPin.P2, 0)
    if uart_string == "R1":
        pins.digital_write_pin(DigitalPin.P2, 1)
    if uart_string == "ALLUP":
        pins.digital_write_pin(DigitalPin.P0, 1)
        pins.digital_write_pin(DigitalPin.P1, 1)
        pins.digital_write_pin(DigitalPin.P2, 1)
    if uart_string == "ALLDOWN":
        pins.digital_write_pin(DigitalPin.P0, 0)
        pins.digital_write_pin(DigitalPin.P1, 0)
        pins.digital_write_pin(DigitalPin.P2, 0)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.HASH), on_uart_data_received)

uart_string = ""
bluetooth.start_uart_service()
basic.show_icon(IconNames.PITCHFORK)
uart_string = "Null"