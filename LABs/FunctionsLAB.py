#Question 1 - Computing box volume
def volume(l,w,h):
    return l*w*h

def main():
   print("BOX #1 length(cm): ",end='')
   l1 = float(input( ))
   print("BOX #1 Width(cm): ",end='')
   w1 = float(input())
   print("Box #1 height(cm): ",end='')
   h1 = float(input())

   v1 = volume(l1,w1,h1)
   print("BOX 1 Volume is", v1, "cmm")
   
   print("Box #2 length (cm): ", end='')
   l2 = float(input())
   print(" Box #2 width (cm):", end='')
   w2 = float(input())
   print("Box #2 height (cm): ", end='')
   h2 = float(input())

   v2 = volume(l2,w2,h2)
   print("BOX 2 Volume is", v2,"ccm")

main()








