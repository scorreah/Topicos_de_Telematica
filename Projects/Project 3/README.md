# **Project 3 - Spark con Notebooks y PySpark**

### **Información general**
> Info de la materia: ST0263 Tópicos especiales en telemática

> Estudiante(s): 
> * Simón Correa Henao, scorreah@eafit.edu.co

> Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co

---  

## **1. Breve descripción de la actividad**

Trabajando con los datos del dataset de Casos Positivos de Covid 19 en Colombia, se hicieron operaciones con los datos por medio de PySpark. Se trabajó con los datos almacenados en AWS S3 y en Google Drive. Se hicieron operaciones sobre los datos y contestaron una serie de preguntas.

### **1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)**

* Las operaciones sobre los datos se realizaron en Google Colab
* Las operaciones sobre los datos se realizaron por medio del dataframe PySpark
* Las operaciones sobre los datos se realizaron por medio de PySpark SQL
* Los datos fueron obtenidos a partir del dataset de Casos Positivos de Covid 19 en Colombia
* Se trabajaron con los datos con origen en AWS S3 y en Google Drive
  
---  

## **2. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**
  
### **Detalles técnicos**  

* **Servicios:** Jupyter, Google Colab, Google Drive
* **Dataframe:** PySpark
* **Bucket:** AWS S3

## **Detalles del desarrollo**
## **0) Almacenar datos en AWS S3 y en Google Drive**
### **Descarga de datos con los que trabajar**
   1. Podemos obtener los datos del repositorio o de [datos.gov.co](https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD):
        ![](img/download-repo.png)
### **Carga a Google Drive y ejecución desde Google Colab**
   2. Luego nos conectamos a nuestro Google Drive personal y cargamos los archivos:
        ![](img/google-colab.png)
   3. En la carpeta st0263-2266 > bigdata > 03-spark, damos click derecho en el archivo google-colab-setup-pyspark.ipynb, abrir con > Conectar más aplicaciones y elegimos Google Colab:
        ![](img/google-colab-2.png)
        ![](img/google-colab-3.png)
   4. Ahora, para confirmar su correcto funcionamiento, ejecutamos todo el archivo:
        ![](img/spark.png)
        ![](img/spark-1.png)
        ![](img/spark-2.png)
        ![](img/spark-3.png)
        ![](img/spark-4.png)
### **Carga a S3**
   2. Para cargar los datos a S3:
        ![](img/load-to-s3.png)
        ![](img/load-to-s3-1.png)
        ![](img/load-to-s3-2.png)
## **1) Cargar datos desde AWS S3 y desde Google Drive.**
### **Carga desde S3 y conexión a AWS**
El notebook a utilizar es [google_colab_setup_pyspark_aws.ipynb](google_colab_setup_pyspark_aws.ipynb):
   1. Entramos a AWS Learning Lab y damos click en AWS Details, una vez lanzada la sesión:
        ![](img/spark-aws.png)
   2. Copiamos estas 3 variables y las pegamos en el notebook (Linea 4):
        ![](img/spark-aws-1.png)
        ![](img/spark-aws-2.png)
        ![](img/spark-aws-3.png)
   3. Probamos a ejecutar el resto del notebook para verificar su correcto funcionamiento:
        ![](img/spark-aws-4.png)
        ![](img/spark-aws-5.png)
        ![](img/spark-aws-6.png)
        ![](img/spark-aws-7.png)
        ![](img/spark-aws-8.png)
### **Carga desde Google Drive**
El notebook a utilizar es [google_colab_setup_pyspark.ipynb](google_colab_setup_pyspark.ipynb):
   1. Copiamos la ruta del archivo con el que vamos a trabajar:
        ![](img/spark-gc.png)
   2. Añadimos esta linea en el notebook:
        ![](img/carga-drive.png)
   3. Probamos a ejecutar los primeros pasos del notebook para verificar su correcto funcionamiento:
        ![](img/spark-gc-1.png)
        ![](img/spark-gc-2.png)

