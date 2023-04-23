COMANDOS SCRIPT

UTILIZADO 21092022 

read -r -p "Estao corretos? [y/N] " resp
if [[ "$resp" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    echo "Prosseguindo"
elif [[ "$resp" =~ ^([nN][oO]|[nN])$ ]]; then
    echo "Corrija os dados no arquivo de configuracao e execute novamente este arquivo"
    exit 0
else 
    echo "Digite um comando valido e tente novamente"
    exit 0
fi


UTILIZADO 21092022
while read -p "Estao corretos? [y/N] " a_resp
do
    if [[ "$a_resp" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        echo "Proseguindo"
        break
    elif [[ "$a_resp" =~ ^([nN][oO]|[nN])$ ]]; then
        echo "Corrija os dados no arquivo de config e execute novamente este arquivo"
        break
    else
        echo "Digite um comando valido e tente novamente"
                 
        
    fi
done
