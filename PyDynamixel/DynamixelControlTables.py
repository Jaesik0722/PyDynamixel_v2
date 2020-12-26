"""
This file contains the classes for the control tables of the dynamixel
motors. 
"""
# Dynamixel MX-28T/R/AT/AR for Protocol 1.0
class MX_P1:
    # Addresses
    ADDR_MODEL_NUMBER = 0
    ADDR_FIRMWARE_VERSION = 2
    ADDR_ID = 3
    ADDR_BAUD_RATE = 4
    ADDR_RETURN_DELAY_TIME = 5
    ADDR_CW_ANGLE_LIMIT = 6
    ADDR_CCW_ANGLE_LIMIT = 8
    ADDR_TEMPERATURE_LIMIT = 11
    ADDR_MIN_VOLTAGE_LIMIT = 12
    ADDR_MAX_VOLTAGE_LIMIT = 13
    ADDR_MAX_TORQUE = 14
    ADDR_STATUS_RETURN_LEVEL = 16
    ADDR_ALARM_LED = 17
    ADDR_SHUTDOWN = 18
    ADDR_MULTI_TURN_OFFSET = 20
    ADDR_RESOLUTION_DIVIDER = 22
    ADDR_TORQUE_ENABLE = 24
    ADDR_LED = 25
    ADDR_D_GAIN = 26
    ADDR_I_GAIN = 27
    ADDR_P_GAIN = 28
    ADDR_GOAL_POSITION = 30
    ADDR_MOVING_SPEED = 32
    ADDR_TORQUE_LIMIT = 34
    ADDR_PRESENT_POSITION = 36
    ADDR_PRESENT_SPEED = 38
    ADDR_PRESENT_LOAD = 40
    ADDR_PRESENT_VOLTAGE = 42
    ADDR_PRESENT_TEMPERATURE = 43
    ADDR_REGISTERED = 44
    ADDR_MOVING = 46
    ADDR_LOCK = 47
    ADDR_PUNCH = 48
    ADDR_REALTIME_TICK = 50
    ADDR_GOAL_ACCELERATION = 73
    # Lengths (in bytes)
    LEN_MODEL_NUMBER = 2
    LEN_FIRMWARE_VERSION = 1
    LEN_ID = 1
    LEN_BAUD_RATE = 1
    LEN_RETURN_DELAY_TIME = 1
    LEN_CW_ANGLE_LIMIT = 2
    LEN_CCW_ANGLE_LIMIT = 2
    LEN_TEMPERATURE_LIMIT = 1
    LEN_MIN_VOLTAGE_LIMIT = 1
    LEN_MAX_VOLTAGE_LIMIT = 1
    LEN_MAX_TORQUE = 2
    LEN_STATUS_RETURN_LEVEL = 1
    LEN_ALARM_LED = 1
    LEN_SHUTDOWN = 1
    LEN_MULTI_TURN_OFFSET = 2
    LEN_RESOLUTION_DIVIDER = 1
    LEN_TORQUE_ENABLE = 1
    LEN_LED = 1
    LEN_D_GAIN = 1
    LEN_I_GAIN = 1
    LEN_P_GAIN = 1
    LEN_GOAL_POSITION = 2
    LEN_MOVING_SPEED = 2
    LEN_TORQUE_LIMIT = 2
    LEN_PRESENT_POSITION = 2
    LEN_PRESENT_SPEED = 2
    LEN_PRESENT_LOAD = 2
    LEN_PRESENT_VOLTAGE = 1
    LEN_PRESENT_TEMPERATURE = 1
    LEN_REGISTERED = 1
    LEN_MOVING = 1
    LEN_LOCK = 1
    LEN_PUNCH = 2
    LEN_REALTIME_TICK = 2
    LEN_GOAL_ACCELERATION = 1

