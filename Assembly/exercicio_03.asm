%include "io.inc"

section .data
    num dd 20

section .text
    global CMAIN
CMAIN:
    call verificaimpar
    xor eax, eax
    ret
    
verificaimpar:
    mov ecx, 0 ; numeros a serem verificados
    mov edi, 0 ; contador de vezes
    @L:
        ; cond de parada
        cmp edi, [num]
        je exit
        
        add ecx, 1
        
        ; divisao         
        mov eax, ecx
        mov edx, 0
        mov ebx, 2
        idiv ebx

        cmp edx, 0 ;verifica  se eh par
        jg print_impar ;jump caso not par
        jmp @L ; volta pro loop
        ret
        
print_impar:
    PRINT_UDEC 4, ecx ; mostra o numero impar
    NEWLINE
    add edi, 1
    jmp @L ; volta pro loop
        
exit:
    xor eax, eax
    ret
        