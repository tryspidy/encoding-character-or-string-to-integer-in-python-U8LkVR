note:text contains your string or already read textfile 

import numpy as np
text = 'hello'
vocab=sorted(set(text))
char_to_ind = {char:ind for ind,char in enumerate(vocab)}
encoded_text = np.array([char_to_ind[c]for c in text])

your string has been encoded