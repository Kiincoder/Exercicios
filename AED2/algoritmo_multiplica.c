#include <stdio.h>
#define SIZE 3

int potencia(int num, int expo){
  int cont, pot = 1;
  if(expo == 0){
    return 1;
  }
  else {
    for(cont = 1; cont <= expo; cont++){
     pot *= num; 
    }
    return pot;
  }
}

int main(){
  int arr1[SIZE] = {3,0,0}, arr2[SIZE] = {3,0,0}, arr3[SIZE*2] = {0};
  int index1, index2, index3, produto, numero;
  int resultado = 0;

  for (index1 = SIZE-1; index1 >= 0; index1--){
    int carry = 0;
    int soma = 0;
    int expoente = 0;

    for (index2 = SIZE-1; index2 >= 0; index2--){
      produto = (arr1[index1] * arr2[index2]) + carry;
      numero = produto%10;
      carry = produto/10;
      arr3[index1 + index2 + 1] = numero;
    }
    for (index3 = (SIZE*2)-1; index3 >= 0; index3--){
      soma += arr3[index3] * potencia(10, expoente);
      expoente ++;
    }
    resultado += soma;
  }
  printf("Resultado: %d", resultado);
}

// Sendo A e B vetores de tamanho n contendo os valores do multiplicador e multiplicando, respectivamente, 
// e C sendo um vetor de tamanho 2n preenchida por zeros. Exemplo:
// A[3] = [3, 0, 0], B[3] = [3, 0, 0], C[6] = [0, 0, 0, 0, 0, 0]
//
// for i = size(A) - 1 to 0 do:
//  carry = 0
//  sum = 0
//  exp = 0
//  for j = size(B) - 1 to 0 do:
//    product = (A[i] * B[j]) + carry
//    number = product % 10
//    carry = product / 10
//    C[i + j + 1] = number
//  for k = (size(C)*2) - 1 to 0 do:
//    sum = sum + C[k] * 10^exp 
//    exp = exp + 1
//  result = result + sum
