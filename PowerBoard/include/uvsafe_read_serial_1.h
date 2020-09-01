/*
 *  by: MRO for UVSA GROUP
 *  Todos los derechos reservados
 *  Winnipeg, Manitoba. Canada. Julio 2020
 */

//const size_t capacity = JSON_OBJECT_SIZE(1) + JSON_SERIAL1_BUFFER_SIZE + 1; //JSON_SERIAL1_BUFFER_SIZE definido en HAL.h
const size_t capacity = 2*JSON_ARRAY_SIZE(2) + JSON_OBJECT_SIZE(2) + 20;
DynamicJsonDocument doc(capacity);

void serialEvent() {
  while (Serial.available()) {
    // recibe el primer byte:
    char inChar = (char)Serial.read();
    // Lo agrega al string:
    if (int(inChar) != 0){
       inputString += inChar; //Descarta un caracter nulo que envia el bt
    }
    // Si el caracter que llega es "newline" (\n) 
    // el string esta completo y hacemos algo con el.
    if (inChar == '\n') {
      DeserializationError error = deserializeJson(doc, inputString);
      if (error) {
        //Serial.println("Error");
        beeper.Trigger(ERROR);
      }
      else{
   
        int time_flag = doc["time"][0]; 
        int time_int = doc["time"][1]; 
        JsonArray mask = doc["mask"];
        
        if (mask[0] == 1){
          int byte_buffer = mask[1]; 
          mascara.flag = mask[0];
          mascara.buzzer = byte_buffer & B00000001; 
          mascara.lamp_1 = byte_buffer & B00000010;
          mascara.lamp_2 = byte_buffer & B00000100;
          mascara.lamp_3 = byte_buffer & B00001000;
          mascara.lamp_4 = byte_buffer & B00010000;
          mascara.lamp_5 = byte_buffer & B00100000;
          mascara.lamp_6 = byte_buffer & B01000000;
          //Calcula lo que se debe grabar en el eeprom 
          mask_byte = mask[1];
          if (mask_byte != eeprom_mask)
          {
            EEPROM.write(addr_hwd, mask_byte);
            eeprom_mask = EEPROM.read(addr_hwd);
          }
          if ((mascara.buzzer == 1) && !BUZZER_ENABLED)
          {
            BUZZER_ENABLED = true;
            EEPROM.write(addr, true);
          }
          if ((mascara.buzzer == 0) && BUZZER_ENABLED)
          {
            BUZZER_ENABLED = false;
            EEPROM.write(addr, false);
          }
          //Serial.println(mask_byte);
        }//Mask
        if (time_flag == 1) //si hay que modificar el tiempo
        {
          //Si el aparato no esta en manual y el timer flag es 1 y el sensor magnetico es = 1 (doble check !manual)
          if (operation_mode == mode_manual)
          {
            if (sensor_state.magnetic_status != 1)
            {
                beeper.Trigger(ERROR);  
            }
            else
            {
                beeper.Trigger(TWO_BEEP);
                nuevo_tiempo_exposicion = time_int; 
                tiempo_restante = nuevo_tiempo_exposicion;
                for (int i=timer_count; i<NUM_LEDS; i++)
                {
                  leds[i] = CRGB::Black;
                }
                FastLED.show(0); //apagar los leds
                operation_mode = mode_auto_init;
            } 
          } // if modo manual
          //Si no esta en manual, apaga todo y se pone en modo manual
          else
          {
            beeper.Trigger(ONE_BEEP);
            operation_mode = mode_manual;
            pre_desinfeccion_count = 0;
          }
        }//time flag
      } //Else si no hay error en el decode Json
    inputString = "";
    }// if \n
  }//while
}