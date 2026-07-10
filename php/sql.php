<?php
$conn = new mysqli("mysql", "root", "root", "iot_project");

if ($conn->connect_error) {
    die("MySQL connection failed");
}

$result = $conn->query("SELECT * FROM air_quality_readings ORDER BY created_at DESC LIMIT 20");
?>

<!DOCTYPE html>
<html>
<head>
    <title>MySQL Air Quality Data</title>
    <meta http-equiv="refresh" content="5">
</head>
<body>
<h1>MySQL: Air Quality Data</h1>
<a href="index.php">Back</a>

<table border="1" cellpadding="8">
<tr>
    <th>ID</th>
    <th>Sensor</th>
    <th>Room</th>
    <th>Air Quality</th>
    <th>Status</th>
    <th>Time</th>
</tr>

<?php while ($row = $result->fetch_assoc()) { ?>
<tr>
    <td><?= $row["id"] ?></td>
    <td><?= $row["sensor_id"] ?></td>
    <td><?= $row["room_name"] ?></td>
    <td><?= $row["air_quality"] ?></td>
    <td><?= $row["status"] ?></td>
    <td><?= $row["created_at"] ?></td>
</tr>
<?php } ?>

</table>
</body>
</html>
