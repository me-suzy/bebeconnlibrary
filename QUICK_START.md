# 🚀 BebeConn - Quick Start Guide

## Instalare Rapidă

```bash
# 1. Navighează la folderul librăriei
cd bebe-conn-library

# 2. Instalează și testează automat
python install_and_test.py

# 3. Pornește sistemul
bebe-conn start
```

## Utilizare Simplă

### Pornire Locală
```bash
bebe-conn start
```
Accesează: `http://localhost:5000`

### Pornire cu Acces Extern
```bash
bebe-conn start --ngrok
```
Folosește URL-ul afișat în terminal.

### Pornire cu Configurări Personalizate
```bash
bebe-conn start --ngrok --port 8080 --screenshot 60
```

## Utilizare în Python

```python
import bebe_conn

# Pornire simplă
bebe_conn.start()

# Pornire cu ngrok
bebe_conn.start(ngrok=True)

# Pornire doar serverul
bebe_conn.start_server(port=5000)

# Pornire doar agentul
bebe_conn.start_agent(server_url="http://localhost:5000")
```

## Ce Vezi pe Dashboard

- ✅ **Status live** - dacă laptopul este online
- 📸 **Screenshots** - capturi de ecran automate
- 🔧 **Procese active** - lista programelor care rulează
- 📊 **Statistici sistem** - CPU, RAM, Disk usage
- 🕒 **Ultima actualizare** - timestamp curent

## Comenzi Disponibile

```bash
bebe-conn start                    # Pornire completă
bebe-conn start --ngrok           # Cu acces extern
bebe-conn server --port 5000      # Doar serverul
bebe-conn agent                   # Doar agentul
```

## Pentru Dezvoltatori

```bash
# Instalare în mod development
pip install -e .

# Teste
python test_library.py

# Build pentru PyPI
python build_and_upload.py
```

## Cerințe

- Python 3.8+
- Pentru ngrok: https://ngrok.com/download

## Suport

Pentru probleme, deschide un issue pe GitHub sau contactează autorul.

---

**BebeConn** - Monitorizare laptop simplă și eficientă! 🖥️📱