# Dynamixel MX-28T/R/AT/AR for Protocol 2.0
class MX_P2:
    # Addresses
    ADDR_MODEL_NUMBER = 0
    ADDR_MODEL_INFORMATION = 2
    ADDR_FIRMWARE_VERSION = 6
    ADDR_ID = 7
    ADDR_BAUD_RATE = 8
    ADDR_RETURN_DELAY_TIME = 9
    ADDR_DRIVE_MODE = 10
    ADDR_OPERATING_MODE = 11
    ADDR_SECONDARY_ID = 12
    ADDR_PROTOCOL_TYPE = 13
    ADDR_HOMING_OFFSET = 20
    ADDR_MOVING_THRESHOLD = 24
    ADDR_TEMPERATURE_LIMIT = 31
    ADDR_MAX_VOLTAGE_LIMIT = 32
    ADDR_MIN_VOLTAGE_LIMIT = 34
    ADDR_PWM_LIMIT = 36
    ADDR_ACCELERATION_LIMIT = 40
    ADDR_VELOCITY_LIMIT = 44
    ADDR_MAX_POSITION_LIMIT = 48
    ADDR_MIN_POSITION_LIMIT = 52
    ADDR_SHUTDOWN = 63
    ADDR_TORQUE_ENABLE = 64
    ADDR_LED = 65
    ADDR_STATUS_RETURN_LEVEL = 68
    ADDR_REGISTERED = 69
    ADDR_HARDWARE_ERROR_STATUS = 70
    ADDR_VELOCITY_I_GAIN = 76
    ADDR_VELOCITY_P_GAIN = 78
    ADDR_POSITION_D_GAIN = 80
    ADDR_POSITION_I_GAIN = 82
    ADDR_POSITION_P_GAIN = 84
    ADDR_FEEDROWARD_2_GAIN = 88
    ADDR_FEEDFORWARD_1_GAIN = 90
    ADDR_BUS_WATCHDOG = 98
    ADDR_GOAL_PWM = 100
    ADDR_GOAL_VELOCITY = 104
    ADDR_PROFILE_ACCELERATION = 108
    ADDR_PROFILE_VELOCITY = 112
    ADDR_GOAL_POSITION = 116
    ADDR_REALTIME_TICK = 120
    ADDR_MOVING = 122
    ADDR_MOVING_STATUS = 123
    ADDR_PRESENT_PWM = 124
    ADDR_PRESENT_LOAD = 126
    ADDR_PRESENT_VELOCITY = 128
    ADDR_PRESENT_POSITION = 132
    ADDR_VELOCITY_TRAJECTORY = 136
    ADDR_POSITION_TRAJECTORY = 140
    ADDR_PRESENT_INPUT_VOLTAGE = 144
    ADDR_PRESENT_TEMPERATURE = 146
    # Lengths (in bytes)
    LEN_MODEL_NUMBER = 2
    LEN_MODEL_INFORMATION = 4
    LEN_FIRMWARE_VERSION = 1
    LEN_ID = 1
    LEN_BAUD_RATE = 1
    LEN_RETURN_DELAY_TIME = 1
    LEN_DRIVE_MODE = 1
    LEN_OPERATING_MODE = 1
    LEN_SECONDARY_ID = 1
    LEN_PROTOCOL_TYPE = 1
    LEN_HOMING_OFFSET = 4
    LEN_MOVING_THRESHOLD = 4
    LEN_TEMPERATURE_LIMIT = 1
    LEN_MAX_VOLTAGE_LIMIT = 2
    LEN_MIN_VOLTAGE_LIMIT = 2
    LEN_PWM_LIMIT = 2
    LEN_ACCELERATION_LIMIT = 4
    LEN_VELOCITY_LIMIT = 4
    LEN_MAX_POSITION_LIMIT = 4
    LEN_MIN_POSITION_LIMIT = 4
    LEN_SHUTDOWN = 1
    LEN_TORQUE_ENABLE = 1
    LEN_LED = 1
    LEN_STATUS_RETURN_LEVEL = 1
    LEN_REGISTERED = 1
    LEN_HARDWARE_ERROR_STATUS = 1
    LEN_VELOCITY_I_GAIN = 2
    LEN_VELOCITY_P_GAIN = 2
    LEN_POSITION_D_GAIN = 2
    LEN_POSITION_I_GAIN = 2
    LEN_POSITION_P_GAIN = 2
    LEN_FEEDROWARD_2_GAIN = 2
    LEN_FEEDFORWARD_1_GAIN = 2
    LEN_BUS_WATCHDOG = 1
    LEN_GOAL_PWM = 2
    LEN_GOAL_VELOCITY = 4
    LEN_PROFILE_ACCELERATION = 4
    LEN_PROFILE_VELOCITY = 4
    LEN_GOAL_POSITION = 4
    LEN_REALTIME_TICK = 2
    LEN_MOVING = 1
    LEN_MOVING_STATUS = 1
    LEN_PRESENT_PWM = 2
    LEN_PRESENT_LOAD = 2
    LEN_PRESENT_VELOCITY = 4
    LEN_PRESENT_POSITION = 4
    LEN_VELOCITY_TRAJECTORY = 4
    LEN_POSITION_TRAJECTORY = 4
    LEN_PRESENT_INPUT_VOLTAGE = 2
    LEN_PRESENT_TEMPERATURE = 1

