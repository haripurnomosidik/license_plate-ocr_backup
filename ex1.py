import trans_char
import pickle
fun = trans_char


with open ('out.pkl', 'wb') as x:
    pickle.dump(fun, x)