## **2) Análisis exploratorio del dataframe donde cargamos los datos**
> Este punto se realizó con el archivo [Data_processing_using_PySpark_aws_P3.ipynb](Data_processing_using_PySpark_aws_P3.ipynb) para el caso de AWS
> Este punto se realizó con el archivo [Data_processing_using_PySpark_google_colab_P3.ipynb](Data_processing_using_PySpark_google_colab_P3.ipynb) para el caso de Drive
### **2.1) Columnas**
   1. Mostramos las columnas del archivo y la cantidad de columnas:
        ![](img/spark-gc-3.png)
        ![](img/spark-gc-4.png)
### **2.2) Tipos de datos**
   1. Para mostrar los tipos de datos del csv:
        ![](img/spark-gc-5.png)
### **2.3) Seleccionar algunas columnas**
   1. Para todas las columnas o algunas especificas:
        ![](img/spark-gc-6.png)
### **2.4) Renombrar columnas**
   1. Para seleccionar dos columnas y renombrar una de ellas:
        ![](img/spark-gc-7.png)
### **2.5) Agregar columnas**
   1. Para agregar una columna adicional a partir del calculo con columnas existentes:
        ![](img/spark-gc-9.png)
### **2.6) Borrar columnas**
   1. Para seleccionar varias columnas y borrar una de ellas:
        ![](img/spark-gc-8.png)
### **2.7) Filtrar datos**
   1. Para filtrar los datos por un valor especifico:
        ![](img/spark-gc-10.png)
### **2.8) Ejecutar alguna función UDF o lambda sobre alguna columna creando una nueva.**
   1. Ejemplo de funcion UDF, columna adicional al final:
        ![](img/spark-gc-11.png)
## **3) Preguntas sobre los Datos de Covid**
> Este punto se realizó con el archivo [Data_processing_using_PySpark_aws_P3.ipynb](Data_processing_using_PySpark_aws_P3.ipynb) para el caso de AWS
> Este punto se realizó con el archivo [Data_processing_using_PySpark_google_colab_P3.ipynb](Data_processing_using_PySpark_google_colab_P3.ipynb) para el caso de Drive
### **3.1) Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor.**
   1. Con Dataframes:
        ![](img/3-1-dataframe.png)
   2. Con Spark SQL:
        ![](img/3-1-spark-sql.png)
### **3.2) Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor.**
   1. Con Dataframes:
        ![](img/3-2-dataframe.png)
   2. Con Spark SQL:
        ![](img/3-2-spark-sql.png)
### **3.3) Los 10 días con más casos de covid en Colombia ordenados de mayor a menor.**
   3. Con Dataframes:
        ![](img/3-3-dataframe.png)
   4. Con Spark SQL:
        ![](img/3-3-spark-sql.png)

### **3.4) Distribución de casos por edades de covid en Colombia.**
   5. Con Dataframes:
        ![](img/3-4-dataframe.png)
   6. Con Spark SQL:
        ![](img/3-4-spark-sql.png)
### **3.5) Distribución de casos por tipo de contagio de covid en Colombia..**
   7. Con Dataframes:
        ![](img/3-5-dataframe.png)
   8. Con Spark SQL:
        ![](img/3-5-spark-sql.png)

## **4) Guardar datos anteriores en AWS S3**
   1. Seguimos los pasos de [Conexion a AWS](#carga-desde-s3-y-conexión-a-aws)
   2. Añadimos estas lineas al final despues de ejecutar el punto 3):
      ![](img/save.png)
## **3. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**
* **Cloud:** Amazon Web Services (AWS)
* **Dataframe:** PySpark
* **Bucket:** AWS S3

## **4. Otra información que considere relevante para esta actividad**

### **Referencias:**
- [Github Topicos_de_Telematica - Lab 6](../../Labs/Lab%206/README.md)
- [Github st0263 Eafit - Bigdata](https://github.com/st0263eafit/st0263-2022-2/tree/main/bigdata/03-spark)

#### versión README.md -> 1.0 (2022-noviembre)