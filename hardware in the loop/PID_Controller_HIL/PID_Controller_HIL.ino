float Vcurr;
String message;
float Vsp = 60;
float dt = 0.003;
float ErrDiff_prev = Vsp;
float ErrPrev = Vsp;
float ErrInt = 0;
float kp =8; 
float ki =0.9*4*3 ;
float kd =-3*1.5;
float Force;
void setup() {

Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0){
    Vcurr = Serial.parseFloat();
    Force = PID_Controller(Vsp,Vcurr,dt);
    Serial.println(Force);

  }

}

float PID_Controller(float Vsp,float Vcurr,float dt){
        float Err = Vsp - Vcurr;
        int N = 5;
        float alpha = N*dt / (1 + N*dt);   
        float ErrDiff = alpha*((Err - ErrPrev)/dt) + (1-alpha)*ErrDiff_prev;
        ErrInt = ErrInt + Err*dt;
        float force = kp*Err + ki*ErrInt + kd*ErrDiff;
        // ErrDiff_prev = ErrDiff;
        ErrPrev = Err;
        return force;
}