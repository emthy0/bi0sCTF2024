#! /opt/homebrew/bin/python3
from time import sleep
import sympy
import pwn
import math
from itertools import product
from bf import generate_brainfuck_code

r = pwn.remote('13.201.224.182', 32081)
print("> " + r.recv().decode("utf-8"))
r.sendline(b"N")
print("> " + r.recv().decode("utf-8"))
r.sendline(b"N")
while True:
  r.recvuntil(b"TAPE > [").decode("utf-8")
  flagdp = int(r.recvuntil(b"]")[:-1])
  r.recvuntil(b"POINTER IS AT : ")
  curdp = int(r.recvuntil(b"\n").decode("utf-8"))
  r.recv()
  print("flag : ",flagdp)
  print("current : ",curdp)
  byte2go = flagdp - curdp
  print("diff",byte2go)
  program=""
  if byte2go > 0:
    program = "+[>[<-]<[->+<]>]>"
  else:
    program = "+[<[>-]>[-<+>]<]<"

  # if byte2go < 0:
  #     program = "-" + ("+" * abs(byte2go)) + "[[<+>-]<-]"
  # else:
  #     program = ("+" * abs(byte2go)) + "[[>+<-]>-]"

  # print(program)
  # sleep(3)
  r.sendline(program.encode("utf-8"))
  r.recvuntil("DATA POINTER AT - ".encode("utf-8"))
  resultpre = r.recvuntil("\n".encode("utf-8")).decode("utf-8")
  r.recvuntil("THIS IS YOUR ONE BYTE -- [".encode("utf-8"))
  thebyte = r.recvuntil("]".encode("utf-8"))[:-1]
  print("result ptr",resultpre)
  print("res byte",thebyte.decode("utf-8"))

  # r.interactive()
