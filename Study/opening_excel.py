import pandas as pd #as pd vc esta abreviando pandas para pd

from twilio.rest import Client

# Passo a passso da solucao:

# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'] #toda lista do python fica entre [] e pode ficar entre '' e "", mas temos que deixar padronizado.

for mes in lista_meses:
       
    if (tabela_vendas['Vendas'] > 55000).any(): # O [] define qual a coluna da tabela que queremos. 
        
        tabela_vendas = pd.read_excel(f'{mes}.xlsx')#editar o texto de maneira dinamica, colocamos f'{} e colocamos o nome entre chaves para o que queremos mudar, nesse caso e os meses.
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] #.loc e para ele localizar 1 ou mais linhas da tabela.
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0] #.values[0] sempre que usamos o loc, mesmo que encontramos um valor so ele da a tabela e nao o valor, agora quando colocamos o .values[0] recebemos apenas o valor.
        print(f'no mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')


# Para cada arquivo:?
# Verificar se algum valor na coluna Vendas daquele arquivo e maior que 55.00
# Se for maior que 55.000 -> Envia um SMS com o Nome, mes e as vendas do vendedor
# Caso nao seja maior do que 55.000 nao quero fazer nada


#Your Account SID from twilio.com/console

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

# Your Auth Token from twilio.com/console

auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

message = client.messages.create (
    to = "+199xxxxx"
    from_ = "+19xxxxxxx"
    body = "Hello from Python!"
)

print(message.sid)
