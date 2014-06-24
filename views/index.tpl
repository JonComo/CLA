<html>

<head>
    <title>CLA</title>
</head>

<body>

<h1>CLA: Cortical Learning Algorithm</h1>
<p>Version 0.1</p>

<!-- Visual representation -->
<h2>Visual Representation</h2>
<img src={{outputURL}} width="100" height="100">


<!-- Form for creating network -->
<h2>Create</h2>
<form action="/create" method="post">
Size: <input type="text" name="size" value={{networkSize}}><br>
<input type="submit" value="Submit">
</form>

<!-- Modify -->
<h2>Modify</h2>
<form action="/randomize">
    <input type="submit" value="Randomize">
</form>

<!-- Train -->

<h2>Training</h2>

<!-- form for uploading image sequence -->
<form action="/upload" method="post" enctype="multipart/form-data">
  Select images: <input type="file" name="uploads[]" multiple="multiple" />
  <input type="submit" value="Start upload" />
</form>

</body>

</html>