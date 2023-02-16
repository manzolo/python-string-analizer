curl http://localhost:8080/

# Generare un token JWT valido
TOKEN=$(curl -u user1:password1 http://localhost:8080/login | jq -r '.token')

# Effettuare una richiesta GET all'endpoint '/protected' includendo il token JWT nell'header Authorization
curl -H "Authorization: Bearer $TOKEN" http://localhost:8080/protected

curl http://localhost:8080/protected

# Generare un token JWT non valido
TOKEN="invalid_token"

# Effettuare una richiesta GET all'endpoint '/protected' includendo il token JWT non valido nell'header Authorization
curl -H "Authorization: Bearer $TOKEN" http://localhost:8080/protected
