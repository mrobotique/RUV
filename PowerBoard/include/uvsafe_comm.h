#include <ArduinoJson.h>

void send_data(SENSOR_STRUCT sensor_state){
    const size_t capacity = JSON_ARRAY_SIZE(19) + JSON_OBJECT_SIZE(2);
    DynamicJsonDocument doc(capacity);
    doc["sensors"] = "all";
    JsonArray data = doc.createNestedArray("data");
    data.add(sensor_state.deadman_sw);
    data.add(sensor_state.pir_1);
    data.add(sensor_state.pir_2);
    data.add(sensor_state.pir_3);
    data.add(sensor_state.pir_4);
    data.add(sensor_state.magnetic_1);
    data.add(sensor_state.magnetic_2);
    data.add(sensor_state.magnetic_3);
    data.add(sensor_state.magnetic_4);
    data.add(sensor_state.magnetic_5);
    data.add(sensor_state.magnetic_6);
    data.add(sensor_state.lamp_1);
    data.add(sensor_state.lamp_2);
    data.add(sensor_state.lamp_3);
    data.add(sensor_state.lamp_4);
    data.add(sensor_state.lamp_5);
    data.add(sensor_state.lamp_6);
    data.add(sensor_state.lamp_7);
    data.add(sensor_state.lamp_8);
    serializeJson(doc, Serial);
    Serial.println();
}
