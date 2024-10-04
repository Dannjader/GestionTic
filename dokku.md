## Para crear un servidor casero con Ubuntu Server e instalar Dokku, aquí te presento un paso a paso detallado:

### Paso 1: Instalación y configuración básica de Ubuntu Server

1. Descarga la imagen ISO de Ubuntu Server desde el sitio oficial.
2. Crea un USB booteable con la imagen ISO.
3. Conecta tu servidor casero y arranca desde el USB.
4. Sigue las instrucciones del instalador para instalar Ubuntu Server.
5. Configura la red, crea un usuario administrativo y completa la instalación.

### Paso 2: Actualización del sistema

Una vez instalado Ubuntu Server, actualiza el sistema:

```bash
sudo apt update
sudo apt upgrade -y
```

### Paso 3: Instalación de Docker

Dokku requiere Docker, así que lo instalamos primero:

```bash
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
```

Verifica que Docker esté funcionando correctamente:

```bash
sudo docker --version
```

### Paso 4: Instalación de Dokku

Descarga el script de instalación de Dokku y ejecútalo:

```bash
wget https://raw.githubusercontent.com/dokku/dokku/v0.35.3/bootstrap.sh
sudo DOKKU_TAG=v0.35.3 bash bootstrap.sh
```

Este proceso puede tardar unos minutos dependiendo de tu conexión a internet [3].

### Paso 5: Configuración inicial de Dokku

Una vez completada la instalación, abre un navegador y accede a la IP de tu servidor o al dominio que hayas configurado. Sigue las instrucciones en pantalla para:

1. Agregar una clave SSH pública.
2. Configurar el nombre de host virtual.

Si no tienes acceso a una interfaz web, puedes hacer esta configuración manualmente usando comandos dokku [3]:

```bash
# Añade tu clave SSH pública
cat ~/.ssh/id_rsa.pub | dokku ssh-keys:add admin

# Configura el dominio global
dokku domains:set-global tu-dominio.com
```

### Paso 6: Despliegue de tu primera aplicación

Para probar que todo funciona correctamente, crea una aplicación simple y despliégala:

```bash
mkdir mi-aplicacion
cd mi-aplicacion
git init
echo "Hola Mundo!" > index.html
git add .
git commit -m "Inicial"
git remote add dokku dokku@tu-servidor:mi-aplicacion
git push dokku main
```

### Consideraciones importantes:

- Asegúrate de tener al menos 1 GB de memoria RAM en tu servidor [3].
- Si usas un dominio, configúralo para que apunte a la IP de tu servidor.
- Dokku es compatible con Ubuntu 20.04/22.04/24.04 y Debian 10+ x64 [3].

### Resumen

Con estos pasos, habrás creado un servidor casero con Ubuntu Server e instalado Dokku, listo para desplegar aplicaciones fácilmente. Recuerda que Dokku es una plataforma como servicio (PaaS) que facilita mucho el proceso de despliegue y administración de aplicaciones [3].

Citations:
[1] https://dokku.com/docs~v0.9.4/
[2] https://www.youtube.com/watch?v=wkzkjnH9nbo
[3] https://dokku.com/docs/getting-started/installation/
[4] https://www.youtube.com/watch?v=UbTIGJCk5CY
[5] https://ipv6.rs/tutorial/Ubuntu_Server_Latest/Dokku/
[6] https://www.youtube.com/watch?v=1F8nLX_qgXs
[7] https://www.youtube.com/watch?v=1ZkMiq1a890
[8] https://medium.com/@josiahowensypsk/how-to-create-vpn-server-on-mac-1ba35da2ecda