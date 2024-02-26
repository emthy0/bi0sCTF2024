#! /usr/bin/env python
def generate_brainfuck_code(byte2go) -> str:
  program = ""
  # program = generate_brainfuck_number(abs(byte2go))
  jumpcode ="[[>+<-]>-]" if  byte2go > 0 else  "[[<+>-]<-]"
  backwardjump, fwdjump =  divmod(byte2go, 255)
  print(backwardjump)
  for i in range(backwardjump):
    program += "-" + jumpcode
  program += generate_brainfuck_number(fwdjump)
  program +=  ">[[>+<-]>-]"
  # print(program)
  return program

def generate_brainfuck_number(number):
    # Brainfuck commands for multiplication and addition
    code = []
    pw = 0
    while True:
      quotient, remainder = divmod(number, 10)
      # code += "+" * remainder
      
      code.append("[<+>-]")
      if pw == 0 : code.append(">")
      multiplier = [ "[>++++++++++<-]" for i in range(pw)]
      code.append(">".join(multiplier))
      code.append("+" * remainder)
      
      number = quotient
      pw += 1
      if number == 0 :
        break
    code.reverse()
    code =  "".join(code) + ("<" * (pw -1) )
    # print(code)
        
    # Divide the number into factors
    

    # # Generate the Brainfuck code
    # code = ""
    # code += multiplication_code * quotient
    # code += addition_code
    # code += "+" * remainder
    # code += "."
    
    return code
n = 1000
print(generate_brainfuck_code(n-1))