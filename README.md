# ECG-Heart-Beat-Monitor-Using-STM32-and-AD8323

Overview
An application that calculates RPM of heart beat upon collecting ECG data

Using  STM32F103C8 board, AD8323 heart beat sensor, and USB to TTL

ECG data is collected over one minute and used to calculate the RPM.


Architecture
User inputs commands to set the sampling rate, collect data, and report RPM.

Commands are sent over UART from PC to STM32.

According to the received command the STM32 does the required task then it returns to the state of receiving other commands

When Collect command is received, the STM32 sends over UART to the PC the results and the PC receives them.

They are Plotted and converted to a video drawing the samples showing one minute data using pyserial and matplotlib


