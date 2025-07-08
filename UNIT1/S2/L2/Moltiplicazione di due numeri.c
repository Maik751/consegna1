//Vogliamo ottenere la moltiplicazionme di due numeri
#include <stdio.h>
int main()  {

int primonumero;
int secondonumero;
int risultato;

printf("inserisci il primo numero\n");
scanf("%d", &primonumero);

printf("inserisci il secondo numero\n");
scanf("%d", &secondonumero);

risultato = primonumero * secondonumero;

printf("La moltiplicazione tra i due numeri è: %d\n", risultato);

return 0;

}