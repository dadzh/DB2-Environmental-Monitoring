<?php
$url = "http://neo4j:7474/db/neo4j/tx/commit";

$cypher = " MATCH (s:Sensor)-[:PLACED_IN]->(r:Room)-[:HAS_DEVICE]->(d:Device)
            RETURN s.id, r.name, d.name
            LIMIT 20";

$query = [
    "statements" => [
        ["statement" => $cypher]
    ]
];

$options = [
    "http" => [
        "method" => "POST",
        "header" => "Content-Type: application/json\r\n" .
                    "Authorization: Basic " . base64_encode("neo4j:password") . "\r\n",
        "content" => json_encode($query)
    ]
];

$context = stream_context_create($options);
$response = file_get_contents($url, false, $context);
$data = json_decode($response, true);
$rows = $data["results"][0]["data"] ?? [];
?>

<!DOCTYPE html>
<html>
<head>
    <title>Neo4j Graph Data</title>
    <meta http-equiv="refresh" content="5">
</head>
<body>
<h1>Neo4j: Sensor Room Device Graph</h1>
<a href="index.php">Back</a>

<table border="1" cellpadding="8">
<tr>
    <th>Sensor</th>
    <th>Room</th>
    <th>Device</th>
</tr>

<?php foreach ($rows as $row) { ?>
<tr>
    <td><?= $row["row"][0] ?></td>
    <td><?= $row["row"][1] ?></td>
    <td><?= $row["row"][2] ?></td>
</tr>
<?php } ?>

</table>
</body>
</html>
