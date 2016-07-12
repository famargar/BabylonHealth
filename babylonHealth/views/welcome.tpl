<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
<title>Babylon Health form  </title>
</head>
<body>

<h1>Give me your details !!</h1>

    <form method="post" action="/person_detail">
      <table>
        <tr>
          <td>
            Name
          </td>
          <td>
            <input type="text" name="name" value="" required>
          </td>
        </tr>
        <tr>
          <td>
            Lastname
          </td>
          <td>
            <input type="text" name="lastname" value="" required>
          </td>
        </tr>
        <tr>
          <td>
            email
          </td>
          <td>
            <input type="text" name="email" value="" required>
          </td>
        </tr>
        <tr>
          <td>
            gender
          </td>
           <td>
            <input type="radio" name="sex" value="F"> Female<br>
             <input type="radio" name="sex" value="M"> Male<br>
          </td>
        </tr>
        <tr>
          <td>
            height (m)
          </td>
          <td>
            <input type="text" name="height" value="" required>
          </td>
        </tr>
        <tr>
          <td>
            weight (kg)
          </td>
          <td>
            <input name="weight" value="" type="text" required>
          </td>
        </tr>
         <tr>
          <td>
            glucose
          </td>
          <td>
            <input type="text" name="glucose" value=""  required>
          </td>
        </tr>
         <tr>
          <td>
            HDLC
          </td>
          <td>
            <input type="text" name="HDLC" value=""  required>
          </td>
        </tr>

        <tr>
          <td>
            trygl
          </td>
          <td>
            <input type="text" name="trygl" value=""  required>
          </td>
        </tr>
        <tr>
          <td>
            blpress
          </td>
          <td>
            <input type="text" name="blpress" value=""  required>
          </td>
        </tr>

        <tr>
          <td>
            age
          </td>
          <td>
            <input name="age" value="" type="number" required>
          </td>
        </tr>
        <tr>
          <td>
            fam
          </td>
          <td>
             <input type="radio" name="fam" value="yes"> Yes<br>
             <input type="radio" name="fam" value="no"> No<br>
          </td>
        </tr>
        <tr>
          <td>
            smoke
          </td>
          <td>
            <input type="radio" name="smoke" value="yes"> Yes<br>
             <input type="radio" name="smoke" value="no"> No<br>
          </td>
        </tr>
        <tr>
          <td>
            alchool
          </td>
          <td>
             <input type="radio" name="alchool" value="yes"> Yes<br>
             <input type="radio" name="alchool" value="no"> No<br>
          </td>
        </tr>
      </table>
      <input type="submit" value="give me my risk!">
    </form>
</body>
</html>