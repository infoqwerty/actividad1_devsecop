
def save_password(password):
    # Vulnerabilidad: Uso de un algoritmo de hashing débil (MD5)
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    with open('passwords.txt', 'a') as f:
        f.write(hashed_password + '\n')

def get_ﬁle(ﬁlename):
    # Vulnerabilidad: No se valida la entrada del usuario
    if os.path.exists(ﬁlename):
        with open(ﬁlename, 'r') as f:
            return f.read() 
			
    else:
        return "El archivo no existe"

def login(password):
    # Vulnerabilidad: Comparación de cadenas insegura
    with open('passwords.txt', 'r') as f:
        for line in f:
            if password == line.strip():
                return True
    return False
