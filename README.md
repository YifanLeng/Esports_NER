# Esports contents NER and NEL

This is a Django web application that performs named entity tagging and linking in Esports text (and specifically DOTA2, League of Legends, CS:GO and Overwatch). Our refined ontology contained 5 kinds of entities: GAME, TOURN, ORG, PLAYER, and AVATAR, defined as below:

* GAME: The esports title.
* TOURN:  An esports event or league.
* ORG: The "team" in which name players play for.
* PLAYER: Individuals who play and compete on the game as a career (in other words, “pro players”).
* AVATAR: The character that a player controls. In CS:GO, it is the item that a player uses.

The search bar accepts a URL or text snippet and the web application taggs the above entities from the text extracted. Each entity links to another page that shows its related information in Liquipedia with a URL. A mention and its alias will have the same entry and URL in Liquipedia which suggests succesful named entity linking. 

## Getting Started

To get a copy of this code repository, run the following command

```
git clone https://github.com/YifanLeng/Esports_NER.git
```


### Prerequisites

The following additional python packages are required to run the web app.

```
Django==2.2.6
spacy==2.1.8
beautifulsoup4==4.6.3
```

### Installing
Use pip to install the dependencies. Replace package with the package name and version specified in prerequisite.
```
pip install package
```


## How to run


```
cd Esports_NER
python manage.py runserver
```


## Deployment

The website is currently deployed on http://lengyifan.pythonanywhere.com/


## Built With

* [Django](https://www.djangoproject.com/) - The web framework 


## Authors

* **Yifan Leng** 

## License

This project is licensed under the MIT License 


