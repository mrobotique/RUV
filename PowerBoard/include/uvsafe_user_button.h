/*
 *  by: MRO for IWI
 *  Todos los derechos reservados
 *  Aguascalientes, Mexico. Mayo 2020
 */

#define CINCO_MINUTOS 300 //en segundos

void user_button_update(RGBLeds LedsIndicadores) {
        auto_button.Update();
        safety_functions();

        if (timer_count == 0) last_click_update = millis();
        // Si el switch no es accionado en TIMEOUT_CLICK tiempo el contador se restablece
        else if ((millis() - last_click_update) > TIMEOUT_CLICK) timer_count = 0;

        if (operation_mode == mode_manual) {
                // Si el usuario ejecuta un push largo
                if (auto_button.clicks == -1 && auto_button.depressed == true)
                {
                        LedsIndicadores.confirm_push(true);
                        nuevo_tiempo_exposicion = timer_count * CINCO_MINUTOS;
                        timer_count = 0;
                        while (auto_button.depressed) { //No hacer nada mientras el usuario no suelta el boton
                                auto_button.Update();
                        }

                        LedsIndicadores.confirm_push(false);
                        operation_mode = mode_auto_init;
                }
                if ((auto_button.clicks > 0) && !pir_timeout){
                        last_click_update = millis();
                        timer_count += 1;
                        if (timer_count > NUM_LEDS) timer_count = 1;
                }
        }
        else{
                timer_count = 0;
                safety_functions();
        }
}
