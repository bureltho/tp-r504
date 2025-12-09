compteur1=0
compteur2=0
for i in {1..500}; do
    reponse=$(curl -s localhost:83)
    if [[ $reponse == *"Hello 1"* ]]; then
        ((compteur1++))
    else
        ((compteur2++))
    fi
done
echo "Serveur 1: $compteur1, Serveur 2: $compteur2"
