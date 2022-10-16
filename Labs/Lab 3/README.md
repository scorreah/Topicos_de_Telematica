# **Lab03 - Docker Wordpress SSL**

### **Información general**
> Info de la materia: ST0263 Tópicos especiales en telemática

> Estudiante(s): 
> * Simón Correa Henao, scorreah@eafit.edu.co

> Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co

---  

## **1. Breve descripción de la actividad**

Se realizó el despliegue de un servidor de wordpress implementado mediante docker, y con la adición de un certificado valido de ssl expedido por letsencrypt. Todo en una maquina virtual alojada en Google Cloud Platform, con un dominio gratuito de Freenom y un servidor DNS alojado también en Cloud DNS de GCP.
### **1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)**

* El servidor con Wordpress debe estar desplegado en una maquina virtual en Google Cloud Platform (GCP), con IP Elástica en el puerto 443.
* El servidor debe contar con un certificado SSL valido, es decir funcionar con el protocolo https
* El certificado SSL debe ser emitido por la CA Letsencrypt, por medio de la herramienta Certbot.
* La maquina debe instanciar Wordpress desde Docker y Docker-Compose
* La dirección IP elastica debe contar con un dominio, expedido por el provedor de dominios Freenom
* El servidor DNS debe estar alojado en la nube, particularmente en la GCP
  
---  

## **2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas**

- Se hace uso de una arquitectura Cliente-Servidor 
- El CMS desplegado es Wordpress con Contenedores
- Se hace el despliegue en GCP, con una t2.micro
- El servidor contiene Wordpress Dockerizado con Docker Compose, Php y MySQL
- La maquina virtual es una instancia de Ubuntu 20.04 LTS
- El servidor DNS está alojado dentro de los servicios de GCP
- El dominio se encuentra en el provedor de dominios Freenom
- El certificado SSL es expedido por Letsencrypt
  

    **Diseño de alto nivel:**  
    ![image text](img/architecture.drawio.png)  
  
---

## **3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**
  
### **Detalles técnicos**  

*    **Tecnologías:**  
    ![image text](img/tech.png)  
* **Sistema Operativo**: Ubuntu 20.04 LTS
* **CMS:** Wordpress 6.0.2
* **Base de Datos:** MySQL 
* **Lenguaje de programacion**: PHP 7.4.30
*  **Docker**: Docker version 20.10.12

## **Detalles del desarrollo**
### **Instancia en GCP con IP elastica y par de claves SSH**
   1. Dentro de Google Cloud Platform, en la sección Compute Engine --> Crear Instancia
        ![](img/Instancias.png)
   2. Creamos la instancia especificando el nombre de la maquina, tipo de maquina y la región (Dependiendo de esto cambiará el costo)
        ![](img/crear_instancia.png)
   3. Para este caso cambiamos el Sistema Operativo de la maquina para Ubuntu 20.04 LTS amd x86-64
        ![](img/crear_instancia1.png)
        ![](img/crear_instancia2.png)

   4. Ahora para obtener la IP elastica, nos dirigimos a Red VPC --> Direcciones IP --> Reservar Dirección Estatica Externa
        ![](img/red_vpc.png)
        ![](img/dir_estatica_externa.png)
   5. Le damos un nombre a la Dirección, para identificarla en GPC y lo adjuntamos
        ![](img/dir_estatica_externa1.png)
        ![](img/dir_estatica_externa2.png)
   6. Entonces quedará como a continuación:
        ![](img/red_vpc2.png)
   7. Ahora, para configurar las claves SSH, primero la generamos localmente:
        ![](img/ssh_key_instance.png)
   8. Luego en GPC damos click en Compute Engine --> Metadatos --> Editar --> Claves SSH. Y colocamos la clave publica generada previamente:
        ![](img/ssh_key.png)
        ![](img/ssh_key1.png)
        ![](img/ssh_key2.png)
