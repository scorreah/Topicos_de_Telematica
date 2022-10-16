# **Lab03 - Docker Wordpress SSL Distributed**

### **Información general**
> Info de la materia: ST0263 Tópicos especiales en telemática

> Estudiante(s): 
> * Simón Correa Henao, scorreah@eafit.edu.co

> Profesor: Edwin Nelson Montoya, emontoya@eafit.edu.co

---  

## **1. Breve descripción de la actividad**

Se realizó el despligue de una aplicación monolitica del CMS de Wordpress en Docker con balanceo y alta disponibilidad. Se hizo uso de varias maquinas virtuales alojadas en Google CLoud Platform, con un dominio gratuito de Freenom y un servidor DNS alojado también en Cloud DNS de GCP. Además la aplicación cuenta con certificado SSL emitido por Letsencrypt.
### **1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)**

* La aplicación debe contar con un balanceador de carga implementado con Nginx
* El balanceador de carga debe contar con un certificado SSL valido, es decir funcionar con el protocolo https
* El certificado SSL debe ser emitido por la CA Letsencrypt, por medio de la herramienta Certbot.
* Los servidores con Wordpress deben estar desplegados en maquinas virtuales en Google Cloud Platform (GCP), con IP Elástica en el puerto 443.
* Los servidores con Wordpress deben tener acceso a una instancia de base de datos externa.
* La instancia de base de datos debe utilizar el gestor de bases de datos MySQL
* Los servidores con Wordpress deben tener acceso a una instancia de NFS por el cual se compartirán los archivos del servidor.
* Las maquinas deben instanciar Wordpress, Nginx y MySQL, respectivamente, desde Docker y Docker-Compose
* Todas las instancias deben contar con direcciones IP elasticas
* La dirección IP elastica del balanceador debe contar con un dominio, expedido por el provedor de dominios Freenom
* El servidor DNS debe estar alojado en la nube, particularmente en la GCP
  
---  

## **2. Información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas**

- Se hace uso de una arquitectura Cliente-Servidor 
- El CMS desplegado es Wordpress con Contenedores
- El balanceador hace uso de Nginx con Contenedores
- La base de datos hace uso de MySQL con Contenedores
- Se hace el despliegue en GCP, con e2.micro y e2.small
- Los servidores contienen Wordpress, MySQL y Nginx dockerizados con Docker Compose, respectivamente.
- Las maquinas virtuales son instancias de Ubuntu 20.04 LTS
- El servidor DNS está alojado dentro de los servicios de GCP
- El dominio se encuentra en el provedor de dominios Freenom
- El certificado SSL es expedido por Letsencrypt
  
     **Diseño de alto nivel:**  
     ![image text](img/architecture.png)  
  
---

## **3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**
  
### **Detalles técnicos**  

*    **Tecnologías:**  
    ![image text](img/tech.png)  
