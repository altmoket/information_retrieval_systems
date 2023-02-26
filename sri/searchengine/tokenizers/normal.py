from nltk.tokenize import word_tokenize
from nltk.stem import 	WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string

class NormalTokenizer:
    def __init__(self) -> None:
        pass
    
    def tokenize(self, text: str):
        # convirtiendo en palabras
        tokens = word_tokenize(text)
        # convertir a minúsculas
        tokens = [w.lower() for w in tokens]
        # prepare a regex para el filtrado de caracteres
        re_punc = re.compile('[%s]' % re.escape(string.punctuation))
        # eliminar la puntuación de cada palabra
        stripped = [re_punc.sub('', w) for w in tokens]
        # eliminar los tokens restantes que no estén en orden alfabético
        words = [word for word in stripped if word.isalpha()]
        # Eliminar stopwords
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
        # Lemantizacion
        wordnet_lemmatizer = WordNetLemmatizer()
        lemmas = [wordnet_lemmatizer.lemmatize(word) for word in words]
        return lemmas
    
if __name__ == "__main__":
    TEXT = " supersonic shear flow past an airfoil between two parallel walls .   the supersonic flow with assigned mach number gradient in the span direction past a straight wing between two parallel walls is studied using the small-disturbance theory .  the governing equation for the disturbance pressure on the airfoil, together with the boundary conditions on the airfoil and at the walls, is solved by the method of separation of variables .  upon separation the problem is reduced to a sturm-liouville eigenvalue problem and to the solution of the telegraph equation .   as an application, a certain mach number profile is selected and the resulting pressure distribution on a parabolic arc airfoil is computed . "
    tokenizer = NormalTokenizer()
    print(TEXT)
    words = tokenizer.tokenize(TEXT)
    print(words)