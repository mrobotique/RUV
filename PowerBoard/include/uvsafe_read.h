

SENSOR_STRUCT read_sensors(SENSOR_STRUCT sensor_state, Adafruit_MCP23017 gpio){
  /*
  This function reads all the declared sensors
  :return: struct conteniendo el estado de los sensores
  :rtype: SENSOR_STRUCT
  */
  sensor_state.deadman_sw = digitalRead(DEADMAN_Pin);
  sensor_state.pir_1 = digitalRead(PIR1_Pin);
  sensor_state.pir_2 = digitalRead(PIR2_Pin);
  sensor_state.pir_3 = digitalRead(PIR3_Pin);
  sensor_state.pir_4 = digitalRead(PIR4_Pin);
  sensor_state.magnetic_1 = gpio.digitalRead(MAGNETIC1);
  sensor_state.magnetic_2 = gpio.digitalRead(MAGNETIC2);
  sensor_state.magnetic_3 = gpio.digitalRead(MAGNETIC3);
  sensor_state.magnetic_4 = gpio.digitalRead(MAGNETIC4);
  sensor_state.magnetic_5 = gpio.digitalRead(MAGNETIC5);
  sensor_state.magnetic_6 = gpio.digitalRead(MAGNETIC6);
  sensor_state.lamp_1 = gpio.digitalRead(LAMP1);
  sensor_state.lamp_2 = gpio.digitalRead(LAMP2);
  sensor_state.lamp_3 = gpio.digitalRead(LAMP3);
  sensor_state.lamp_4 = gpio.digitalRead(LAMP4);
  sensor_state.lamp_5 = gpio.digitalRead(LAMP5);
  sensor_state.lamp_6 = gpio.digitalRead(LAMP6);
  sensor_state.lamp_7 = gpio.digitalRead(LAMP7);
  sensor_state.lamp_8 = gpio.digitalRead(LAMP8);
  return sensor_state;
}

void print_sensor_state(SENSOR_STRUCT sensor_state){
  Serial.print("deadman_sw: ");
  Serial.print(sensor_state.deadman_sw);
  Serial.print(" | PIR :");
  Serial.print(sensor_state.pir_1);
  Serial.print(sensor_state.pir_2);
  Serial.print(sensor_state.pir_3);
  Serial.print(sensor_state.pir_4);
  Serial.print(" | mag: ");
  Serial.print(sensor_state.magnetic_1);
  Serial.print(sensor_state.magnetic_2);
  Serial.print(sensor_state.magnetic_3);
  Serial.print(sensor_state.magnetic_4);
  Serial.print(sensor_state.magnetic_5);
  Serial.print(sensor_state.magnetic_6);
  Serial.print(" | lamps: ");
  Serial.print(sensor_state.lamp_1);
  Serial.print(sensor_state.lamp_2);
  Serial.print(sensor_state.lamp_3);
  Serial.print(sensor_state.lamp_4);
  Serial.print(sensor_state.lamp_5);
  Serial.print(sensor_state.lamp_6);
  Serial.print(sensor_state.lamp_7);
  Serial.println(sensor_state.lamp_8);
}
