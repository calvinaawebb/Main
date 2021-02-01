import tkinter as tk
import json as js

def entry_add():
    out = []
    d = {1:"Enter Name:",2:"Enter Language:",3:"Enter Category:",4:"Enter Description:"}
    for i in range(4):
        inp = input(d[i])
        out.append(inp)
        return out
entry_add()
