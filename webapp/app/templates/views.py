<!DOCTYPE html>
<html>
 <head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<style>
  input[type=text] {
  width: 130px;
  box-sizing: border-box;
  border: 2px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  background-color: white;
  background-image: url('searchicon.png');
  background-position: 10px 10px;
  background-repeat: no-repeat;
  padding: 12px 20px 12px 40px;
  -webkit-transition: width 0.4s ease-in-out;
  transition: width 0.4s ease-in-out;
  }
  input[type=text]:focus {
  width: 100%;
  }
</style>

<style>
right{
 posiion: absolute;
 top: 10px;
 right: 10px;

}
</style>
<body style="height:1500px">



  <nav class="navbar navbar-expand-sm bg-light navbar-light fixed-top">
     <ul class="navbar-nav">
        <li class="nav-item">
           <img href="/heron/templates/homepage.html" src="static/heron1.png" alt="Logo" style="width:60px;">
        </li>
        <li><a class="nav-link" href="/login">Heron</a></li>
        <li><a class="nav-link" href="/Films">Film Details</a></li>
        <li><a class="nav-link" href="/Screenings">Screenings</a></li>
      </ul>

     <ul class="nav navbar-nav ml-auto">
        <li class="nav-item"><a class="fa fa-user-circle-o" style="font-size:36px;center"></a></li>
        <li class="nav-item"><a class="fa fa-shopping-basket"  style="font-size:36px;center"><a></i>
        <li class="nav-item>"><form class="form-inline" action="/action_page.php">
           <input align="center"  type="text" name="search" placeholder="Search..">
          </form>
        </li>
     </ul>
  </nav>
  <div>
  {% block content %}{% endblock %}
  </div>
  </html>