# Seed Robotics RH8D for Protocol 1.0
class RH8D_P1:
    # Addresses
    ADDR_MODEL_NUMBER = 0
    ADDR_FIRMWARE_VERSION = 2
    ADDR_ID = 3
    ADDR_BAUD_RATE = 4
    ADDR_RETURN_DELAY_TIME = 5
    ADDR_CW_ANGLE_LIMIT = 6
    ADDR_CCW_ANGLE_LIMIT = 8
    ADDR_STATUS_RETURN_LEVEL = 16
    ADDR_SHUTDOWN = 18
    ADDR_EMULATE_12_BIT = 20 
    ADDR_ZERO_OFFSET = 21
    ADDR_PZR_LOCK = 23
    ADDR_TORQUE_ENABLE = 24
    ADDR_D_GAIN = 26
    ADDR_I_GAIN = 27
    ADDR_P_GAIN = 28
    ADDR_GOAL_POSITION = 30
    ADDR_MOVING_SPEED = 32
    ADDR_PRESENT_POSITION = 36
    ADDR_PRESENT_SPEED = 38
    ADDR_PRESENT_TEMPERATURE = 43
    ADDR_MOVING = 46
    ADDR_BOOT_PASS_LENGTH = 81
    ADDR_BOOT_FIRST_CH = 82
    ADDR_BOOT_TIMEOUT = 85
    ADDR_UART_FRAME_ERROR_COUNT = 87
    ADDR_UART_PROC_BUFFER_OVERFLOW_COUNT = 88
    ADDR_UART_FIRM_BUFFER_OVERFLOW_COUNT = 89
    ADDR_CONTROL_MODE = 90
    ADDR_PWM = 92
    # Lengths (in bytes)
    LEN_MODEL_NUMBER = 2
    LEN_FIRMWARE_VERSION = 1
    LEN_ID = 1
    LEN_BAUD_RATE = 1
    LEN_RETURN_DELAY_TIME = 1
    LEN_CW_ANGLE_LIMIT = 2
    LEN_CCW_ANGLE_LIMIT = 2
    LEN_STATUS_RETURN_LEVEL = 1
    LEN_SHUTDOWN = 1
    LEN_EMULATE_12_BIT = 21
    LEN_ZERO_OFFSET = 2
    LEN_PZR_LOCK = 1
    LEN_TORQUE_ENABLE = 1
    LEN_D_GAIN = 1
    LEN_I_GAIN = 1
    LEN_P_GAIN = 1
    LEN_GOAL_POSITION = 2
    LEN_MOVING_SPEED = 2
    LEN_PRESENT_POSITION = 2
    LEN_PRESENT_SPEED = 2
    LEN_PRESENT_TEMPERATURE = 1
    LEN_MOVING = 1
    LEN_BOOT_PASS_LENGTH = 1
    LEN_BOOT_FIRST_CH = 1
    LEN_BOOT_TIMEOUT = 1
    LEN_UART_FRAME_ERROR_COUNT = 1
    LEN_UART_PROC_BUFFER_OVERFLOW_COUNT = 1
    LEN_UART_FIRM_BUFFER_OVERFLOW_COUNT = 1
    LEN_CONTROL_MODE = 1
    LEN_PWM = 2

