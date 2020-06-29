#include <Arduino.h>
#include <U8g2lib.h>
#include <SPI.h>

U8G2_ST7920_128X64_1_SW_SPI u8g2(U8G2_R2, /* clock=*/ 13, /* data=*/ 11, /* CS=*/ 10, /* reset=*/ 8);

void setup() {
  u8g2.begin();
}

void u8g2_prepare(void) {
  u8g2.setFont(u8g2_font_siji_t_6x10);
  u8g2.setFontRefHeightExtendedText();
  u8g2.setDrawColor(1);
  u8g2.setFontPosTop();
  u8g2.setFontDirection(0);
}

void u8g2_box_title(uint8_t a) {
  u8g2.drawStr( 3, 3, "UVSA Menu");
  u8g2.drawStr( 8, 15, "Timer");
  u8g2.drawStr( 8, 25, "Lamparas");
  u8g2.drawStr( 8, 35, "Info");
  u8g2.drawLine(u8g2.getDisplayWidth()/2, 0, u8g2.getDisplayWidth()/2, u8g2.getDisplayHeight());
  u8g2.drawFrame(0,0,u8g2.getDisplayWidth(),u8g2.getDisplayHeight() );
}

void draw_hexagon(int x_offset){
  //Hexagono de 20 px de lado
  //El hexagono se calculo usando :
  //https://www.mathopenref.com/coordpolycalc.html
  u8g2.drawLine(x_offset+30,10,x_offset+13,20);
  u8g2.drawLine(x_offset+13,20,x_offset+13,40);
  u8g2.drawLine(x_offset+13,40,x_offset+30,50);
  u8g2.drawLine(x_offset+30,50,x_offset+47,40);
  u8g2.drawLine(x_offset+47,40,x_offset+47,20);
  u8g2.drawLine(x_offset+47,20,x_offset+30,10);
  //Dibujar las "lamparas"
  u8g2.drawCircle(x_offset+19,11,4);
  u8g2.drawCircle(x_offset+41,11,4);
  u8g2.drawCircle(x_offset+19,49,4);
  u8g2.drawCircle(x_offset+40,49,4);
  u8g2.drawCircle(x_offset+8,30,4);
  //como prender y apagar la  "lampara" en el display
  //primero dibuja el circulo (lampara apagada)
  u8g2.drawCircle(x_offset+52,30,4);
  //dibuja el disco (lampara prendida)
  //este se puede sobreponer la circulo y se va  a rellenar
  u8g2.drawDisc(x_offset+52,30,4);
  //para "apagarla"
  //primero se invierte el color (para apgar los pixeles)
  u8g2.setDrawColor(0);
  //despues se dibuja un circulo en "negativo"
  u8g2.drawDisc(x_offset+52,30,4);
  //Se vuelve a poner el color en blanco
  u8g2.setDrawColor(1);
  //aqui uno dibuja otra vez lo que se necesite.
  //En este caso, un circulo ( lampara apagada)
  u8g2.drawCircle(x_offset+52,30,4);
  }

uint8_t m = 24;

void loop() {
  char m_str[3];
strcpy(m_str, u8x8_u8toa(m, 2));		/* convert m to a string with two digits */
u8g2.firstPage();
do {
  u8g2_prepare();
   //u8g2_box_title(0);
   draw_hexagon(70);
} while ( u8g2.nextPage() );

}
