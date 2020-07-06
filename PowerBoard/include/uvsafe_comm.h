/*
 *  by: MRO for IWI
 *  Todos los derechos reservados
 *  Aguascalientes, Mexico. Mayo 2020
 */


#include <ArduinoJson.h>

class DataSender {
unsigned long data_period = 250;    // tiempo en milisegs
SENSOR_STRUCT sensor_state;
unsigned long previousMillis;     // will store last time LED was updated

public:
DataSender(SENSOR_STRUCT _sensor_state)
{
        sensor_state = _sensor_state;
}

public:
void Update (SENSOR_STRUCT sensor_state)
{
        const size_t capacity = JSON_ARRAY_SIZE(19) + JSON_OBJECT_SIZE(2);
        DynamicJsonDocument doc(capacity);
        // check to see if it's time to send the data
        unsigned long currentMillis = millis();
        if (currentMillis - previousMillis >= data_period) {
                previousMillis = currentMillis; // Remember the time
                doc["sensors"] = "all";
                JsonArray data = doc.createNestedArray("data");
                data.add(sensor_state.deadman1_sw);
                data.add(sensor_state.deadman2_sw);
                data.add(sensor_state.pir_1);
                data.add(sensor_state.pir_2);
                data.add(sensor_state.pir_3);
                data.add(sensor_state.pir_4);
                data.add(sensor_state.magnetic_1);
                data.add(sensor_state.magnetic_2);
                data.add(sensor_state.lamp_1);
                data.add(sensor_state.lamp_2);
                data.add(sensor_state.lamp_3);
                data.add(sensor_state.lamp_4);
                data.add(sensor_state.lamp_5);
                data.add(sensor_state.lamp_6);
                serializeJson(doc, Serial);
                Serial.println();
        }
}
};
