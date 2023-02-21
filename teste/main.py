# assembly_function.asm
section .text
global my_function

my_function:
  mov eax, 1
  ret

# Python script
from ctypes import CDLL

lib = CDLL("path/to/assembly_function.so")
result = lib.my_function()
print(result) # saída: 1
