#define INPUT_PIN 6
#define TIME_INTERVAL 10000

const int blink_no = 5;
int count = 0;
bool flag = false;
unsigned long last_millis;

void setup() {
    pinMode(INPUT_PIN, INPUT);
    Serial.begin(9600);
}

void loop() {
    count = 0;
    last_millis = millis();

    while(flag == false && millis() - last_millis <= TIME_INTERVAL) {
        if(digitalRead(INPUT_PIN) == HIGH)
            ++count;

        if(count >= blink_no) {
            flag = true;

            Serial.println("1");
            Serial.end();

            break;
        }

        delay(100);
    }
    
}
