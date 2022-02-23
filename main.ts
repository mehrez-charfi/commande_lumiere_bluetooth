bluetooth.onBluetoothConnected(function () {
    basic.showLeds(`
        . # # # .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        `)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showLeds(`
        . # # . .
        . # . # .
        . # . # .
        . # . # .
        . # # . .
        `)
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.Hash), function () {
    uart_string = bluetooth.uartReadUntil(serial.delimiters(Delimiters.Hash))
    if (uart_string == "G0") {
        pins.digitalWritePin(DigitalPin.P0, 0)
    }
    if (uart_string == "G1") {
        pins.digitalWritePin(DigitalPin.P0, 1)
    }
    if (uart_string == "O0") {
        pins.digitalWritePin(DigitalPin.P1, 0)
    }
    if (uart_string == "O1") {
        pins.digitalWritePin(DigitalPin.P1, 1)
    }
    if (uart_string == "R0") {
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    if (uart_string == "R1") {
        pins.digitalWritePin(DigitalPin.P2, 1)
    }
    if (uart_string == "ALLUP") {
        pins.digitalWritePin(DigitalPin.P0, 1)
        pins.digitalWritePin(DigitalPin.P1, 1)
        pins.digitalWritePin(DigitalPin.P2, 1)
    }
    if (uart_string == "ALLDOWN") {
        pins.digitalWritePin(DigitalPin.P0, 0)
        pins.digitalWritePin(DigitalPin.P1, 0)
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
})
let uart_string = ""
bluetooth.startUartService()
basic.showIcon(IconNames.Pitchfork)
uart_string = "Null"
