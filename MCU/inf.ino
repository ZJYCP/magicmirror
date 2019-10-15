#include <SoftwareSerial.h>


SoftwareSerial BT(10, 11);
unsigned char data[7]={0xAA,0xFB,0xFF,0xFF,0x31,0x32,0x33};
unsigned char data1[7]={0xAA,0xFB,0x00,0x01,0x31,0x32,0x33};
unsigned char data2[7]={0xAA,0xFB,0x00,0xFF,0x31,0x32,0x33};
int i;
char dd;
int inf_dete;
int inf_flag=1;
void setup() {
  Serial.begin(9600);
  Serial.println("BT is ready!");
  pinMode(8,OUTPUT);//设置数字8引脚为辒出模式
  BT.begin(115200);

}
void loop() {

  inf_dete=analogRead(5);//读叏模拟5口电压值
  if(inf_dete>512&&inf_flag==1)//如果大于512（2.5V）
  {
      for(i=0;i<7;i++){
         BT.write(data[i]);
      }
      digitalWrite(8,HIGH);//点亮led灯
      delay(3000);
      digitalWrite(8,LOW);//熄灭led灯
  }



//  if (Serial.available()) {
//    dd=Serial.read();
//    if(dd=='g'){
//      for(i=0;i<7;i++){
//         BT.write(data1[i]);
//      }
//    }
//    if(dd=='h'){
//      for(i=0;i<7;i++){
//         BT.write(data[i]);
//      }
//    }
//
//  }
//  if (BT.available()) {
//    Serial.print(BT.read(),HEX);
//  }
}
