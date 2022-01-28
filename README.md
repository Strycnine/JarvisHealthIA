# JarvisHealthIA


## Projet :

 - Améliorer le modèle du projet [Medical MNIST](https://github.com/apolanco3225/Medical-MNIST-Classification "Medical MNIST")
 - Créer une interface dans laquelle on puisse classifier une ou plusieurs images à l'aide de [Flask](https://flask.palletsprojects.com/en/2.0.x/ "Flask")
 - Déployer l'API sur [Heroku](https://dashboard.heroku.com/ "Heroku") et [Azure](https://portal.azure.com "Microsoft Azure")


## Interface :

![Interface_upload](https://user-images.githubusercontent.com/86345325/144743606-e96b0170-0e1d-4c4c-b3c6-4e118fd5443b.png)
![Interface_result](https://user-images.githubusercontent.com/86345325/144743609-16516a1f-4957-4bf7-a743-4571541385b2.png)


## Déploiement :

 - [Heroku](https://jarvis-health-ia.herokuapp.com/ "Jarvis Health IA")
 - [MS Azure](https://mednist.azurewebsites.net/ "MedNIST")


## Tests :

```bash
pytest -v
```
![1pytest](https://user-images.githubusercontent.com/86345325/151562269-a0a36b9f-8415-4536-9912-adaff770a329.png)

```bash
pytest -v --cov=.
```
![pytest-cov](https://user-images.githubusercontent.com/86345325/151561519-ae95cc36-3c03-4853-b332-648103110777.png)
```bash
pytest --html=report.html
```
![pytest-html](https://user-images.githubusercontent.com/86345325/151561668-480e83d7-700e-421a-a063-57c0580fe787.png)
