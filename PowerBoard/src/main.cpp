#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_MCP23017.h"
#include "../lib/HAL.h"
#include <FastLED.h>
#include <SoftwareSerial.h>

Adafruit_MCP23017 gpio;
SoftwareSerial GUISerial(2, 3); // RX, TX

void setup() {
  init_gpio(gpio);
  Serial.begin(115200); //Regular serial port -- Terminal/debug/program
  GUISerial.begin(9600); //Serial port for GUI
  }

void loop() {
  // put your main code here, to run repeatedly:
  gpio.digitalWrite(0,gpio.digitalRead(MAGNETIC1));
  delay(100);
  // Turn the LED on, then pause
  for(int i=0;i<=6;i++){
    //leds[i] = CRGB::Purple;
      leds[i] = CRGB::Black;
      FastLED.show(BRIGHTNESS);
      delay(100);}

      //leds[3] = CRGB::Black;
  for(int i=5;i>=0;i--){
    leds[i] = CRGB::DarkBlue;
    FastLED.show(BRIGHTNESS);
    delay(100);
    }

}
