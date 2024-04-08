%include "io.inc"

section .data
    num dd 5

section .text
    global CMAIN


CMAIN:
    call fatorial
    xor eax, eax
    ret
    
fatorial:
    mov eax, [num]
    mov ebx, eax
    while:
        dec ebx
        cmp ebx, 1
        je exit
        imul eax, ebx
        LOOP while
        ret

exit:
    PRINT_UDEC 4, eax
    xor eax, eax
    ret