#include <stdio.h>
#include <string.h>


int main(){
  char palavra[4] = "ANA";
  char frase[30] = "ANA E MARIANA GOSTAM DE BANANA";

  int i = 0, repet = 0;

  while (i < 40)
  {
    if (frase[i] == palavra[0]){
      int j = i;
      int cont = 0;
      char comp[4] = "";
      while (cont < 3 && j < 30)
      {
        comp[cont] = frase[j];
        j += 1;
        cont += 1;
      }
      if (strcmp(comp, palavra) == 0){
        repet += 1;
      } 
    }
    i += 1;
  }
  printf("Temos que a palavra %s ocorre %d vezes na frase.", palavra,repet);
}


