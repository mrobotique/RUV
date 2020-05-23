/*
*  by: MRO for IWI
*  Todos los derechos reservados
*  Aguascalientes, Mexico. Mayo 2020
*/


#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "HAL.h"
#include <SoftwareSerial.h>
#include "uvsafe_read.h"
#include "uvsafe_write.h"
#include "uvsafe_comm.h"
#include "uvsafe_rgb_leds.h"
#include "uvsafe_safety.h"
#include "uvsafe_user_button.h"
#include "uvsafe_manual.h"
#include "uvsafe_time.h"

Adafruit_MCP23017 gpio;
SoftwareSerial GUISerial(2, 3); // RX, TX
DataSender SerialDataSender(sensor_state);
RGBLeds LedsIndicadores(mode_manual); //inicializa siempre en manual
ReadSensors sensors(sensor_state, gpio);

void testt (void);

Countdown timerk(10, testt);




void setup() {
  init_gpio(gpio);
  Serial.begin(115200); //Regular serial port -- Terminal/debug/program
  GUISerial.begin(115200); //Serial port for GUI
  operation_mode = mode_manual;
    timerk.start();

  }



void loop() {
  // put your main code here, to run repeatedly:
  sensor_state = sensors.read_sensors();
  //SerialDataSender.Update(sensor_state);
  //chenille_test(gpio);
  LedsIndicadores.Update(operation_mode, sensor_state);
  user_button_update(LedsIndicadores);
  safety_functions();
  lamparas_manual(gpio);
  delay(10); //Para no atascar el pueto serie

  if ((sensor_state.pir_1 == 0) and (timerk.is_running())){
    timerk.pause();
  }
  else if (timerk.is_running()) {
    timerk.start();
  }
  timerk.run();

}

void testt (void){
  Serial.println("*****");
}
