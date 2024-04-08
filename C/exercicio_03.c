// 3. Dado um número inteiro positivo n, imprimir os n primeiros naturais ímpares

#include <stdio.h>
#include <stdbool.h>


int main(){
  int numero;
  int cont_imp = 0, cont_num = 1;

  printf("Digite um numero inteiro: \n");
  scanf("%d", &numero);
  printf("\n");

  while (cont_imp < numero)
  {
    if(cont_num % 2 != 0){
      printf("%d ", cont_num);
      cont_num++;
      cont_imp++;
    }
    else{
      cont_num++;
    }
  } 
}