// 2. Dado um inteiro positivo n, verificar se n é primo.

#include <stdio.h>

int main(){
  int numero;
  int divisores = 0;

  printf("Digite um numero inteiro> \n");
  scanf("%d", &numero);

  for (int divisor = numero; divisor > 0; divisor--){
    if (numero % divisor == 0){
      divisores ++;
    }
  }
  if (divisores == 2){
    printf("Primo");
  }
  else {
    printf("Composto");
  }
}