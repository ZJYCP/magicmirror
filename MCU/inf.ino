#include <SoftwareSerial.h> 


SoftwareSerial BT(10, 11);
unsigned char data[7]={0xAA,0xFB,0xFF,0xFF,0x01,0x00,0x11};
unsigned char data1[7]={0xAA,0xFB,0xFF,0xFF,0x02};
int i;
char dd;
int inf_dete;
int inf_last=0;  //记录上一次的红外状态
int inf_now=0;
unsigned long lDTime=0;
unsigned long deDelay=5000;
int sound;
unsigned long sound_last=0;

void setup() {
  Serial.begin(9600);
  Serial.println("BT is ready!");
  pinMode(8,OUTPUT);//设置数字8引脚为辒出模式 
  BT.begin(115200);

}

String tohex(int n) {
  if (n == 0) {
    return "00"; //n为0
  }
  String result = "";
  char _16[] = {
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
  };
  const int radix = 16;
  while (n) {
    int i = n % radix;          // 余数
    result = _16[i] + result;   // 将余数对应的十六进制数字加入结果
    n /= radix;                 // 除以16获得商，最为下一轮的被除数
  }
  if (result.length() < 2) {
    result = '0' + result; //不足两位补零
  }
  return result;
}
void loop() {


  //声音
  sound=analogRead(4);
  if(millis()-sound_last>4000){
      sound_last=millis();
      String res="";
      res=tohex(sound);
      for(i=0;i<5;i++){
         BT.write(data1[i]);
      }
      for(i=0;i<res.length();i++){
        BT.write(res[i]-48);
      }      
  }

 //红外
  inf_dete=analogRead(5);//读取模拟5口电压值 

  if(inf_dete>512){
    inf_now=1;
  }else{
    inf_now=0;
    digitalWrite(8,LOW);//熄灭led灯
  }

  if(inf_dete>512&&millis()-lDTime>deDelay)//如果大于512（2.5V） 
  { 
      lDTime=millis();
      for(i=0;i<7;i++){
         BT.write(data[i]);
      }
      digitalWrite(8,HIGH);//点亮led灯 
  }
  inf_last=inf_now;
  
//蓝牙模块测试  
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
