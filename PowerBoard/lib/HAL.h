/*** HAL file
HAL: Hardware Abstraction Layer
by: MRO for IWI
Todos los derechos reservados
Aguascalientes, Mexico. Mayo 2020***/

#include "Adafruit_MCP23017.h"
#include <Arduino.h>
#include "FastLED.h"

//LED TypicalLEDStrip
#define LED_PIN     7
#define NUM_LEDS    6
#define BRIGHTNESS  64
CRGB leds[NUM_LEDS]; //Instance

//PIR sensors. Connected directly to the Arduino board
//D10 to D13
#define PIR1_Pin 10
#define PIR2_Pin 11
#define PIR3_Pin 12
#define PIR4_Pin 13
//Deadman switch
#define DEADMAN_Pin 7

//Relay outputs
//Connected to the MCP23017
//GPA0 to GPA7
#define LAMP1 0
#define LAMP2 1
#define LAMP3 2
#define LAMP4 3
#define LAMP5 4
#define LAMP6 5
#define LAMP7 6
#define LAMP8 7

//Magnetic sensors inputs
#define MAGNETIC1 8
#define MAGNETIC2 9
#define MAGNETIC3 10
#define MAGNETIC4 11
#define MAGNETIC5 12
#define MAGNETIC6 13

//Struct Sensores
struct SENSOR_STRUCT{
  int deadman_sw;
  int pir_1;
  int pir_2;
  int pir_3;
  int pir_4;
  int magnetic_1;
  int magnetic_2;
  int magnetic_3;
  int magnetic_4;
  int magnetic_5;
  int magnetic_6;
  int lamp_1; //It is possible to read the output status.
  int lamp_2; //So, lets read the lamps staus
  int lamp_3;
  int lamp_4;
  int lamp_5;
  int lamp_6;
  int lamp_7;
  int lamp_8;
};

//Struct outputs
struct LAMP_STRUCT{
  int lamp_1;
  int lamp_2;
  int lamp_3;
  int lamp_4;
  int lamp_5;
  int lamp_6;
  int lamp_7;
  int lamp_8;
};

//Prototypes
void init_gpio(Adafruit_MCP23017 gpio);

/**** Operational Functions ****/
void init_gpio(Adafruit_MCP23017 gpio){
//Init gpio
//Outputs
gpio.begin();      // use default address 0
gpio.pinMode(LAMP1, OUTPUT);
gpio.pinMode(LAMP2, OUTPUT);
gpio.pinMode(LAMP3, OUTPUT);
gpio.pinMode(LAMP4, OUTPUT);
gpio.pinMode(LAMP5, OUTPUT);
gpio.pinMode(LAMP6, OUTPUT);
gpio.pinMode(LAMP7, OUTPUT);
gpio.pinMode(LAMP8, OUTPUT);
//Inputs
gpio.pinMode(MAGNETIC1, INPUT);
gpio.pullUp(MAGNETIC1, HIGH);  // turn on a 100K pullup internally
gpio.pinMode(MAGNETIC2, INPUT);
gpio.pullUp(MAGNETIC2, HIGH);  // turn on a 100K pullup internally
gpio.pinMode(MAGNETIC3, INPUT);
gpio.pullUp(MAGNETIC3, HIGH);  // turn on a 100K pullup internally
gpio.pinMode(MAGNETIC4, INPUT);
gpio.pullUp(MAGNETIC4, HIGH);  // turn on a 100K pullup internally
gpio.pinMode(MAGNETIC5, INPUT);
gpio.pullUp(MAGNETIC5, HIGH);  // turn on a 100K pullup internally
gpio.pinMode(MAGNETIC6, INPUT);
gpio.pullUp(MAGNETIC6, HIGH);  // turn on a 100K pullup internally

//Now the Microcontroller Inputs
pinMode(PIR1_Pin, INPUT_PULLUP);
pinMode(PIR2_Pin, INPUT_PULLUP);
pinMode(PIR3_Pin, INPUT_PULLUP);
pinMode(PIR4_Pin, INPUT_PULLUP);
pinMode(DEADMAN_Pin, INPUT_PULLUP);
//Microcontroller outputs
//Outputs for future applications

//LED Strip  WS2812B
FastLED.addLeds<WS2812B,LED_PIN,EOrder::GRB>(leds, NUM_LEDS);

}
