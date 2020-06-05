import myprosody as mysp
import pickle

p="7.RP.1 - Ratios and Unit Rates-Is9ioUILsrU_new" #Audio file name
c=r"D:/Grad/IST Research/Done/myprosody-master/myprosody" #an example of path to directory "myprosody" 

gender,mood = mysp.myspgend(p,c)
score = mysp.mysppron(p,c)