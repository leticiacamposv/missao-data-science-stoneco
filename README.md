# Sobre o repositório
## Estrutura de pastas e seus conteúdos
- data
    - raw
        Contem os dados como vêm direto da fonte. Neste caso, o dataset 'Missão_Stone_-_Dados_de_trx_(3).xslx
    - processed
        Contem dados raw pré-processados para análise dos dados
    - train_test
        Contém os dados inteiriços pré-processados e a parcela de treino, teste e validação usados na modelagem
    - predicted
        Contém os dados crus sem classificação preditos pelo modelo (aba2, no caso)
- models
    Contém artefatos do modelo treinado
- notebooks <u>**!!!!! Aqui está todo o desenvolvimento do desafio passo a passo, os demais são entregas extras**</u>
    Contém os notebooks de toda a fase de teste e modelagem, etapa de desenvolvimento
- reports 
    Contém os resultados da EDA
- src
    Contém todos os códigos para automação dos processos
    - data
        Contém script de criação do dataset (limpeza, tratamento de nulos, etc)
    - features
        Contém script para adição de novas features/feature engineering
    - models
        Contém scripts de treino e de predição do modelo
    - visualization
        Contém scripts para construção de gráficos ou quaisquer elementos para dataviz
- documents
    Contém todos os arquivos de documentação

## Autora:
Leticia Campos Valente | [LinkedIn](https://www.linkedin.com/in/leticia-campos-valente/)

# Sobre o desafio
## Missão Stone Co.
Entendimento da missão:
### **Dados disponíveis sobre a transação:**
| Dia    | Data da transação  |
|--------|--------------------|
| Hora   | Hora da transação  |
| Valor  | Valor da transação |
| Cartão | Número do cartão   |
| CBK    | Flag de chargeback |

### **Perguntas a serem repondidas/etapas**
#### Aba 1:
- Qual é o comportamento transacional do cliente (o que caracteriza as transações deste cliente)?

- Qual é o perfil das transações que retornaram chargeback?

- Crie um método de identificar se uma transação futura retornará chargeback (modelagem)

#### Aba 2: 
- Aplicar o modelo nas transações da Aba 2, que representam as transações do mesmo lojista depois de um mês.

#### Final:
- Propor regras de negócio que melhorem a operação deste cliente, fazendo uma análise numérica do impacto que suas regras teriam no negócio e apresentando os resultados de forma estruturada.

# Notas da autora:
Uma abordagem a se tratar para além do desafio: Treinar algoritmo de anomalias para comparação com o modelo treinado do Lightgbm como um Isolation Forest

