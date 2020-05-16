#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "HAL.h"
#include <FastLED.h>
#include <SoftwareSerial.h>
#include "uvsafe_read.h"
#include "uvsafe_write.h"
#include "uvsafe_comm.h"

Adafruit_MCP23017 gpio;
SoftwareSerial GUISerial(2, 3); // RX, TX

void setup() {
  init_gpio(gpio);
  Serial.begin(115200); //Regular serial port -- Terminal/debug/program
  GUISerial.begin(115200); //Serial port for GUI
  }

void loop() {
  // put your main code here, to run repeatedly:
  sensor_state = read_sensors(sensor_state, gpio);
  chenille_test(gpio);
  //print_sensor_state(sensor_state);
  send_data(sensor_state);
  delay(100);/*
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
