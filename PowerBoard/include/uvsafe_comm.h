/*
 *  by: MRO for UVSA GROUP
 *  Todos los derechos reservados
 *  Winnipeg, Manitoba. Canada. Julio 2020
 */


#include <ArduinoJson.h>

class DataSender {
unsigned long data_period = 200;    // tiempo en milisegs
SENSOR_STRUCT sensor_state;
unsigned long previousMillis;     // will store last time LED was updated

public:
DataSender(SENSOR_STRUCT _sensor_state)
{
        sensor_state = _sensor_state;
}

public:
void Update (SENSOR_STRUCT sensor_state)
{       //Check size calculator for the array at:
       //https://arduinojson.org/v6/assistant/
        const size_t capacity = JSON_ARRAY_SIZE(18) + JSON_OBJECT_SIZE(1) + 45;
        DynamicJsonDocument doc(capacity);
        // check to see if it's time to send the data
        unsigned long currentMillis = millis();
        if (currentMillis - previousMillis >= data_period) {
                previousMillis = currentMillis; // Remember the time
                JsonArray data = doc.createNestedArray("data");
                data.add(millis());
                data.add(FIRMWARE_VERSION);
                data.add(TARJETA);
                data.add(sensor_state.deadman1_sw);
                data.add(sensor_state.deadman2_sw);
                data.add(sensor_state.auto_button);
                data.add(sensor_state.pir_1);
                data.add(sensor_state.pir_2);
                data.add(sensor_state.pir_3);
                data.add(sensor_state.pir_4);
                data.add(sensor_state.magnetic_1);
                data.add(sensor_state.magnetic_2);
                //Comprimir datos antes de enviarlos
                int byte_lamps = sensor_state.lamp_1 + sensor_state.lamp_2 * 2 + 
                sensor_state.lamp_3 * 4 + sensor_state.lamp_4 * 8 + sensor_state.lamp_5 * 16 + 
                sensor_state.lamp_6 * 32 + sensor_state.lamp_deadman * 64 + sensor_state.lamp_auto * 128;
                data.add(byte_lamps);
                data.add(HOROMETRO);
                data.add(BUZZER_ENABLED);
                data.add(operation_mode);
                data.add(tiempo_restante);
                data.add(mask_byte);
                data.add(pre_desinfeccion_count); 
                serializeJson(doc, Serial);
                Serial.println();
        }
}
};
