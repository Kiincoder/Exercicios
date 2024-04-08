// 1. Dado um inteiro x, determine 𝑥!

#include <stdio.h>

int main(){
  int numero, resultado = 1;

  printf("Digite um numero inteiro> \n");
  scanf("%d", &numero);

  while (numero > 1)
  {
    resultado *= numero;
    numero --;
  };

  printf("Resultado: %d", resultado);

}