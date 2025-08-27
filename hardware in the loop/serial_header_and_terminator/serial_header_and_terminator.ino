const int NumberSize = 4;//byte amount for a single number
const int number_amount = 3;//number of numbers
const int ReadNumbersSize = number_amount*NumberSize;//calculated once here so to not calculte every time it is used
byte byte_read;//variable for the read byte
byte array[number_amount*NumberSize];//amount of bytes that the numbers take
int index = 0;
float num_array[number_amount] = {50,51,52};//if it remains like that it is not working
bool flag = false;

void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

writeToPython(num_array,number_amount);
while(Serial.available()> 0){
  byte_read = Serial.read();
  if(byte_read == 21){//if recived start byte it will initialize the code
    flag = true;
    index = 0;
  }
    if(flag){//if initailized
      if(byte_read == 13){
            if(index == ReadNumbersSize){
              byteArray2number(array,num_array);

            }
        flag = false;
      }
      else if(index < ReadNumbersSize){
        array[index] = byte_read;
        index++;
      }
      else{//wrong amount or AKA missed the CR
      flag = false;//exits to wait for next start byte
      index = 0;
      }   
    }
}
}



void byteArray2number(byte array[ReadNumbersSize], float num_array[number_amount]){
for(int i = 0; i<number_amount; i++){memcpy(&num_array[i] ,&array[i*NumberSize] ,sizeof(float) );}
}

void writeToPython(float* vector, int size)
{
  Serial.write((byte*)vector, size * sizeof(float)); // Send raw bytes
  Serial.write('\r'); 
}