# Dynamixel X Series for Protocol 2.0
class X_SERIES:
    # Addresses
    ADDR_MODEL_NUMBER = 0
    ADDR_MODEL_INFORMATION = 2
    ADDR_FIRMWARE_VERSION = 6
    ADDR_ID = 7
    ADDR_BAUD_RATE = 8
    ADDR_RETURN_DELAY_TIME = 9
    ADDR_DRIVE_MODE = 10
    ADDR_OPERATING_MODE = 11
    ADDR_SECONDARY_ID = 12
    ADDR_PROTOCOL_TYPE = 13
    ADDR_HOMING_OFFSET = 20
    ADDR_MOVING_THRESHOLD = 24
    ADDR_TEMPERATURE_LIMIT = 31
    ADDR_MAX_VOLTAGE_LIMIT = 32
    ADDR_MIN_VOLTAGE_LIMIT = 34
    ADDR_PWM_LIMIT = 36
    ADDR_CURRENT_LIMIT = 38
    #ADDR_ACCELERATION_LIMIT = 40
    ADDR_VELOCITY_LIMIT = 44
    ADDR_MAX_POSITION_LIMIT = 48
    ADDR_MIN_POSITION_LIMIT = 52
    ADDR_EXTERNAL_PORT_MODE_1 = 56
    ADDR_EXTERNAL_PORT_MODE_2 = 57
    ADDR_EXTERNAL_PORT_MODE_3 = 58
    ADDR_SHUTDOWN = 63
    ADDR_TORQUE_ENABLE = 64
    ADDR_LED = 65
    ADDR_STATUS_RETURN_LEVEL = 68
    ADDR_REGISTERED = 69
    ADDR_HARDWARE_ERROR_STATUS = 70
    ADDR_VELOCITY_I_GAIN = 76
    ADDR_VELOCITY_P_GAIN = 78
    ADDR_POSITION_D_GAIN = 80
    ADDR_POSITION_I_GAIN = 82
    ADDR_POSITION_P_GAIN = 84
    ADDR_FEEDROWARD_2_GAIN = 88
    ADDR_FEEDFORWARD_1_GAIN = 90
    ADDR_BUS_WATCHDOG = 98
    ADDR_GOAL_PWM = 100
    ADDR_GOAL_CURRENT = 102
    ADDR_GOAL_VELOCITY = 104
    ADDR_PROFILE_ACCELERATION = 108
    ADDR_PROFILE_VELOCITY = 112
    ADDR_GOAL_POSITION = 116
    ADDR_REALTIME_TICK = 120
    ADDR_MOVING = 122
    ADDR_MOVING_STATUS = 123
    ADDR_PRESENT_PWM = 124
    ADDR_PRESENT_CURRENT = 126
    ADDR_PRESENT_VELOCITY = 128
    ADDR_PRESENT_POSITION = 132
    ADDR_VELOCITY_TRAJECTORY = 136
    ADDR_POSITION_TRAJECTORY = 140
    ADDR_PRESENT_INPUT_VOLTAGE = 144
    ADDR_PRESENT_TEMPERATURE = 146
    # Lengths (in bytes)
    LEN_MODEL_NUMBER = 2
    LEN_MODEL_INFORMATION = 4
    LEN_FIRMWARE_VERSION = 1
    LEN_ID = 1
    LEN_BAUD_RATE = 1
    LEN_RETURN_DELAY_TIME = 1
    LEN_DRIVE_MODE = 1
    LEN_OPERATING_MODE = 1
    LEN_SECONDARY_ID = 1
    LEN_PROTOCOL_TYPE = 1
    LEN_HOMING_OFFSET = 4
    LEN_MOVING_THRESHOLD = 4
    LEN_TEMPERATURE_LIMIT = 1
    LEN_MAX_VOLTAGE_LIMIT = 2
    LEN_MIN_VOLTAGE_LIMIT = 2
    LEN_PWM_LIMIT = 2
    LEN_CURRENT_LIMIT = 2
    #LEN_ACCELERATION_LIMIT = 4
    LEN_VELOCITY_LIMIT = 4
    LEN_MAX_POSITION_LIMIT = 4
    LEN_MIN_POSITION_LIMIT = 4
    LEN_EXTERNAL_PORT_MODE_1 = 1
    LEN_EXTERNAL_PORT_MODE_2 = 1
    LEN_EXTERNAL_PORT_MODE_3 = 1
    LEN_SHUTDOWN = 1
    LEN_TORQUE_ENABLE = 1
    LEN_LED = 1
    LEN_STATUS_RETURN_LEVEL = 1
    LEN_REGISTERED = 1
    LEN_HARDWARE_ERROR_STATUS = 1
    LEN_VELOCITY_I_GAIN = 2
    LEN_VELOCITY_P_GAIN = 2
    LEN_POSITION_D_GAIN = 2
    LEN_POSITION_I_GAIN = 2
    LEN_POSITION_P_GAIN = 2
    LEN_FEEDROWARD_2_GAIN = 2
    LEN_FEEDFORWARD_1_GAIN = 2
    LEN_BUS_WATCHDOG = 1
    LEN_GOAL_PWM = 2
    LEN_GOAL_CURRENT = 2
    LEN_GOAL_VELOCITY = 4
    LEN_PROFILE_ACCELERATION = 4
    LEN_PROFILE_VELOCITY = 4
    LEN_GOAL_POSITION = 4
    LEN_REALTIME_TICK = 2
    LEN_MOVING = 1
    LEN_MOVING_STATUS = 1
    LEN_PRESENT_PWM = 2
    LEN_PRESENT_CURRENT = 2
    LEN_PRESENT_VELOCITY = 4
    LEN_PRESENT_POSITION = 4
    LEN_VELOCITY_TRAJECTORY = 4
    LEN_POSITION_TRAJECTORY = 4
    LEN_PRESENT_INPUT_VOLTAGE = 2
    LEN_PRESENT_TEMPERATURE = 1

ctrltables_str_mappings = {"MX-P1": MX_P1, "MX-P2": MX_P2, "RH8D-P1": RH8D_P1, "X-SERIES": X_SERIES}
