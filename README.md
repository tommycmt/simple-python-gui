# Simple-Python-GUI

This is a practising application for myself. Features of this application will be added without any milestone schedule.

## Getting Started

This is a simple python GUI application. The provided functions may not be useful at all.
This application is mainly using Python tkinter, selenium with BeautifulSoup to do the GUI and Web-scraping.
The structure of this application is built on OOP which may not be the best/good practise on making a python GUI application.

### Prerequisites

The things you need to install the software

* Python 3.x (recommend the latest version)
* BeautifulSoup
```
pip install beautifulsoup4
```

* selenium (with chrome webdriver)
```
pip install selenium
```

### Installing

To get this application

1. Clone this repository

```
git clone https://github.com/tommycmt/simple-python-gui.git
```

2. Make sure the directory structure

```
simple-python-gui\
	README.md
	images\
		xxx.png
	root\
		main.py
		component\
			menubar.py
			...
		uiEvent
			command.py
		utility\
			weatherUtil.py
			applications\
				chromedriver.exe
```


## Run this application

Go to the root directory under simple-python-gui 

```
pythonw main.py
```

Wait for a while and wait the content is loaded
The following screenshot is a successful screen.

![Image of successful screen](https://github.com/tommycmt/simple-python-gui/blob/master/images/demo.png "screenshot")

## Built With

* [tkinter](https://wiki.python.org/moin/TkInter) - Python GUI
* [Selenium](https://www.seleniumhq.org/) - The browserr automaintion
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Screen-scraping

## Authors

* **Tommy Tang** - [tommycmt](https://github.com/tommycmt)

## License

This project is licensed under the Apache License, Version 2.0 - see the [LICENSE.md](LICENSE.md) file for details