### **DNS en GPC y Dominio en Freenom**
   1. Nos dirigimos a Market Place y buscamos DNS Cloud
        ![](img/cloud_dns.png)
   2. Damos Click en Ir a Cloud DNS y luego en Habilitar:
        ![](img/cloud_dns1.png)
        ![](img/cloud_dns2.png)
   3. Ahora en Servicios de Red --> Cloud DNS damos click en Crear Zona
        ![](img/cloud_dns3.png)
   4. En este punto creamos el archivo de zona:
        ![](img/dns_zone.png)
        ![](img/dns_zone1.png)
        ![](img/dns_zone2.png)
   5. Luego agregamos los registros DNS:
        ![](img/dns_zone3.png)
        ![](img/dns_zone4.png)
        ![](img/dns_zone5.png)
        ![](img/dns_zone6.png)
   6. Con esto hecho nos dirigimos a Freenom y buscamos el dominio que queremos solicitar:
        ![](img/freenom.png)
        ![](img/freenom1.png)
        ![](img/freenom2.png)
   7. Procedemos con los pasos requeridos:
        ![](img/freenom3.png)
        ![](img/freenom4.png)
        ![](img/freenom5.png)
   8. Ya habiendo reservado el dominio entramos a My Domains --> Manage Domain --> Nameservers
        ![](img/freenom6.png)
        ![](img/freenom7.png)
        ![](img/freenom8.png)
   9.  Y colocamos los servidores de GPC que aparecen en Cloud DNS en el registro NS que se creó al crear el archivo de zona:
        ![](img/freenom-gpc.png)
        ![](img/freenom9.png)
### **Implementación**
   1. Nos conectamos a la maquina virtual, como explicado en [Como Conectarse al Servidor](#como-conectarse-al-servidor)
   2. Actualizamos los repositorios y paquetes
        ![](img/apt-update.png)
   3. Instalamos Certbot
        ![](img/snap-certbot.png)
   4. Instalamos letsencrypt
        ![](img/apt-install-letsencrypt.png)
   5. Instalamos ngingx:
        ![](img/apt-install-nginx.png)
   6. Editamos la configuración de Nginx:
        ![](img/nging_conf.png)
        ![](img/nging_conf1.png)
   7. Con la configuración de Nginx reconfigurada, creamos la carpeta correspondiente para letsencrypt y recargamos Nginx
        ![](img/ngingx-service.png)
   8. Ahora ejecutamos Letsencrypt para pedir el certificado SSL para registros especificos
        ![](img/ssl_cert.png)
   9. Entonces, ejecutamos certbot para pedir certificado SSL para todo el dominio (wildcard):Y al generarse el hash procedemos a crear un registro DNS en GPC como se indica en los pasos:
        ![](img/txt_cert2.png)
        ![](img/txt_cert.png)
        ![](img/txt_cert1.png)
   10. Creamos las carpetas para wordpress y Docker Compose:
        ![](img/mkdir_wordpress.png)
   11. Copiamos los archivos necesarios de letsecnrypt a nuestro wordpress y creamos el archivo options para Nginx:
        ![](img/cp_files.png)
        ![](img/nginx-options.png)
   12. Creamos la llave requerida ss-dhparams.pem y la añadimos a Wordpress
        ![](img/dhparam.png)
   13. Realizamos las siguientes instrucciones para nuestro subdominio con NginX
        ![](img/domain.png)
        ![](img/cp-live.png)
   14. Instalamos Docker, Docker-Compose y Git:
        ![](img/apt-install-docker.png)
   15. Habilitamos el servicio de Docker:
        ![](img/docker-service.png)
   16. Descargamos el repositorio de la materia y copiamos los archivos necesarios:
        ![](img/git.png)
   17. Deshabilitamos NginX:
        ![](img/nginx_disable.png)
   18. Ejecutamos Docker-compose:
        ![](img/docker-compose.png)
        ![](img/docker-compose2.png)
   19. Finalmente, ingresamos al dominio [https://www.scorreah.tk/](https://www.scorreah.tk/) y podremos verificar el certificado SSL y la conexión https:
        ![](img/res_final.png)
   20. Configuramos Wordpress y listo, hemos terminado!
        ![](img/scorreah.png)

## **4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**
* **Cloud:** Google Cloud Platform (GPC)
* **Proveedor de Dominios:** Freenom
* **Servidor DNS:** GPC
* **URL:** https://www.scorreah.tk/
* **Clave SSH**: Por correo al profesor
* **IP de la maquina**: 34.172.116.101

### **Como conectarse al servidor.**
El servidor de GPC se encuentra corriendo constantemente, así que solo se necesita acceder mediante SSH, de la siguiente forma:

1. Se pega la clave publica y privada en la carpeta .ssh del home del usuario: (Claves enviadas al profesor por interno)
2. Se corre el siguiente comando en el home de la persona:
   ```bash
   ssh -i ~/.ssh/google_compute_engine scorreah@34.172.116.101
   ```
    ![](img/vm_connection.png)

 
### **Una mini guia de como un usuario utilizaría el software o la aplicación**
1. Ingresa desde el navegador a la pagina ![https://www.scorreah.tk/](https://www.scorreah.tk/)

  
---

## **5. Otra información que considere relevante para esta actividad**

### **Referencias:**
- [Github st0263 Eafit - Docker Nginx Wordpress SSL Letsencrypt](https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt)

#### versión README.md -> 1.0 (2022-septiembre)