# Segmentação de cliente com análise RFM e K-means clustering

Este repositório exercíta a criação de uma list segmentada de clientes baseada em suas transações de compra online. 
O código da análise RFM foi majoritariamente obtido neste
 [post](https://towardsdatascience.com/data-driven-growth-with-python-part-2-customer-segmentation-5c019d150444). 
 Pequenas alterações foram realizadas para tratar o dataset utilizado.
 
 ## Dataset
 
 O dataset de compras online se encontra nada pasta **data** e foi ser obtido
 [aqui](https://www.kaggle.com/hellbuoy/online-retail-customer-clustering).
 
 ## Análise e clustering
 
 O código para gerar a lista segmentada se encontra na pasta *notebooks*.
 
 ## API
 
 Uma vez gerados os dados dos segmentos dos clientes, foi disponibilizada uma API na plataforma de núvem do Google
 para obtenção dos segmentos a partir do código dos clientes.
 O código da *cloud function*, bem como os artefatos necessários para fazer o *deploy* da mesma na GCP se encontram na 
 pasta **api**.   
 
 Utilização:
 
 ```
 https://us-central1-rfmclustering.cloudfunctions.net/get_segment?id=<id do client>
```

 Para se informar mais de um cliente por requisição, basta concatenar mais parâmetros *id* com "&":
 
  ```
 https://us-central1-rfmclustering.cloudfunctions.net/get_segment?id=<id do client>&id=<outro id>
```

O resultado será um json com o *id* do cliente como chave e o segmento como valor.