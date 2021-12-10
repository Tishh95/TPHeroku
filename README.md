# TPHeroku

Pour voir l'application voici le lien:

  https://test2060.herokuapp.com/
  
  
  https://test2060.herokuapp.com/exemple



Commande a utilisé:

  sudo docker build -t flask-heroku:V2 .
    
  sudo docker run  -p 5000:5000 flask-heroku:V2
  
  sudo heroku container:push web --app test2060
  
  sudo heroku container:release web --app test2060


