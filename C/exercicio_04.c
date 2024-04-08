// 4. Escreva um programa que converta temperaturas de Fahrenheit para Celsus

#include <stdio.h>

float forFahrenheit(float temp_celsius){
  float fahrenheit = (temp_celsius*1.8) + 32;
  return fahrenheit;
}

float forCelsius(float temp_fahrenheit){
  float celsius = ((temp_fahrenheit - 32)*5)/9;
  return celsius;
} 

int main(){
  float temperatura;
  int escolha;

  printf("Deseja realizar qual conversão: \n 1. Fahrenheit -> Celsius \n 2. Celsius -> Fahrenheit \n");
  scanf("%d", &escolha);

  switch (escolha){
    case 1:
      printf("Qual temperatura em Fahrenheit> \n");
      scanf("%f", &temperatura);
      printf("Resultado: %.2f C", forCelsius(temperatura));
      break;
    case 2:
      printf("Qual temperatura em Celsius> \n");
      scanf("%f", &temperatura);
      printf("Resultado: %.2f F", forFahrenheit(temperatura));
      break;
    default:
      printf("Opcao invalida");
      break;
  }
}