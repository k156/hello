#include <stdio.h>
 int main(){
     int n;
     int f;
     scanf("%d",&n);


    switch(n){
        case 1:
        printf("1이 켜졌습니다.");
        break;

        case 2:
        printf("2이 켜졌습니다.");
        break;


        case 3:
        printf("3이 켜졌습니다.");
        break;


        case 4:
        printf("4이 켜졌습니다.");
        break;

        default:
        printf("스위치 오류 :  우리집의 스위치는 1~4번까지 밖에 없습니다.");
        break;



    }
 return 0;
 }
