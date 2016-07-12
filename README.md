# Babylon Health diabetes likelihood prediction - implementation by Fabrizio Margaroli

This module allows the user to input her/his own data through a form (welcome.tpl, error pages are not_found.tpl,
error.tpl) running on a webserver (webserver.py). The data is read on the fly by a script (score_calculator.py)
that computes the diabetes score according to the specifications provided by BabylonHealth - with some
assumptions by myself on its impact due to age, smoke and alchool - and returns the user the likelihood to
develop Type 2 Diabetes (T2D) in the next 8 years.
The webserver chosen is Bottle (bottle.org), that is a simple and lightweight WSGI micro web-framework.
To run it:
python webserver.py
then open http://localhost:8084/
and input her/his own data.

The form used html5 required input type  as a simple validation type: this is not supported by Safari.

## Code limitations:

-I was planning to use SQLite to store all the users data in two tables, one for the generic users' data
and one for data strictly inherent to the diabetes score. The tables would be linked by keys, and the user table would
be linked to BabylonHealth other informations on the user. A complete prototype should include a database, and a
complete production code would replace SQLlite with a full database - mySQL for instance - to allow for network access,
concurrency, and manipulation of large data.

-the code has been tested manually; however the the score_calculator.py should have more control checks to
allow for data compatibility with its operations: assure form data integrity/correct units (height has to be a float
and should be reported in meters, etc.) and unit tests should be added

-comments/descriptions have been added in most places; would need some comments on the webserver.py

## Model limitations:

-the form mandates the presence of all data from the user. This is enforced as the score calculator makes sense
only if all data is available. One possible solution would be to use population average values for that particular
predictor. Do not recommend that as it increases the variance of the model.

-the model could be improved accounting for other known T2D predictors: history of disease correlated to T2D
(gestational diabetes, polycystic ovarian syndrome) physical activity, diet, and waist circumference.
They all could be easily added once their relative weight in the model is known.
The physical activity can be reliably assesses using a simple questionnaire:
http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3292724/pdf/10654_2011_Article_9625.pdf.
Diet could be assessed via a questionnaire. The user could be instructed on how to measure waist circumference
using a short video.


