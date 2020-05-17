#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "HAL.h"
#include <SoftwareSerial.h>
#include "uvsafe_read.h"
#include "uvsafe_write.h"
#include "uvsafe_comm.h"
#include "uvsafe_rgb_leds.h"

Adafruit_MCP23017 gpio;
SoftwareSerial GUISerial(2, 3); // RX, TX
DataSender SerialDataSender(sensor_state);
RGBLeds LedsIndicadores(mode_manual);
ReadSensors sensors(sensor_state, gpio);

void setup() {
  init_gpio(gpio);
  Serial.begin(115200); //Regular serial port -- Terminal/debug/program
  GUISerial.begin(115200); //Serial port for GUI
  operation_mode = mode_manual;
  }

void loop() {
  // put your main code here, to run repeatedly:
  sensor_state = sensors.read_sensors();
  SerialDataSender.Update(sensor_state);
  chenille_test(gpio);
  LedsIndicadores.Update(operation_mode, sensor_state);
  //sensors.print_sensor_state(sensor_state);
  /*
  // Turn the LED on, then pause
  for (int i=0;i<=6;i++){
    leds[i] = CRGB::Purple;
    }

  for(int i=5;i<=255;i++){
    //leds[i] = CRGB::Purple;
      //leds[i] = CRGB::Black;
      FastLED.show(i);
      delay(10);}

      //leds[3] = CRGB::Black;
  for(int i=255;i>=5;i--){
    //leds[i] = CRGB::Purple;
    FastLED.show(i);
    delay(10);
    }*/
}