* **Sistema Operativo**: Ubuntu 20.04 LTS
* **CMS:** Wordpress 6.0.2
* **Base de Datos:** MySQL 
* **Lenguaje de programacion**: PHP 7.4.30
* **Docker**: Docker version 20.10.12
* **Nginx**: Nginx 1.23.1

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
En todas las maquinas vamos a seguir los siguientes pasos
   1. Nos conectamos a la maquina virtual, como explicado en [Como Conectarse al Servidor](#como-conectarse-al-servidor)
   2. Actualizamos los repositorios y paquetes
        ![](img/apt-update.png)
### **NFS**
   3. Instalamos NFS
        ![](img/nfs/nfs-install.png)
   4. Creamos el directorio que vamos a compartir y establecemos los permisos adecuados
        ![](img/nfs/create_nfs-share_folder.png)
   5. Establecemos la configuración del NFS, teniendo en cuenta la red privada que estamos utilizando en GCP
        ![](img/nfs/etc_exports.png)
        ![](img/nfs/red-vpc-interna.png)
   6. Actualizamos las reglas de firewall para permitir el protocolo de nfs
        ![](img/nfs/nfs-rules-updated.png)
   7. Nos dirigimos a la maquina wordpress y actualizamos sus paquetes y repositorios
        ![](img/nfs/sudo-apt-update-wordpress.png)
   8. Instalamos nfs en cada instancia de wordpress
        ![](img/nfs/wordpress-apt-install-nfs.png)
   9. Editamos la configuración de NFS en cada wordpress, e indicamos la carpeta a compartir
        ![](img/nfs/wordpress-etc-fstab.png)
   10. Instalamos Nginx en cada instancia de wordpress
        ![](img/nfs/wordpress-apt-install-nginx.png)
   11. Montamos la carpeta compartida en cada wordpress
        ![](img/nfs/wordpress-mount.png)
   12. Verificamos que se compartan los archivos entre las instancias creando un archivo y confirmando que se sincronice en las otras maquinas
        ![](img/nfs/wordpress-test-nfs.png)
### **Database**
   3. Instalamos Docker y Docker-Compose
        ![](img/mysql/apt-install-docker-compose.png)
        ![](img/mysql/Install%20docker.png)
   4. Lanzamos el servicio de Docker
        ![](img/mysql/enable-docker.png)
   5. Editamos y lanzamos el docker-compose.yaml
        ![](img/mysql/docker-compose-yaml.png)
        ![](img/mysql/docker-compose-up.png.png)
   6. Creamos los usuarios en MySQL
        ![](img/mysql/mysql-users-creation.png)
   7. Actualizamos las reglas del firewall
        ![](img/mysql/ufw-rules.png)

### **Load Balancer**
   3. Instalamos Certbot
        ![](img/lb/install-certbot.png)
   4. Instalamos letsencrypt
        ![](img/lb/install-letsencrypt.png)
   5. Instalamos ngingx:
        ![](img/lb/install-nginx.png)
   6. Editamos la configuración de Nginx:
        ![](img/lb/editing-nginx-initial.png)
        ![](img/lb/install-nginx1.png)
   7. Con la configuración de Nginx reconfigurada, creamos la carpeta correspondiente para letsencrypt y recargamos Nginx
        ![](img/lb/mkdir-letsencrypt.png)
   8. Ahora ejecutamos Letsencrypt para pedir el certificado SSL para registros especificos
        ![](img/lb/cert-lab4.png)
   9. Entonces, ejecutamos certbot para pedir certificado SSL para todo el dominio (wildcard):Y al generarse el hash procedemos a crear un registro DNS en GPC como se indica en los pasos:
        ![](img/lb/cert-scorreah.png)
        ![](img/lb/txt_cert.png)
        ![](img/lb/txt_cert1.png)
   10. Creamos la carpeta para los archivos de Nginx y SSL:
        ![](img/lb/mkdir-nginx-ssl.png)
   11. Copiamos los archivos necesarios de letsencrypt a nuestro wordpress y creamos el archivo options para Nginx:
        ![](img/lb/nano-options-ssl.png)
        ![](img/lb/cp-letsencrypt.png)
   12. Creamos la llave requerida ss-dhparams.pem y la añadimos a Wordpress
        ![](img/lb/dhparams.png)
   13. Realizamos las siguientes instrucciones para nuestro subdominio con NginX
        ![](img/lb/nginx-domain.png)
   14. Instalamos Docker, Docker-Compose:
        ![](img/lb/apt-install-docker.png)
   15. Descargamos el repositorio de la materia y copiamos los archivos necesarios:
        ![](img/lb/clone-repository.png)
   16. Habilitamos el servicio de Docker:
        ![](img/lb/enable-docker.png)
   17. Deshabilitamos NginX:
        ![](img/lb/disable-nginx.png)
   18. Editamos el archivo de configuración de docker-compose
        ![](img/lb/nano-docker-compose.png)
   19. Editamos el archivo de configuración de Nginx
        ![](img/lb/nano-nginx-conf.png)
        ![](img/lb/nginx-conf.png)
   20. Ejecutamos Docker-compose:
        ![](img/lb/docker-compose-up.png)
        ![](img/lb/docker-compose.png)
### **Wordpress**
   3. Instalamos Docker y Docker-Compose:
        ![](img/wordpress/apt-install-docker.png)
   4. Creamos el archivo docker-compose.yaml:
        ![](img/wordpress/docker-compose.png)
   5. Ejecutamos Docker-Compose up, teniendo en cuenta la configuración de la base de datos:
        ![](img/wordpress/docker-compose-up.png)
        ![](img/wordpress/mysql.png)
   6.  Configuramos Wordpress y listo, hemos terminado!
        ![](img/wordpress/wp-admin.png)
   7.  Finalmente, ingresamos al dominio [https://lab4.scorreah.tk/](https://lab4.scorreah.tk/) y podremos verificar el certificado SSL y la conexión https:
        ![](img/results.png)


## **4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones**
* **Cloud:** Google Cloud Platform (GPC)
* **Proveedor de Dominios:** Freenom
* **Servidor DNS:** GPC
* **URL:** https://lab4.scorreah.tk/
* **Clave SSH**: Por correo al profesor
* **IP de la maquina (LB)**: 34.172.116.101
* **IPs**: ![](img/instances.png)

### **Como conectarse al servidor.**
El servidor de GPC se encuentra corriendo constantemente, así que solo se necesita acceder mediante SSH, de la siguiente forma:

1. Se pega la clave publica y privada en la carpeta .ssh del home del usuario: (Claves enviadas al profesor por interno)
2. Se corre el siguiente comando en el home de la persona:
   ```bash
   eval $(ssh-agent -s)
   ssh-add ~/.ssh/gcp
   ssh scorreah@direccionIP
   ```
    ![](img/vm_connection.png)

 
### **Una mini guia de como un usuario utilizaría el software o la aplicación**
1. Ingresa desde el navegador a la pagina [https://lab4.scorreah.tk/](https://lab4.scorreah.tk/)

  
---

## **5. Otra información que considere relevante para esta actividad**

### **Referencias:**
- [Github st0263 Eafit - Docker Nginx Wordpress SSL Letsencrypt](https://github.com/st0263eafit/st0263-2022-2/tree/main/docker-nginx-wordpress-ssl-letsencrypt)

#### versión README.md -> 1.0 (2022-octubre)