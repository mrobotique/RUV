
#include <FastLED.h>

//Define la posicion del primer led por segmento
const int seg0 = 0;
const int seg1 = 1;
const int seg2 = 2;
const int seg3 = 3;
const int seg4 = 4;
const int seg5 = 5;
const int seg6 = 6;

class RGBLeds{
int current_mode; //Modo en el que se encuentra el uvs
unsigned long previousMillis;
unsigned long data_period = 100;  // tiempo en milisegs

public:
RGBLeds(uvs_mode _current_mode){
  current_mode = _current_mode;
}

public:
  void Update(uvs_mode _current_mode, SENSOR_STRUCT sensors){
    current_mode = _current_mode;
    switch (current_mode) {
      case mode_manual:
          manual_pattern(sensors);
        break;

      case mode_auto:
        //aqui tiene que tener dos modos. primero el de la cuenta regresiva
        //en donde los leds se iluminaran poco a poco y despues
        // el fade in fade out mientras el timer no ha acabado.
        // ver enum timer mode (HAL.h)
        break;

      case mode_test:
        //TBD
        break;

      default:
        //El default es el modo manual... por seguirdad
        break;
    }//case
  }


  void manual_pattern(SENSOR_STRUCT sensors){
    if(sensors.magnetic_1 == 1){
      for(int i=seg0; i<seg1; i++){
        leds[i] = CRGB::Green;
      }
      }
    else{
      for(int i=seg0; i<seg1; i++){
        leds[i] = CRGB::Red;
      }
      }

    if(sensors.magnetic_2 == 1){
      for(int i=seg1; i<seg2; i++){
        leds[i] = CRGB::Green;
      }
      }
    else{
      for(int i=seg1; i<seg2; i++){
        leds[i] = CRGB::Red;
      }
    }

    if(sensors.magnetic_3 == 1){
      for(int i=seg2; i<seg3; i++){
        leds[i] = CRGB::Green;
      }
    }
    else{
      for(int i=seg2; i<seg3; i++){
        leds[i] = CRGB::Red;
      }
    }

    if(sensors.magnetic_4 == 1){
      for(int i=seg3; i<seg4; i++){
        leds[i] = CRGB::Green;
      }
    }
    else{
      for(int i=seg3; i<seg4; i++){
        leds[i] = CRGB::Red;
      }
    }

    if(sensors.magnetic_5 == 1){
      for(int i=seg4; i<seg5; i++){
        leds[i] = CRGB::Green;
      }
    }
    else{
      for(int i=seg4; i<seg5; i++){
        leds[i] = CRGB::Red;
      }
    }

    if(sensors.magnetic_6 == 1){
      for(int i=seg5; i<seg6; i++){
        leds[i] = CRGB::Green;
      }
    }
    else{
      for(int i=seg5; i<seg6; i++){
        leds[i] = CRGB::Red;
      }
    }
    FastLED.show(64);
  }

};
