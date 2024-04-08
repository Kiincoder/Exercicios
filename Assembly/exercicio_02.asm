%include "io.inc"

section .data
    num dd 43

section .text
    global CMAIN

CMAIN:
    mov eax, [num]
    call primo
    xor eax, eax
    ret
    
primo:
    cmp eax, 2
    je isprimo
    mov edx, 0
    mov ebx, 2
    idiv ebx
    cmp edx, 0
    je isnotprimo
    jg isprimo

  
isprimo:
    PRINT_STRING 'PRIMO'
    xor eax, eax
    ret

isnotprimo:
    PRINT_STRING 'COMPOSTO'
    xor eax, eax
    ret

    