/*
 *  by: MRO for IWI
 *  Todos los derechos reservados
 *  Aguascalientes, Mexico. Mayo 2020
 */
#include <avr/wdt.h>
#include <Arduino.h>
#include <SoftwareSerial.h>
#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "HAL.h"
#include "uvsafe_user_definitions.h"
#include "uvsafe_read.h"
#include "uvsafe_write.h"
#include "uvsafe_comm.h"
#include "uvsafe_rgb_leds.h"
#include "uvsafe_safety.h"
#include "uvsafe_user_button.h"
#include "uvsafe_manual.h"
#include "uvsafe_auto.h"
#include "uvsafe_init_test.h"

Adafruit_MCP23017 gpio;
SoftwareSerial GUISerial(2, 3); // RX, TX
DataSender SerialDataSender(sensor_state);
RGBLeds LedsIndicadores(mode_manual); //inicializa siempre en manual
ReadSensors sensors(sensor_state, gpio);

void setup() {
        wdt_disable(); //deshabilitar watchdog para no tener interrupciones
        init_gpio(gpio);
        Serial.begin(115200); //Regular serial port -- Terminal/debug/program
        GUISerial.begin(115200); //Serial port for GUI
        operation_mode = mode_boot;
        activity_led.Update_mode(3);
        auto_button.debounceTime = AUTO_DEBOUNCE;
        if (!digitalRead(AUTO_Pin)) {//Corre el test solo si el boton esta activado
          beeper.Trigger(ONE_BEEP); //Avisa
          while (!digitalRead(AUTO_Pin)) //bloquea el asunto hasta que el boton se suelta
          {
            gpio.digitalWrite(BUZZER,beeper.Update());
          }
          init_test(gpio);
        }
        beeper.Trigger(TWO_BEEP);
        wdt_enable(WDTO_4S);// nunca usar menos de 250 ms si no se va a resetar sin control
}


void loop() {
        wdt_reset(); //ping al watchdog
        sensor_state = sensors.read_sensors(operation_mode);
        SerialDataSender.Update(sensor_state);
        LedsIndicadores.Update(operation_mode, sensor_state);
        user_button_update(LedsIndicadores, gpio);
        safety_functions();
        lamparas_manual(gpio);
        lamparas_auto(gpio);
        activity_led.Update();
        gpio.digitalWrite(BUZZER,beeper.Update());
}
