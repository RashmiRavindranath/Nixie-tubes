char data[6];
int store[] = {1,2,3,4,5,6};
int i=0;
int k=0;
int mypin=5;
String dat;
int data_int[6];


// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(mypin, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {

// Read time
  if(Serial.available()){
    int size = Serial.readBytes(data, 6);
    for(int j=0; j<6; j++){
      data_int[j] = int(data[j])-48;
    }
  }
}
