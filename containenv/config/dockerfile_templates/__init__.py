templates = {"ubuntu": '''FROM   ubuntu:latest
RUN    DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y\
{% for aptinstallable in APTINSTALLS %}
       {{ aptinstallable }} \{% endfor%}
       && rm -rf /var/lib/apt/lists/*'''}
