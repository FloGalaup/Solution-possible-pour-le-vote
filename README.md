# Solution-possible-pour-le-vote
## Lancer le projet localement

### Pré-requis

- Python 3.9+
- Environnement virtuel (recommandé)

### Cloner le projet

```
git clone https://github.com/jayParent/distributed-systems-crypto.git
```

### Installer les dépendances Python

```
cd distributed-systems-crypto/cryptoproject
pip install -r requirements.txt
```

### Lancer le serveur

```
cd distributed-systems-crypto/cryptoproject
python manage.py runserver
```

### Accéder au site Web

http://127.0.0.1:8000/

### Accéder à l'API REST

http://127.0.0.1:8000/api/v1/

## Lancer le projet localement avec Docker

### Pré-requis

- Python 3.9+
- Environnement virtuel (recommandé)
- Docker

### Cloner le projet

```
git clone https://github.com/jayParent/distributed-systems-crypto.git
```

### Construire l'image Docker
```
docker build --tag cryptoproject:latest .
```

### Lancer le container Docker 
```
docker run --name cryptoproject -d -p 8000:8000 cryptoproject:latest
```

### Accéder au site Web

http://127.0.0.1:8000/

### Accéder à l'API REST

http://127.0.0.1:8000/api/v1/
