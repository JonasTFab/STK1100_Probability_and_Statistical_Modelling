
import numpy as np , ma tpl o t l ib . pyplot as p l t
data = np . l o adt x t ( " dods sannsynl ighe t􀀀f e l l e s . txt " , skiprows=1)
sorted = np . t r anspo s e ( data )
a l de r = sorted [ 0 ]
dod = sorted [ 1 ] / 1 0 0 0
############ oppgave 3c ) ############
def punkt sannsynl ighe t (x , q ) :
i f x==0:
return q [ x ]
el se :
prod=(1􀀀q [ 0 ] )
for y in range (x􀀀1):
prod = (1􀀀q [ y+1])
return q [ x ]  prod
pkt san = np . z e r o s ( len ( a l de r ) )
for i in range ( len ( a l de r ) ) :
pkt san [ i ] = punkt sannsynl ighe t ( int ( a l de r [ i ] ) , dod )
# Sum av p unk t s anns ynl i g h e t s k a l vaere l i k 1 . Sj e k k e r om de t er
# sant i e t t e r f o l g e n d e p r i n t
print ( "Sum over punkt sannsynl ighe t ene : " , sum( pkt san ) )
p l t . pl o t ( a l de r [ 3 5 : ] , pkt san [ 3 5 : ]  1 0 0 0 )
p l t . g r id ( ) ; p l t . x l a b e l ( "Alder i aar " ) ; p l t . y l a b e l ( r " Sannsynl ighe t i pr omi l l e " )
p l t . t i t l e ( "Punkt sannsynl ighe t " )
#p l t . show ( )
############ oppgave 3e ) ############
def h(X) :
i f X<32:
return 0
el se :
return (100000/1.0332)  (1 􀀀(1/1.03)(X􀀀31)) / (1􀀀1/1.03)
E h = 0
for i in range ( 7 2 ) :
E h += h( i ) pkt san [ i +35]
7
print ( "Forventet naave rdi av p e n s j o n s u t b e t a l i n g : %.1 f " % E h )
############ oppgave 3g ) ############
def g (X) :
i f X<=31:
return (1 􀀀(1/1.03)(X+1)) / (1􀀀1/1.03)
el se :
return (1 􀀀(1/1.03)(32) ) / (1 􀀀1/1.03)
E g = 0
for i in range ( 7 2 ) :
E g += g ( i ) pkt san [ i +35]
print ( "Forventet naave rdi av pr emi e innbe t a l ing ene : %.2 f " % E g )
p l t . show ( )
"""
Ut s k r i f t f r a t e rminal :
Sum over punk t s anns ynl i g h e t ene : 1.0
For v ent e t naav e rdi av p e n s j o n s u t b e t a l i n g : 495929.1
For v ent e t naav e rdi av p r emi e innb e t a l ing ene : 20.37
"""
