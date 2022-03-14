# Vit'fée (Planificateur repas)

Application permettant de planifier les repas de la semaine !

## Pour commencer

Entrez ici les instructions pour bien débuter avec votre projet...

### Pré-requis

- Installer les requirements

```python
 pip install -r requirements.txt 
```
- Docker
- K3d (pour un test en local)
- Un compte Azure (pour tester sur un AKS)
- Terraform
- MysQL 
  
### Installation et démarrage

1. Pour tester en local il suffit de lancer docker compose
2. Pour tester sur k3d en local  il suffit de créer un cluster voici un exemple :
``` kubectl
k3d cluster create clusterComplexe --api-port 127.0.0.1:6551 --servers 1 --agents 1
```
et lancer les manifests dans le dossier kubernetes.
3. Pour deployer sur le cloud :
   - Créer cluster en lancant le script terraform
   - Lancer les maifests kubernetes
   

## Fabriqué avec

Python, Flask, CSS, HTML, MySQL, SQLAlchemy, Yaml, GithubAction, Terraform, Keubernetes, Docker.


## Versions


## Auteurs

## License

