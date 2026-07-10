<?php
$manager = new MongoDB\Driver\Manager("mongodb://mongodb:27017");

$query = new MongoDB\Driver\Query([], [
    "sort" => ["_id" => -1],
    "limit" => 20
]);

$cursor = $manager->executeQuery("iot_project.climate_readings", $query);
?>

<!DOCTYPE html>
<html>
<head>
    <title>MongoDB Climate Data</title>
    <meta http-equiv="refresh" content="5">
</head>
<body>
<h1>MongoDB: Temperature and Humidity Data</h1>
<a href="index.php">Back</a>

<table border="1" cellpadding="8">
<tr>
    <th>Sensor</th>
    <th>Room</th>
    <th>Temperature</th>
    <th>Humidity</th>
</tr>

<?php foreach ($cursor as $doc) { ?>
<tr>
    <td><?= $doc->sensor_id ?></td>
    <td><?= $doc->room_name ?></td>
    <td><?= $doc->temperature ?></td>
    <td><?= $doc->humidity ?></td>
</tr>
<?php } ?>

</table>
</body>
</html>
