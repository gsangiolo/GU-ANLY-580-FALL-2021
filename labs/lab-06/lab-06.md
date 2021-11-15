# Lab 06: Query matching with FastText and Virtex


## Launch a FastText service using the Virtex library in Python
The purpose of this lab is to expose you to a few things:

(a) The [FastText](https://fasttext.cc/docs/en/python-module.html) library in Python, which is a language modeling and text classification framework

(b) The idea that NLP systems typically take on the form of microservices, wherein specific functions, such as computing embeddings or computing similar words, are performed in isolation and accessed through HTTP requests (or other protocols such as gRPC).

(c) The [Advanced Rest Client](https://install.advancedrestclient.com/install) (ARC), which allows you to make HTTP requests containing data (such as JSON) to an HTTP endpoint.

(d) The [Virtex](https://pypi.org/project/virtex/) library, which provides a convenient way to expose your machine learning computation as a service over HTTP without having to write any networking code (see `query_matching_demo.py`, `query_matching_demo.sh`).


## Task I (20 pts)

1. Launch the FastText query matching service by running the following command from the terminal from within the `labs/lab-06/` directory:

    $ ./query_matching_demo.sh

2. Open your Advanced Rest Client application (you need to download it first)

    a. Enter `http://0.0.0.0:580` into the Request URL bar
    
    b. In the Body content type field choose `application/json`

    c. Click the body tab and enter `{"data": ["dogs", "bakery", "hose", "florida", "supreme"]}`

    d. Explore FastText by changing the words and looking at the matches. Paste of a few of the responses below:

    ``` 
    # Query results go here
    ``` 
Query Results:
{"data":[[[0.9300785064697266,"arctiidae"],[0.9237712621688843,"noctuidae"],[0.9216641783714294,"eupithecia"],[0.9213652610778809,"mollusk"],[0.9206809401512146,"geometridae"],[0.9193852543830872,"burrows"],[0.9190572500228882,"homo"],[0.9189303517341614,"hunting"],[0.9168787002563477,"tortricidae"],[0.9140787720680237,"conus"]],[[0.9736358523368835,"specialty"],[0.9631682634353638,"slogan"],[0.9589007496833801,"tavern"],[0.9555143713951111,"restaurant"],[0.9517912864685059,"steakhouse"],[0.9470339417457581,"flavors"],[0.9431126713752747,"adobe"],[0.9428221583366394,"corner"],[0.942036509513855,"1860s"],[0.9348995685577393,"missouri"]],[[0.0,"in"],[0.0,"."],[0.0,"of"],[0.0,"and"],[0.0,"a"],[0.0,"</s>"],[0.0,"("],[0.0,"zeynally"],[0.0,"徐嬌"],[0.0,"romanizations"]],[[0.9168912172317505,"decree"],[0.8954152464866638,"jurisdiction"],[0.8942437171936035,"salisbury"],[0.8920913338661194,"opportunities"],[0.8886478543281555,"biotechnology"],[0.8827422261238098,"depending"],[0.8791956901550293,"accreditation"],[0.8787104487419128,"collegiate"],[0.8769832253456116,"graduates"],[0.8687768578529358,"inns"]],[[0.9724624752998352,"labor"],[0.9721168279647827,"officer"],[0.9707459211349487,"commissioner"],[0.9703463315963745,"constituency"],[0.9677392840385437,"servant"],[0.9677126407623291,"regent"],[0.9675344824790955,"mohammed"],[0.9650437831878662,"tenure"],[0.9646663665771484,"tax"],[0.9618818163871765,"brigadier"]]],"error":null}

**Note for Windows users**: Virtex does not run on Windows (because it requires uvloop which unfortunately does not support Windows). As an alternative, you can run this on your machine using [Docker](https://docs.docker.com/desktop/windows/install/). Once you have docker installed, execute the following commands from within the `GU-ANLY-580/labs/lab-06` folder:

    $ docker build -t fasttext-demo .
    $ docker run -p 580:580 fasttext-demo:latest

And then head over to your rest client (step 2 above) to complete the task. Alternatively, you can interact with FastText programmatically from within Python, for example:

   ```python
   import fasttext
   
   model = fasttext.load_model("en.quant.bin")
   match = model.get_nearest_neighbors("italian")
   ```
