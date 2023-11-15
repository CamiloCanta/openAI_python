# Taller Sainapsis

## Planteamiento 

La finalidad de este taller consiste en adquirir habilidades para emplear Langchain (una herramienta esencial en la creación de agentes que aplican la técnica de Generación Aumentada con Recuperación, también conocida como RAG), a la par de evaluar buenas prácticas y la escritura de código limpio en Python.

Las siguientes actividades y desafíos serán beneficiosos para consolidar el conocimiento en los ámbitos mencionados anteriormente.

El logro final que se persigue es desarrollar una API REST capaz de recibir como entrada un mensaje del usuario final (para ser procesado por un orquestador, que es una API de Python que ejecuta un agente de Langchain), y mediante el uso de una base de datos de vectores y los puntos finales de OpenAI para su Modelo de Lenguaje, generar una respuesta.

## Desafío #1
Crear una base de datos de vectores en [Pinecone Starter Version](https://www.pinecone.io/) usando su correo institucional, cargar los documentos anexos (FAQs de universidades) usando Embeddings de OpenAI y Langchain. Configurar una Tool de langchain que consulte los documentos y genere una respuesta.

## Prerequicitos:
Es necesario tener instaladas las siguientes librerías en nuestros entornos de trabajo:

- langchain
- openai==0.27.8
- tiktoken
- requests
- pydantic
- pinecone-client

## Desarrollo
1. Primero, configuramos la variable de entorno, limitada al uso en la clase del laboratorio:
```
OPENAI_API_KEY = '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'
```
2. Luego, replicamos el agente básico que se nos presentó, haciendo uso de:
    + Langchain: Agents, Tools, Embeddings y Vectorstores - Pinecone  
    ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/448417a3-6d59-461e-8d0b-69c4f7cf4a7c)

3. Añadir los documentos proporcionados referentes a información de los diferentes carreras en la universidad:
4. Creamos una base de datos de Vectores en Pinecone, ingresando con nuestra cuenta institucional:
   + Nombre (index): gpt
   + API Key: fc1c7b01-da90-4480-8599-ae80124757b9
   + Environment: gcp-starter
5. Configuramos la API key de Pinecone y el environment en Windows como variables de entorno:
```
PINECONE_API_KEY = <API KEY de Pinecone Aquí>
PINECONE_ENVIRONMENT = 'gcp-starter'
```
6. Vectorizamos estos documentos y los subimos a la base de Datos recién creada:
   ![image](https://github.com/CamiloCanta/openAI_python/assets/108955358/0b14e74a-e071-41db-b768-d75bc02e9966)


7. Creamos un método de búsqueda con OpenAI, Pinecone y sus agentes, en búsqueda de implementar un nuevo tool:
   + ![image](https://github.com/SanRocks1220/Taller_IA_AREP/assets/99696682/b1d1af40-019a-496c-8042-6e0eb1512e8c)

##Funcionamiento
No se puede tener evidencias de funcionamiento a la fecha de la realización de este taller por diferentes motivos:

- Al momento de probar las consultas, se indicaba que el número de consultas máximas había sido alcanzado.
- La API Key de OpenAI caduco.



## Autor
- Camilo Cantillo Tatis
