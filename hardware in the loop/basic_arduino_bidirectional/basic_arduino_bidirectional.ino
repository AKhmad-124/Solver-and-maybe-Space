char chr;
float states[2];
int index = 0;
char argvalu1[16];
char argvalu2[16];
int arg_index = 0;
float x = -100;
float y = 50;
int dt = 10;


void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
while (Serial.available() > 0) {
    
    // Read the next character
    chr = Serial.read();
    Serial.print(chr);
    // Terminate a command with a \n
    if (chr == '\n') {
          Serial.println("FUCK");
      Serial.print(states[0]);
      Serial.print(",");
      Serial.println(states[1]);
      index = 0;
    }
    else if(chr = 'x'){//delimiter
          Serial.println("NLLJLK");
      states[index] = atof(argvalu1);
      index++;
      arg_index = 0;
      // memset(argvalu1, 0, sizeof(argvalu1));
    }
    else{
        argvalu1[arg_index] = chr;
          Serial.println("argvalu1[arg_index]");
          Serial.println(argvalu1[arg_index]);

        arg_index++;

    }

}
}
