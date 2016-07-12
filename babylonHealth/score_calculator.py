"""
    score_calculator.py is called by the webserver.py once the user inputs her/his data. It manipulates the inputs in
    order to compute score related to the user's medical data, and transforms the score into a likelihood to develop
    T2D in the next 8 years
"""

def ageFactor(age, smoke, alchool):
    """
        Assumes that the 8 year risk to develop T2D increases linearly with age after age 40,
        and exponentially if the user is smoker or heavy drinker. It then computes extra points
        due to these predictors. The linearity coeffiecient is assumed to be 0.05.
        The exponent is 1.2 if smoker or drinker, and 1.23 if both. All these numbers are arbitrary
        and should be checked against most recent medical literature.

        Args:
            age: the user age
            smoke: whether the user has been smoking in the past 5 years
            alchool: whether the user drinks more than average

        Returns:
            points (integer) computed using the assumption above, to be added to points from other predictors
    """
    factor_age = 0
    if age >= 40:
        if smoke == "no" and alchool == "no":
            factor_age = (age-40)*0.05
        elif smoke == "no" and alchool == "yes":
            factor_age = ((age-40)**1.2)*0.05
        elif smoke == "yes" and alchool == "no":
            factor_age = ((age-40)**1.2)*0.05
        elif smoke == "yes" and alchool == "yes":
            factor_age = ((age-40)**1.23)*0.05
    else:
        factor_age = factor_age

    return int(round(factor_age))


def BMIpoint(weight, height):
    """
        Computes BMI using the usual formula, associates points to it under BabylonHealth assumptions

        Args:
            weigth: the user weigth in kilograms
            height: the user height in meters

        Returns:
            pointBMI: points computed using the assumption above, to be added to points from other predictors
    """
    point_BMI = 0

    BMI = weight/(height**2)
    if 25 <= BMI < 30:
        point_BMI = 2
    elif BMI >= 30:
        point_BMI = 5

    return point_BMI


def HDLCpoint(HDLC, sex):
    """
        Associates points to Cholesterol under BabylonHealth assumptions

        Args:
            HDLC: the user's HDL-C level
            sex: the user's sex

        Returns:
            pointHDLC: points computed using the assumption above, to be added to points from other predictors
    """
    pointHDLC=0

    if (HDLC < 40 and sex == "M") or (HDLC < 50 and sex == "F"):
         pointHDLC=5

    return pointHDLC


def overallscore(sex,height,weight,glucose,HDLC,trygl,blpress,age,family,smoke,alchool):
    """
        Computes starting from the keys of the dictionary data (the user's data) the overall T2D score

        Args:
            sex:
            height:
            weight:
            glucose: fasting glucose levels
            HDLC:    HDL-C levels
            trygl:   triglycerids
            blpress: blood pressure
            age:
            family:
            smoke:
            alchool:
        Returns:
            the overall score
    """
    pointTRI, pointGLU, pointFAM, pointBLO = 0, 0, 0, 0

    if trygl > 150:
        pointTRI = 3
    if glucose > 100:
        pointGLU = 10
    if family == "yes":
        pointFAM = 3
    if blpress == "yes":
        pointBLO = 2

    pointAGE = ageFactor(age, smoke, alchool)
    pointBMI = BMIpoint(weight, height)
    pointHDLC = HDLCpoint(HDLC, sex)

    return pointGLU + pointBMI + pointHDLC + pointFAM + pointTRI + pointBLO + pointAGE


def scoreToLikelihood(data):
    """
        maps score to likelihood to develop T2D in the next 8 years

        Args:
            data: the dictionary with the user data
        returns:
            likelihood: the 8y likelihood to develop T2D
    """

    scoremap = {10: 3, 11: 4, 12: 4, 13: 5, 14: 6, 15: 7, 16: 9, 17: 11, 18: 13, 19: 15, 20: 18,
                       21: 21, 22: 25, 23: 29, 24: 33}

    score = overallscore(**data)

    if score <= 10:
        likelihood = "< 3"
    elif score > 24:
        likelihood = "> 35"
    else:
        likelihood = scoremap.get(score)

    return likelihood