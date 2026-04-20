
________________________________________
🎬 Movie Recommendation API & Data Analysis
Este proyecto consiste en una API funcional construida con FastAPI que ofrece consultas sobre un dataset de películas y un Sistema de Recomendación basado en contenido utilizando Machine Learning (ML).
🚀 Descripción del Proyecto
Se realizó un proceso completo de Data Engineering y Data Science:
1.	ETL: Limpieza de datos, desanidación de columnas y tratamiento de nulos.
2.	EDA: Análisis exploratorio para entender tendencias y palabras clave.
3.	ML: Implementación de un modelo de similitud de coseno con reducción de dimensionalidad (SVD) para optimizar el rendimiento en la nube.
________________________________________
🛠️ Instalación y Ejecución Local
1.	Clonar el repositorio:
Bash
git clone https://github.com/robbalca/api-peliculas.git
2.	Instalar dependencias:
Bash
pip install -r requirements.txt
3.	Ejecutar la API:
Bash
uvicorn main:app --reload
Luego, abre http://127.0.0.1:8000/docs en tu navegador.
________________________________________
📌 Endpoints de la API
La API cuenta con 7 funciones principales:
Endpoint	Descripción
/get_max_duration	Filtra la película con mayor duración según año, plataforma y tipo.
/get_score_count	Cantidad de películas con puntaje mayor a XX en un año determinado.
/get_count_platform	Retorna el número de películas por plataforma.
/get_actor	Actor con mayor aparición según plataforma y año.
/get_contents	Cantidad de contenido (películas/series) por plataforma.
/get_rating	Cantidad de ítems según su clasificación (rating).
/get_recommendation	Sistema de ML: Ingresa un título y recibe 5 películas similares.
________________________________________
🧠 El Modelo de Recomendación
Para optimizar el despliegue en Render (evitando errores de memoria RAM), se aplicaron las siguientes técnicas:
•	TF-IDF Vectorizer: Para convertir el texto de las descripciones en vectores numéricos.
•	Truncated SVD: Reducción de dimensiones para que la matriz de similitud sea ligera y rápida.
•	Carga con Pickle: Los datos procesados se cargan de forma inmediata al iniciar la API.
________________________________________
🌐 Despliegue
La API se encuentra desplegada en: [https://api-peliculas-ct1y.onrender.com/docs]
________________________________________
